from django import forms

class ProfileForm(forms.Form):
   name = forms.CharField(max_length = 100)
   workers = forms.FileField()

class PaymentForm(forms.Form):
   destination = forms.CharField(max_length = 100)
   reson = forms.CharField(max_length = 100)
   typeofcns = forms.CharField(max_length = 100)
   amount = forms.CharField(max_length = 100)
   phonenumber = forms.CharField(max_length = 100)
   # clienttime = forms.CharField(max_length = 100)