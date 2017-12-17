from django import forms
from .models import Auto

class AutoCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AutoCreateForm, self).__init__(*args, **kwargs)
        self.fields['patente'].label = "Matricula"

    class Meta:
        model = Auto
        #exclude = ['peso']
        fields = '__all__'
        widgets = {
            'patente': forms.DateInput(attrs={'class':'datepicker','style':'font-size:25px'}, format='%d-%m-%Y')
        }