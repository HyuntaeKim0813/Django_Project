from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# request handler
# action

def index(request):
    return render(request, 'index.html')

def single(request):
    return render(request, 'single.html')

def category(request):
    return render(request, 'category.html')

def contact(request):
    return render(request, 'contact.html')

def invsetment_stock(request):
    return render(request, 'investment_stock.html')

def investment_stock_chap1(request):
    return render(request, 'investment_stock_chap1.html')

def investment_stock_chap2(request):
    return render(request, 'investment_stock_chap2.html')

def cfa_lvl_1(request):
    return render(request, 'cfa_lvl_1.html')

def cfa_lvl_1_voca(request):
    return render(request, 'cfa_lvl_1_voca.html')

def boston_college(request):
    return render(request, 'boston_college.html')