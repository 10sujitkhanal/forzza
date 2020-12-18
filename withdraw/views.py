from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.safestring import mark_safe
import json
from django.http import HttpResponse
from withdraw.models import Withdraw
from accounts.models import User
from django.contrib import messages
from notifications.models import Notification
from notifications.signals import notify
from userprofile.models import Profile



def withdraw(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('accounts:login'))

    histories = Withdraw.objects.filter(user=request.user)

    allAdmin = User.objects.filter(is_superuser = True)
    profiles = Profile.objects.get(user = request.user)

    if request.method == 'POST':
        withdraw = request.POST['withdraw']
        username = request.POST['username']
        review = request.POST['review']
        for admin in allAdmin:
            notify.send(request.user, recipient=allAdmin, verb='withdraw a balance',
                        level=Notification.LEVELS.success)

        Withdraw.objects.create(withdraw_amount=withdraw, frozza_username = username, review=review, user=request.user )
        messages.warning(request, 'Withdraw Successfull')
    
    context = {
        'histories': histories,
        'page_url' : '/withdraw',
        'profiles' : profiles
    }
    
    return render(request, 'withdraw/withdraw.html', context)
