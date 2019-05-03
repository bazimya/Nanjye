from django import forms
from .models import PaymentForm

class ProfileForm(forms.Form):
   name = forms.CharField(max_length = 100)
   workers = forms.FileField()

class Payment(forms.ModelForm):
   class Meta:
      model= PaymentForm
      exclude=['transaction_code']
   # clienttime = forms.CharField(max_length = 100)