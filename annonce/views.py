from django.shortcuts import render, get_object_or_404
from .models import Donne, Pret, Exchice
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from .forms import DonneForm
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout



def index(request):
    return render(request, 'annonce/index.html')

##########################
# Gift Views
##########################
# Post Gift
# View Gifts
# View Gift
