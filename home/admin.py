from django.contrib import admin
from home.forms import GuideForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.forms import BaseInlineFormSet
from home.models import Agreement, Act, Parametr, UserProfile, Guide, GuideParams, AccountingTable, Connection, TechnicalTable, ConnectionTechAccount


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
  list_display = ['name', 'created_date']
  search_fields = ['name']
  ordering = ['-created_date']

class TechnicalInline(admin.TabularInline):
  model = ConnectionTechAccount
  extra = 1
  can_delete = False

@admin.register(AccountingTable)
class AccountingTableAdmin(admin.ModelAdmin):
  form = GuideForm
  list_display = ['name']
  search_fields = ['name']
  ordering = ['-name']

  inlines = [TechnicalInline]

class ConnectionInline(admin.TabularInline):
  model = Connection
  extra = 1
  can_delete = False

@admin.register(TechnicalTable)
class TechnicalTableAdmin(admin.ModelAdmin):
  list_display = ['name']
  ordering = ['-name']

  inlines = [ConnectionInline]

@admin.register(GuideParams)
class GuideParamsAdmin(admin.ModelAdmin):
  list_display = ['body']
  search_fields = ['body']
  ordering = ['-body']

class GuideParamsInline(admin.TabularInline):
  model = GuideParams

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
  list_display = ['name', 'created_date']
  search_fields = ['name']
  ordering = ['-name']

  inlines = [GuideParamsInline]

@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
  pass

@admin.register(Parametr)
class ParametrAdmin(admin.ModelAdmin):
  pass

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['avatar_tag', 'user'] # Показываем в списке пользователей
    # readonly_fields = ['avatar_tag'] # Только просмотр
    # fields = ('avatar_tag', 'user') # Показываем аватар в админке

# class ProfileInline(admin.StackedInline):
#     model = UserProfile
#     # can_delete = False
#     fields = ['avatar_tag',] # Определяем поле для отображения аватара
#     # readonly_fields = ['avatar_tag'] # Только для чтения
 
# # # Создаём собственную форму в админке
# class EUserAdmin(UserAdmin):
#     # Specify what will be in the form of inline
#     inlines = [
#         ProfileInline 
#     ]
#     # modify the list of displayed fields to see the avatar with the other fields
#     list_display =('avatar_tag',) + UserAdmin.list_display
 
#     # and also create a method for getting the avatar tag from the user profile
#     def avatar_tag(self, obj):
#         return obj.userprofile.avatar_tag()
    
# # admin.site.register(UserProfile, UserProfileAdmin)
 
# admin.site.unregister(User)
# admin.site.register(User, EUserAdmin)