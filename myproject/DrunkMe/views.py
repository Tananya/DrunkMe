from django.shortcuts import render, redirect
from DrunkMe.models import Booking , Area , Bar , Drink 
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.db.models import Q
from itertools import chain
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  # <--
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm  # <--
from django.contrib.auth import update_session_auth_hash  # <--
from django.contrib import messages  # <--
from social_django.models import UserSocialAuth  # <--



def home(request):
	bar_list = Bar.objects.all()

	query = request.GET.get("q")
	if query:
		bar_list = bar_list.filter(Q(name__icontains=query))
		
	return render(request, 'home.html' , {'bar' : bar_list})

def event(request):
	
	return render(request, 'event.html')

def eventall(request):
	
	return render(request, 'eventall.html')

def detail(request , num = '1'):
	detail = Bar.objects.get(id=num)

	
	
	barname = request.GET.get("namebar")
	name = request.GET.get("name")
	phone = request.GET.get("phone")
	time = request.GET.get("time")
	people = request.GET.get("people")
	
	
	

	if name:
		b = Bar.objects.get(id=num)
		booking = Booking.objects.create(
								bar = b,
								name = name,
								phone = phone,
								time = time,
								people = people,)
	return render(request, 'detail.html' , {'detail' : detail})

def menu(request , num = '1'):
	barname = Bar.objects.get(id = num)
	
	return render(request, 'menu.html' , {'menu' : menu , 'barname' : barname})

def searchbar(request):
	bar_list = Bar.objects.all()

	query_type = request.GET.get("type")
	query_area = request.GET.get("area")

	if query_type or query_area:
		bar_list = Bar.objects.filter(Q(area__area__icontains=query_area) & Q(category__icontains=query_type))
	
	return render(request, 'searchbar.html' , { 'bar' : bar_list})

def searchdrink(request):

	drink_list = Drink.objects.all()


	return render(request, 'searchdrink.html' , { 'drink' : drink_list})

def nearby(request):
	bar_list = Bar.objects.all()

	query_type = request.GET.get("type")
	query_area = request.GET.get("area")

	if query_type or query_area:
		bar_list = Bar.objects.filter(Q(area__area__icontains=query_area) & Q(category__icontains=query_type))
	return render(request, 'nearby.html',{ 'bar' : bar_list})

def areas(request):
	area = Area.objects.all()
	return render(request, 'areas.html' , {'area' : area})

def areasdetail(request , num = '1'):
	area = Area.objects.get(id = num)
	barlist = Bar.objects.filter(area = area)
	idbar =''
	
	barname = request.GET.get("namebar")
	name = request.GET.get("name")
	phone = request.GET.get("phone")
	time = request.GET.get("time")
	people = request.GET.get("people")
	idbar = request.GET.get("idbar")
	
	

	if name:
		b = Bar.objects.get(id=idbar)
		booking = Booking.objects.create(
								bar = b,
								name = name,
								phone = phone,
								time = time,
								people = people,)


	return render(request, 'areasdetail.html' , {'bar' : barlist , 'area' : area})

def promotion(request):
	bar_list = Bar.objects.all()
	return render(request, 'promotion.html' , {'bar' : bar_list})

def happyhour(request):
	bar_list = Bar.objects.all()
	return render(request, 'happyhour.html' , {'bar' : bar_list})

def contents(request):
	area = Area.objects.all()
	return render(request, 'contents.html' , {'area' : area})

def drinks(request):
	return render(request, 'drinks.html')


def drinkdetail(request  , category = ''):
	drink_list = Drink.objects.filter(category = category)



	return render(request, 'drinkdetail.html' , {'drink' : drink_list , 'category' : category})

def typedrink(request  , typedrink = ''):
	drink_list = Drink.objects.filter(typedrink = typedrink)
	
	return render(request, 'typedrink.html' , { 'drink' : drink_list})


def recommended(request):
	
	return render(request, 'recommended.html')

def drinkdst(request , num = '1'):
	drink = Drink.objects.get(id=num)
	return render(request, 'drinkdst.html' , {'drink' : drink})


def loginbar(request):

	username = request.GET.get("username")
	password = request.GET.get("password")

	print(username)
	print(password)

	if username and password:
		bar = Bar.objects.filter(Q(Username__icontains=username) & Q(Password__icontains=password))
		
		if not bar:
			return render(request, 'loginbar.html')
		else:
			book = Booking.objects.filter(bar = bar).order_by('time')
			return render(request, 'book.html' , {'bar' : bar , 'book' : book})

		

	return render(request, 'loginbar.html')


def book(request):
	idbook = request.GET.get("idbook")

	if idbook:
		b = booking.objects.get(id=idbook)
		b.delete()
		return render(request, 'book.html' )

	return render(request, 'book.html' )

