from django import forms
from .models import Transaction
class TransactionForm(forms.ModelForm):
 class Meta:
  model=Transaction
  fields=["title","transaction_type","category","amount","date","notes"]
  widgets={"title":forms.TextInput(attrs={"class":"form-control"}),"transaction_type":forms.Select(attrs={"class":"form-select"}),"category":forms.Select(attrs={"class":"form-select"}),"amount":forms.NumberInput(attrs={"class":"form-control","min":"0.01","step":"0.01"}),"date":forms.DateInput(attrs={"class":"form-control","type":"date"}),"notes":forms.Textarea(attrs={"class":"form-control","rows":2})}
 def clean_amount(self):
  x=self.cleaned_data["amount"]
  if x<=0: raise forms.ValidationError("Amount must be greater than zero.")
  return x
