from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name ='index'),
    path('single/', views.single, name ='single'),
    path('category/', views.category, name ='category'),
    path('contact/', views.contact, name ='contact'),
    path('investment_stock/', views.invsetment_stock, name ='investment_stock'),
    path('investment_stock_chap1/', views.investment_stock_chap1, name ='investment_stock_chap1'),
    path('investment_stock_chap2/', views.investment_stock_chap2, name ='investment_stock_chap2'),

    path('cfa_lvl_1/', views.cfa_lvl_1, name ='cfa_lvl_1'),
    path('cfa_lvl_1_voca/', views.cfa_lvl_1_voca, name ='cfa_lvl_1_voca'),
    path('boston_college/', views.boston_college, name ='boston_college'),
    
]