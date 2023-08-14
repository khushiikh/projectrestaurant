from django.urls import path
from . import views

urlpatterns=[

    path('',views.index,name='index'),
    path('formContact',views.formContact,name='formContact'),
    path('order',views.order,name='order'),
    path('orderNow',views.orderNow,name='orderNow'),
    ]