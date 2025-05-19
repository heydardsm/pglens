from django.forms import Form
from django.views import View
from django.http import HttpRequest
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render

from monitoring.forms import LoginForm

class Login(View):

    def get(self, request: HttpRequest):
        return render(request, 'login.html', {})

    def post(self, request: HttpRequest):
        form: Form = LoginForm(data=request.POST)
        if not form.is_valid():
            context = {
                "error": True,
                "error_message": form.errors
            }
            return render(request, 'login.html', context)
        user = authenticate(
            request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"]
        )
        if user is None:
            context = {
                "error": True,
                "error_message": "Wrong username or password"
            }
            return render(request, 'login.html', context)
        return redirect('/')
