from django.db import models
class Transaction(models.Model):
 TYPES=[("INCOME","Income"),("EXPENSE","Expense")]
 CATEGORIES=[("SALARY","Salary"),("FOOD","Food"),("TRAVEL","Travel"),("BILLS","Bills"),("EDUCATION","Education"),("OTHER","Other")]
 title=models.CharField(max_length=100)
 transaction_type=models.CharField(max_length=10,choices=TYPES)
 category=models.CharField(max_length=20,choices=CATEGORIES,default="OTHER")
 amount=models.DecimalField(max_digits=10,decimal_places=2)
 date=models.DateField()
 notes=models.TextField(blank=True)
 class Meta: ordering=["-date","-id"]
 def __str__(self): return self.title
