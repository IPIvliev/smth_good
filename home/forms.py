from django import forms
from home.models import Guide, GuideParams

try:
    contractor_id = Guide.objects.get(name='Контрагенты')
except:
    contractor_id = 1

try:
    nomenclature_id = Guide.objects.get(name='Готовая продукция')
except:
    nomenclature_id = 1

try:
    application_id = Guide.objects.get(name='Статус заявки')
except:
    application_id = 1

try:
    payment_id = Guide.objects.get(name='Статус оплаты')
except:
    payment_id = 1

class GuideForm(forms.ModelForm):
    contractor = forms.ModelChoiceField(queryset=GuideParams.objects.filter(guide_id=contractor_id), label='Контрагент', widget=forms.Select)
    nomenclature = forms.ModelChoiceField(queryset=GuideParams.objects.filter(guide_id=nomenclature_id), label='Номенклатура', widget=forms.Select)
    application = forms.ModelChoiceField(queryset=GuideParams.objects.filter(guide_id=application_id), label='Статус заявки', widget=forms.Select)
    payment = forms.ModelChoiceField(queryset=GuideParams.objects.filter(guide_id=payment_id), label='Статус Оплаты', widget=forms.Select)

    # class Meta:
    #     model = Guide
    #     fields = ['name', 'contractor', ]
    def __init__(self, *args, **kwargs):
        super(GuideForm, self).__init__(*args, **kwargs)
        # self.fields['contractor'].queryset = Guide.objects.filter(id=item_id)
        self.fields['contractor'].empty_label = 'Выберите контрагента'