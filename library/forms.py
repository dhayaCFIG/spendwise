from django import forms
from .models import Book,Loan
class BookForm(forms.ModelForm):
 class Meta:
  model=Book
  fields=["title","author","isbn","category","total_copies","available_copies"]
  widgets={f:forms.NumberInput(attrs={"class":"form-control"}) for f in ["total_copies","available_copies"]}
  widgets.update({f:forms.TextInput(attrs={"class":"form-control"}) for f in ["title","author","isbn","category"]})
 def clean(self):
  d=super().clean()
  if d.get("available_copies") is not None and d.get("total_copies") is not None and d["available_copies"]>d["total_copies"]: self.add_error("available_copies","Available copies cannot exceed total copies.")
  return d
class LoanForm(forms.ModelForm):
 class Meta:
  model=Loan
  fields=["student_name","roll_number","due_date"]
  widgets={"student_name":forms.TextInput(attrs={"class":"form-control"}),"roll_number":forms.TextInput(attrs={"class":"form-control"}),"due_date":forms.DateInput(attrs={"class":"form-control","type":"date"})}
