from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

def upload_to(instance, filename):
    return 'avatars/%s' % filename
  
class UserProfile(models.Model):

    # We indicate the relationship to the user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name='Avatar', upload_to=upload_to, null=True, blank=True)

    def __str__(self):
        return self.user.username

    # Here I return the avatar or picture with an owl, if the avatar is not selected
    def get_avatar(self):
        if not self.avatar:
            return '/static/img/ava.jpg'
        return self.avatar.url

    # method to create a fake table field in read only mode
    def avatar_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_avatar())

    avatar_tag.short_description = 'Avatar'

class Agreement(models.Model):
    name = models.CharField(max_length=300, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    repeatable = models.BooleanField(default=False)
    repeat_time = models.TimeField(verbose_name="Повторять каждые", null=True, blank=True)
    # status = models.CharField(max_length=100, blank=True)
    finish_date = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agreement_customer')
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agreement_executor')
    
    class Meta:
      verbose_name = 'Соглашение'
      verbose_name_plural = 'Соглашения'
  
    def __str__(self):
      return u'{0}'.format(self.name)

class Act(models.Model):
    agreement_id = models.ForeignKey(Agreement, on_delete=models.CASCADE, related_name='acts')
    customer_sign = models.BooleanField(default=False)
    executor_sign = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
      return u'{0}'.format(self.agreement_id)
    
class Parametr(models.Model):
    act_id = models.ForeignKey(Act, on_delete=models.CASCADE, related_name='parametr')

class Transaction(models.Model):
    act_id = models.ForeignKey(Act, on_delete=models.CASCADE, related_name='transactions')
    customer_sign = models.BooleanField(default=False)
    executor_sign = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Report(models.Model):
    name = models.CharField(max_length=300, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

# Справочник
class Guide(models.Model):
    name = models.CharField(max_length=500, blank=False)
    # accounting_table_id = models.ForeignKey(AccountingTable, on_delete=models.CASCADE, related_name='guides')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
      verbose_name = 'Справочник'
      verbose_name_plural = 'Справочники'
  
    def __str__(self):
      return u'{0}'.format(self.name)

class GuideParams(models.Model):
    guide_id = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='guide_params')
    body = models.CharField(max_length=500, blank=False)

    class Meta:
      verbose_name = 'Поле справочника'
      verbose_name_plural = 'Поля справочника'
  
    def __str__(self):
      return u'{0}'.format(self.body)

class TechnicalTable(models.Model):
    name = models.CharField(verbose_name = 'Наименование', max_length=500, blank=False)
    labor_spend = models.TimeField(verbose_name = 'Затраченное на операцию время', blank=True, null=True)
    labor_cost = models.IntegerField(verbose_name = 'Стоимость часа работы', blank=True, null=True)
    consumables = models.ManyToManyField(GuideParams, related_name='technical_tables', through='Connection', blank=True)
    calculation = models.CharField(verbose_name = 'Формула расчёта', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'Техкарта'
        verbose_name_plural = 'Техкарты'

    def __str__(self):
      return u'{0}'.format(self.name)

    def save(self, *args, **kwargs):
        # self.name = 'sdf'
        super(AccountingTable, self).save(*args, **kwargs)

class AccountingTable(models.Model):
    name = models.CharField(verbose_name = 'Наименование', max_length=500, blank=False)
    contractor = models.CharField(max_length=500, blank=True, null=True)
    nomenclature = models.CharField(max_length=500, blank=True, null=True)
    amount = models.IntegerField(verbose_name = 'Количество', blank=True, null=True)
    price_production = models.DecimalField(verbose_name = 'Цена на входе', max_digits=9, decimal_places=2, blank=True, null=True)
    marginarity = models.IntegerField(verbose_name = 'Маржинальность', blank=False, null=True)
    price_base = models.DecimalField(verbose_name = 'Цена на выходе', max_digits=9, decimal_places=2, blank=True, null=True)
    contractor_sale = models.DecimalField(verbose_name = 'Скидка контрагенту', max_digits=5, decimal_places=2, blank=True, null=True)
    application = models.CharField(max_length=500, blank=True, null=True)
    payment = models.CharField(max_length=500, blank=True, null=True)
    technicals = models.ManyToManyField(TechnicalTable, related_name='accounting_tables', through='ConnectionTechAccount', blank=True)

    class Meta:
        verbose_name = 'Учётная таблица'
        verbose_name_plural = 'Учётные таблицы'

    def save(self, *args, **kwargs):
        self.price_base = self.price_production + (self.price_production/100 * self.marginarity)

        super(AccountingTable, self).save(*args, **kwargs)

class ConnectionTechAccount(models.Model):
    technical_table = models.ForeignKey(to='TechnicalTable', on_delete=models.CASCADE)
    accounting_table = models.ForeignKey(to='AccountingTable', on_delete=models.CASCADE)
    # amount = models.IntegerField(verbose_name = 'Количество продукции', blank=False, null=False)

    class Meta:
        verbose_name = 'Связь с техкартой'
        verbose_name_plural = 'Связи с техкартами'

    def __str__(self):
    #    return u'{0}'.format(self.technical_table.name)
        return f'{self.technical_table} {self.technical_table.name}'

class Connection(models.Model):
    technical_table = models.ForeignKey(to='TechnicalTable', on_delete=models.CASCADE)
    guide_params = models.ForeignKey(to='GuideParams', on_delete=models.CASCADE)
    amount = models.FloatField(blank=False, null=False)

    class Meta:
        verbose_name = 'Связь со справочником'
        verbose_name_plural = 'Связи со справочником'
    
    def __str__(self):
        return f'{self.guide_params.body} {self.technical_table.name}'