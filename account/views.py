from django.shortcuts import render
from django.http import HttpResponse
from .services import hand_df, tarot_df


def login_view(request):
    return render(request, "login.html")