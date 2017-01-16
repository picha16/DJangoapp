from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hola a todos a mi app!!")
# Create your views here.
