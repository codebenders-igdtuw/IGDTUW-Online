from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
from django.http import HttpResponseRedirect

# Create your views here

def home(request):
    return render(request, 'layout/index.html', )
