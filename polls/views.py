from django.shortcuts import HttpResponse
from django.shortcuts import render

from .models import Question

def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'questions': questions,
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("Você está vendo a questão %s." % question_id)

def results(request, question_id):
    return HttpResponse("Você está vendo os resultados da questão %s" % question_id)

def vote(request, question_id): 
    return HttpResponse("Você está votando na questão %s." % question_id)
