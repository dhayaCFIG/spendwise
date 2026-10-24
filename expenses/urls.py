from django.urls import path
from . import views
urlpatterns=[path("",views.dashboard,name="expense_dashboard"),path("expense/add/",views.add,name="expense_add"),path("expense/<int:pk>/edit/",views.add,name="expense_edit"),path("expense/<int:pk>/delete/",views.delete,name="expense_delete")]
