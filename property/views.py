from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.shortcuts import render

# Create your views here.

def search(request):
    template=loader.get_template('search.html')
    context = RequestContext(request, {}) #'latest_question_list': latest_question_list,
    return HttpResponse(template.render(context))

