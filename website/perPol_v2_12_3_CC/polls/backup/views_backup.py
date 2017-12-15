# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic,View

from .models import Choice, Question
from .forms import SurveyForm

def index(request):
    return render(request, 'polls/index.html')

class SurveyView(generic.ListView):
    template_name = 'polls/survey.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.all

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the questionsion voting form.
        return render(request, 'polls/survey.html', {
            # 'question': question, 
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:analysis'))


class AnalysisView(generic.ListView):
    template_name = 'polls/analysis.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all
    # model = Question
    # template_name = 'polls/analysis.html'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.all


def question_choice_view(request):
    if request.method == "POST":
        question_choice_data = request.POST['data']
        print question_choice_data 
        # question = get_object_or_404(Question.objects, question_text = question_choice_data )
        return HttpResponse(question_choice_data)
        # html = ("<H1>%s</H1>", question_choice_data)
    # template_name = 'polls/question_choice_view.html'
    # context_object_name = 'question_choice'

    # def get_queryset(self):
    #     return render(request, 'polls/question_choice_view.html')

def vote2(request):
    try:

        abortion_question = Question.objects.get(pk=1)
        hiring_question = Question.objects.get(pk=2)
        marriage_question = Question.objects.get(pk=3)

        abortion_selected_choice = abortion_question.choice_set.get(pk=request.POST['abortion_select'])
        hiring_selected_choice = hiring_question.choice_set.get(pk=request.POST['hiring_select'])
        marriage_selected_choice = marriage_question.choice_set.get(pk=request.POST['marriage_select'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the questionsion voting form.
        return render(request, 'polls/survey_form.html', {
            # 'question': question, 
            'error_message': "You didn't select a choice.",
        })
    else:
        abortion_selected_choice.votes += 1
        hiring_selected_choice.votes += 1
        marriage_selected_choice.votes += 1
        abortion_selected_choice.save()
        hiring_selected_choice.save()
        marriage_selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:analysis'))


def radio_form(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            abortion_select = form.cleaned_data['abortion_select']
            hiring_select = form.cleaned_data['hiring_select']
            marriage_select = form.cleaned_data['marriage_select']
            return HttpResponseRedirect('/analysis/')
    else:
        form = SurveyForm()
    return render(request, 'polls/survey_form.html/', {'form': form})

