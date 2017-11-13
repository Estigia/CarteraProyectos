from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


def log_in(request):
    if request.user.is_authenticated():
        return redirect('projects:project_list')

    if request.POST:

        form = LoginForm(request.POST or None)

        context = {
            'form': form
        }

        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(
                        username=username,
                        password=password
                    )

            if not user:
                messages.error(request, 'USUARIO INVALIDO')
            elif not user.check_password(password):
                messages.error(request, 'CONTRASEÑA INCORRECTA')
            elif user is not None:

                if user.is_active:

                    login(request, user)

                    if request.GET:
                        if request.GET['next'] != '/logout/':
                            return HttpResponseRedirect(request.GET['next'])

                    return redirect('projects:project_list')
                else:
                    messages.error(request, 'USUARIO INACTIVO')

        return render(request, 'registration/login.html', context)

    else:
        form = LoginForm()

        context = {
            'form': form
        }

        return render(request, 'registration/login.html', context)
