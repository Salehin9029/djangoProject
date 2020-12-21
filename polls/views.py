from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, choices
# Create your views here.
from django.template import loader, RequestContext


def index(request):
    latest_questions = Question.objects.order_by('pub_date')[:5]  # five is to have the first five questions
    # output = ", ".join(q.question_text for q in latest_questions)
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_questions': latest_questions
    })
    return HttpResponse(template.render(context))


def detail(request, question_id):
    return HttpResponse("THE QUESTION IS %s" % question_id)


def results(request, question_id):
    return HttpResponse("The results %s" % question_id)


def vote(request, question_id):
    return HttpResponse("The Votes %s" % question_id)
