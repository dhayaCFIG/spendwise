from django.urls import path
from . import views
urlpatterns=[path("",views.listing,name="library_list"),path("add/",views.book_form,name="book_add"),path("<int:pk>/edit/",views.book_form,name="book_edit"),path("<int:pk>/delete/",views.book_delete,name="book_delete"),path("<int:pk>/issue/",views.issue,name="book_issue"),path("loan/<int:pk>/return/",views.return_book,name="loan_return")]
