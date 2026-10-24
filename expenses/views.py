from decimal import Decimal
from django.contrib import messages
from django.db.models import Q,Sum
from django.shortcuts import render,redirect,get_object_or_404
from .models import Transaction
from .forms import TransactionForm
def dashboard(request):
 q=request.GET.get("q","").strip()
 rows=Transaction.objects.all()
 if q: rows=rows.filter(Q(title__icontains=q)|Q(category__icontains=q)|Q(notes__icontains=q))
 income=Transaction.objects.filter(transaction_type="INCOME").aggregate(v=Sum("amount"))["v"] or Decimal("0")
 spent=Transaction.objects.filter(transaction_type="EXPENSE").aggregate(v=Sum("amount"))["v"] or Decimal("0")
 return render(request,"expenses/dashboard.html",{"rows":rows,"q":q,"income":income,"spent":spent,"balance":income-spent})
def add(request,pk=None):
 obj=get_object_or_404(Transaction,pk=pk) if pk else None
 form=TransactionForm(request.POST or None,instance=obj)
 if request.method=="POST" and form.is_valid():
  form.save(); messages.success(request,"Transaction saved."); return redirect("expense_dashboard")
 return render(request,"shared/form.html",{"form":form,"title":"Edit transaction" if obj else "Add transaction","back":"/"})
def delete(request,pk):
 obj=get_object_or_404(Transaction,pk=pk)
 if request.method=="POST": obj.delete(); messages.success(request,"Transaction deleted."); return redirect("expense_dashboard")
 return render(request,"shared/delete.html",{"obj":obj,"back":"/"})
