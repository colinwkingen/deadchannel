# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from django.http import Http404

from .models import User, Profile
from builtins import str


def index(request):
    return HttpResponse("Ping!")

def score(request, score):
    return HttpResponse("Here's the score: %s." % score)

def nickname(request, nickname):
    response = "User's nickname: %s."
    return HttpResponse(response % nickname)

def index(request):
    try:
        all_user_list = User.objects.order_by('-dateAdded')[:5]
    except User.DoesNotExist():
        raise Http404("User Does not Exist.")
    template = loader.get_template('pages/index.html')
    
    context = {
        'all_user_list': all_user_list,
    }    
    return HttpResponse(template.render(context,request))
      
def profile(request, user):
    stringUser = str(user)
    profile = get_object_or_404(Profile, pk=stringUser)
    return render(request, 'pages/profile.html', {'stringUser': profile})