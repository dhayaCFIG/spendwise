from django.db import models
class Book(models.Model):
 title=models.CharField(max_length=150)
 author=models.CharField(max_length=100)
 isbn=models.CharField(max_length=25,unique=True)
 category=models.CharField(max_length=60,default="General")
 total_copies=models.PositiveIntegerField(default=1)
 available_copies=models.PositiveIntegerField(default=1)
 def __str__(self): return f"{self.title} — {self.author}"
class Loan(models.Model):
 book=models.ForeignKey(Book,on_delete=models.PROTECT,related_name="loans")
 student_name=models.CharField(max_length=120)
 roll_number=models.CharField(max_length=30)
 due_date=models.DateField()
 returned=models.BooleanField(default=False)
 issued_at=models.DateTimeField(auto_now_add=True)
 def __str__(self): return f"{self.book.title} - {self.roll_number}"
