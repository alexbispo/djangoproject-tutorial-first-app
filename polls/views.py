from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return  render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'É necessário selecionar uma resposta',
        })
    else:
        # Usando a função F para eviar potencial race condition 
        # Por exemplo, mais de uma thread manipulando simultaneamente o campo votes.
        selected_choice.votes = F('votes') + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
