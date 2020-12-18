from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.safestring import mark_safe
import json
from django.http import HttpResponse, HttpResponseRedirect
from .models import Catagories, Partner, Feedback
from django.utils.translation import ugettext_lazy as _

def home(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('accounts:login'))
    
    catagories = Catagories.objects.all()
    partners = Partner.objects.all()
    context = {
        'catagories':catagories,
        'partners': partners,
        'page_url' : '/'
    }
    return render(request, 'home.html', context)


def change_language(request):
    url = '/ru'
    path = request.POST.get('path')
    lang = request.POST.get('language')
    print(lang)
    print(path)

    if lang == 'en-us':
        url = path

    if lang == 'ne':
        url = '/'+ lang + path

    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = url
            elif language == settings.LANGUAGE_CODE:
                redirect_path = url
            else:
                return response
            from django.utils import translation
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response


def feedback(request):
    print("sujit")
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        question = request.POST.get('question')

        Feedback.objects.create(fullname = fullname, email=email, question=question)

    return redirect("/")