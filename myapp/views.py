from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from myapp.forms import *

''' Homepage Link '''


def home(request):
    return render (request, 'homepage.html')


''' Doctor Registration Form Logic '''


def doc_reg(request):
    if request.method == 'POST':
        form = Doctor_Form (request.POST)
        if form.is_valid ():
            form.save ()
            return HttpResponseRedirect ('/doc_login_form.html/')

    else:
        form = Doctor_Form ()
    return render (request, 'doc_reg_form.html', {'form': form})


''' Doctor Login Form Logic '''


def doc_login(request):
    print (request.method)
    if request.method == 'POST':
        search_username = request.POST.get ('username', None)
        search_password = request.POST.get ('password', None)
        print (search_username)
        print (search_password)
        try:
            user = Doctor.objects.get (username=search_username, password=search_password)
            # do something with user
            context = {
                'user': user,
            }
            return render (request, 'doc_profile_page.html', context=context)
            # return HttpResponse(html)
        except ObjectDoesNotExist:
            return HttpResponse ("Invalid credentials")
    else:
        return render (request, 'doc_login_form.html')


''' Patient Registration Form Logic '''


def pat_reg(request):
    if request.method == 'POST':
        form = Patient_Form (request.POST)
        if form.is_valid ():
            form.save ()
            return HttpResponseRedirect ('/')
    else:
        form = Patient_Form ()
    return render (request, 'pat_reg_form.html', {'form': form})
