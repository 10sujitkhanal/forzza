from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.safestring import mark_safe
import json
from django.http import HttpResponse
from deposit.models import Deposit
import json
from django.contrib import messages
from notifications.models import Notification
from notifications.signals import notify
from accounts.models import User
from userprofile.models import Profile


def deposit(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('accounts:login'))

    histories = Deposit.objects.filter(user=request.user).order_by('-date')
    allAdmin = User.objects.filter(is_superuser = True)
    profiles = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        deposit = request.POST['deposit']
        username = request.POST['username']
        review = request.POST['review']
        photo = request.FILES['photo']

        for admin in allAdmin:
            notify.send(request.user, recipient=allAdmin, verb='deposit a balance',
                        level=Notification.LEVELS.success)
        add = Deposit.objects.create(deposit_amount=deposit, frozza_username = username, review=review, photo= photo, user=request.user )
        messages.warning(request, 'Deposit Successfull')

    context = {
        'histories':histories,
        'page_url' : '/deposit',
        'profiles' : profiles
    }
    
    return render(request, 'deposit/deposit.html', context)
