from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from .models import Book,Loan
from .forms import BookForm,LoanForm
def listing(request):
 q=request.GET.get("q","").strip(); books=Book.objects.all()
 if q: books=books.filter(Q(title__icontains=q)|Q(author__icontains=q)|Q(isbn__icontains=q)|Q(category__icontains=q))
 loans=Loan.objects.filter(returned=False).select_related("book")
 return render(request,"library/list.html",{"books":books,"q":q,"loans":loans})
def book_form(request,pk=None):
 obj=get_object_or_404(Book,pk=pk) if pk else None
 form=BookForm(request.POST or None,instance=obj)
 if request.method=="POST" and form.is_valid():
  form.save(); messages.success(request,"Book saved."); return redirect("library_list")
 return render(request,"shared/form.html",{"form":form,"title":"Edit book" if obj else "Add book","back":"/library/"})
def book_delete(request,pk):
 obj=get_object_or_404(Book,pk=pk)
 if request.method=="POST":
  if obj.loans.exists(): messages.error(request,"Book has loan history and cannot be deleted.")
  else: obj.delete(); messages.success(request,"Book deleted.")
  return redirect("library_list")
 return render(request,"shared/delete.html",{"obj":obj,"back":"/library/"})
def issue(request,pk):
 book=get_object_or_404(Book,pk=pk)
 if book.available_copies<1: messages.error(request,"No copies available."); return redirect("library_list")
 form=LoanForm(request.POST or None)
 if request.method=="POST" and form.is_valid():
  loan=form.save(commit=False); loan.book=book; loan.save()
  book.available_copies-=1; book.save(update_fields=["available_copies"])
  messages.success(request,"Book issued."); return redirect("library_list")
 return render(request,"shared/form.html",{"form":form,"title":"Issue: "+book.title,"back":"/library/"})
def return_book(request,pk):
 loan=get_object_or_404(Loan,pk=pk,returned=False)
 if request.method=="POST":
  loan.returned=True; loan.save(update_fields=["returned"])
  book=loan.book; book.available_copies=min(book.total_copies,book.available_copies+1); book.save(update_fields=["available_copies"])
  messages.success(request,"Book marked as returned.")
 return redirect("library_list")
