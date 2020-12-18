from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from deposit.models import Deposit
from withdraw.models import Withdraw
import json

from notifications.models import Notification
from notifications.signals import notify
from accounts.models import User
from django.views.generic import CreateView, FormView, RedirectView
from .forms import *
from django.db.models import Q
from core.models import Feedback
from userprofile.models import Profile

def deposit_status(request):
    print("Sujit")
    if request.method == 'POST':
        id = request.POST['id']

        print(id)

        update = Deposit.objects.get(id=id, status=False)
        update.status = True
        update.save()

        notify.send(request.user, recipient=update.user, verb='complete a deposit',
                        level=Notification.LEVELS.success)
    
    return HttpResponse("Complete")






def complete_user(request):
    if request.method == 'POST':
        id = request.POST['id']
        forzzaUser = request.POST['forzzaUser']
        forzzaPass = request.POST['forzzaPass']
        update = User.objects.get(id=id)
        update.complete = True
        update.save()
        
        profile = Profile.objects.get(user__id=id)
        profile.forzza_username = forzzaUser
        profile.forzza_password = forzzaPass
        profile.save()
        
        notify.send(request.user, recipient=update, verb='Your Forzza Username is '+forzzaUser+' and Password is '+forzzaPass+ ' <a href="https://www.forzza.com/" target="_blank">click here</a> to login in Forzza',
                        level=Notification.LEVELS.success)
    return HttpResponse("Complete")





def add_user(request):
    if request.user.is_superuser == False:
        redirect('common:dashboard')

    users = User.objects.filter(Q(is_staff=True) & Q(is_active=True))

    context = {
        'users':users,
        'page_url' : '/admins/add/user'
    }

    if request.method == 'POST':
        if User.objects.filter(email=request.POST['email']).exists():
            messages.warning(request, 'This email is already taken')
            return redirect('common:add-user')

        user_form = UserRegistrationForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('common:add-user')
        else:
            print(user_form.errors)
            return render(request, 'accounts/register.html', {'form': user_form})

    return render(request, 'common/user/add_user.html', context)




def delete_user(request):
    if request.method == 'POST':
        id = request.POST['id']
        update = User.objects.get(id=id)
        update.is_active = False
        update.save()
    return redirect('common:add-user')



def withdraw_status(request):
    print("Sujit")
    if request.method == 'POST':
        id = request.POST['id']

        print(id)

        update = Withdraw.objects.get(id=id, status=False)
        update.status = True
        update.save()

        notify.send(request.user, recipient=update.user, verb='complete a withdraw',
                        level=Notification.LEVELS.success)

    
    return HttpResponse("Complete")


def deposit(request):
    context ={
        'page_url' : '/admins/deposit'
    }
    return render(request, 'common/deposit/deposit.html', context)


def request_user(request):
    context ={
        'page_url' : '/admins/request/user'
    }
    return render(request, 'common/request_user/user.html', context)


def request_pending(request):

    pendings = User.objects.filter(complete=False)

    context = {
        'pendings':pendings,
    }
    
    return render(request, 'common/request_user/request_pending.html', context)

def request_complete(request):

    completes = User.objects.filter(complete=True).order_by('-date_joined')

    context = {
        'completes':completes,
    }
    
    return render(request, 'common/request_user/request_complete.html', context)


def deposit_pending(request):

    pendings = Deposit.objects.filter(status=False)

    context = {
        'pendings':pendings,
    }
    
    return render(request, 'common/deposit/deposit_pending.html', context)

def deposit_complete(request):

    completes = Deposit.objects.filter(status=True).order_by('-date')

    context = {
        'completes':completes,
    }
    
    return render(request, 'common/deposit/deposit_complete.html', context)



def withdraw(request):  
    context ={
        'page_url' : '/admins/withdraw'
    }
    return render(request, 'common/withdraw/withdraw.html', context)


def withdraw_pending(request):

    pendings = Withdraw.objects.filter(status=False)

    context = {
        'pendings':pendings,
    }
    
    return render(request, 'common/withdraw/withdraw_pending.html', context)

def withdraw_complete(request):

    completes = Withdraw.objects.filter(status=True).order_by('-date')

    context = {
        'completes':completes,
    }
    
    return render(request, 'common/withdraw/withdraw_complete.html', context)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        deposit = Deposit.objects.all().count()
        deposit_pending = Deposit.objects.filter(status=False).count()
        deposit_complete = Deposit.objects.filter(status=True).count()

        withdraw = Withdraw.objects.all().count()
        withdraw_pending = Withdraw.objects.filter(status=False).count()
        withdraw_complete = Withdraw.objects.filter(status=True).count()
        user = User.objects.exclude(is_superuser = True).count()

        context['deposit'] = deposit
        context['deposit_pending'] = deposit_pending
        context['deposit_complete'] = deposit_complete
        context['withdraw'] = withdraw
        context['withdraw_pending'] = withdraw_pending
        context['withdraw_complete'] = withdraw_complete
        context['user'] = user
        context['page_url'] = '/admins/dashboard'
        return context
        


def feedback(request):
    if request.user.is_superuser == False:
        redirect('common:dashboard')

    feedback = Feedback.objects.all()

    context = {
        'feedback':feedback,
        'page_url' : '/admins/feedback'
    }

    return render(request, 'common/feedback/feedback.html', context)
