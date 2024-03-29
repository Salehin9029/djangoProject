from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, choices
# Create your views here.



def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]  # five is to have the first five questions
    # output = ", ".join(q.question_text for q in latest_questions)
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_questions': latest_questions
    # })
    # return HttpResponse(output)
    context = {'latest_questions':latest_questions}
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context))


def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    # return HttpResponse("THE QUESTION IS %s" % question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
    # return HttpResponse("The results %s" % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choices_set.get(pk = request.POST['choices'])
    except:
        return render(request, 'polls/detail.html', {'question':question, 'error_message':"Please select a choice"})
    else:
        selected_choice.votes +=1
        selected_choice.save()
    # return HttpResponse("The Votes %s" % question_id)
    return HttpResponseRedirect(reverse('results', args=(question.id)))