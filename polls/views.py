from django.shortcuts import HttpResponse, render, get_object_or_404

from .models import Question

def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'questions': questions,
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("Você está vendo os resultados da questão %s" % question_id)

def vote(request, question_id): 
    return HttpResponse("Você está votando na questão %s." % question_id)
