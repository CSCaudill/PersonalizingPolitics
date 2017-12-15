# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic,View

from .models import Choice, Question, Response
from .forms import SurveyForm
from .distance import candidate_distance

import pandas as pd

df_candidates = pd.DataFrame.from_csv("polls/model_data/candidate_fields.csv")

# from django.contrib.sessions.backends.db import SessionStore
# from importlib import import_module
# from django.conf import settings
# SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

def index(request):
    return render(request, 'polls/index.html')

# class AnalysisView(generic.ListView):
#     template_name = 'polls/analysis.html'
#     context_object_name = 'question_list'

#     def get_queryset(self):
#         return Question.objects.all

def AnalysisView(request):
    d = {
    '1':int(request.session['q1_val']),
    '2':int(request.session['q2_val']),
    '3':int(request.session['q3_val']),
    '4':int(request.session['q4_val']),
    '5':int(request.session['q5_val']),
    '6':int(request.session['q6_val']),
    '7':int(request.session['q7_val']),
    '8':int(request.session['q8_val']),
    '9':int(request.session['q9_val']),
    '10':int(request.session['q10_val']),
    '11':int(request.session['q11_val']),
    '12':int(request.session['q12_val']),
    '13':int(request.session['q13_val']),
    '14':int(request.session['q14_val']),
    '15':int(request.session['q15_val']),
    '16':int(request.session['q16_val']),
    '17':int(request.session['q17_val']),
    '18':int(request.session['q18_val']),
    '19':int(request.session['q19_val']),
    '20':int(request.session['q20_val'])
    }
    user_df = pd.DataFrame.from_records([d])

    json = candidate_distance(df_candidates, user_df).to_json(orient='records')

    columns = [
    {'field': "candidate", 'title': "candidate"},
    {'field': "distance", 'title': "distance"},
    {'field': "state", 'title': "state"},
    {'field': "year", 'title': "year"},
    ]

    context = {
             'data': json,
             'columns': columns
            }

    return render(request, 'polls/analysis.html', context)

    # def get_queryset(self):
    #     return Response.objects.get(session_id=request.session)


def vote(request):
    # try:

    #     abortion_q = Question.objects.get(pk=1)
    #     hiring_q = Question.objects.get(pk=2)
    #     marriage_q = Question.objects.get(pk=3)
    #     god_q = Question.objects.get(pk=4)
    #     obamacare_q = Question.objects.get(pk=5)
    #     socialsec_q = Question.objects.get(pk=6)
    #     vouchers_q = Question.objects.get(pk=7)
    #     pollution_q = Question.objects.get(pk=8)
    #     punishment_q = Question.objects.get(pk=9)
    #     gun_q = Question.objects.get(pk=10)
    #     tax_q = Question.objects.get(pk=11)
    #     pathway_q = Question.objects.get(pk=12)
    #     trade_q = Question.objects.get(pk=13)
    #     exceptionalism_q = Question.objects.get(pk=14)
    #     military_q = Question.objects.get(pk=15)
    #     registration_q = Question.objects.get(pk=16)
    #     foreign_q = Question.objects.get(pk=17)
    #     green_q = Question.objects.get(pk=18)
    #     marijuana_q = Question.objects.get(pk=19)
    #     stimulus_q = Question.objects.get(pk=20)


        # abortion_selected_choice = abortion_q.choice_set.get(pk=request.POST['abortion_select'])
        # hiring_selected_choice = hiring_q.choice_set.get(pk=request.POST['hiring_select'])
        # marriage_selected_choice = marriage_q.choice_set.get(pk=request.POST['marriage_select'])
        # god_selected_choice = god_q.choice_set.get(pk=request.POST['god_select'])
        # obamacare_selected_choice = obamacare_q.choice_set.get(pk=request.POST['obamacare_select'])
        # socialsec_selected_choice = socialsec_q.choice_set.get(pk=request.POST['socialsec_select'])
        # vouchers_selected_choice = vouchers_q.choice_set.get(pk=request.POST['vouchers_select'])
        # pollution_selected_choice = pollution_q.choice_set.get(pk=request.POST['pollution_select'])
        # punishment_selected_choice = punishment_q.choice_set.get(pk=request.POST['punishment_select'])
        # gun_selected_choice = gun_q.choice_set.get(pk=request.POST['gun_select'])
        # tax_selected_choice = tax_q.choice_set.get(pk=request.POST['tax_select'])
        # pathway_selected_choice = pathway_q.choice_set.get(pk=request.POST['pathway_select'])
        # trade_selected_choice = trade_q.choice_set.get(pk=request.POST['trade_select'])
        # exceptionalism_selected_choice = exceptionalism_q.choice_set.get(pk=request.POST['exceptionalism_select'])
        # military_selected_choice = military_q.choice_set.get(pk=request.POST['military_select'])
        # registration_selected_choice = registration_q.choice_set.get(pk=request.POST['registration_select'])
        # foreign_selected_choice = foreign_q.choice_set.get(pk=request.POST['foreign_select'])
        # green_selected_choice = green_q.choice_set.get(pk=request.POST['green_select'])
        # marijuana_selected_choice = marijuana_q.choice_set.get(pk=request.POST['marijuana_select'])
        # stimulus_selected_choice = stimulus_q.choice_set.get(pk=request.POST['stimulus_select'])
        
    

    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the questionsion voting form.
    #     return render(request, 'polls/survey.html', {
    #         # 'question': question, 
    #         'error_message': "You didn't select a choice.",
    #     })


    # else:
        # abortion_selected_choice.votes += 1
        # hiring_selected_choice.votes += 1
        # marriage_selected_choice.votes += 1
        # god_selected_choice.votes += 1
        # obamacare_selected_choice.votes += 1
        # socialsec_selected_choice.votes += 1
        # vouchers_selected_choice.votes += 1
        # pollution_selected_choice.votes += 1
        # punishment_selected_choice.votes += 1
        # gun_selected_choice.votes += 1
        # tax_selected_choice.votes += 1
        # pathway_selected_choice.votes += 1
        # trade_selected_choice.votes += 1
        # exceptionalism_selected_choice.votes += 1
        # military_selected_choice.votes += 1
        # registration_selected_choice.votes += 1
        # foreign_selected_choice.votes += 1
        # green_selected_choice.votes += 1
        # marijuana_selected_choice.votes += 1
        # stimulus_selected_choice.votes += 1

        # abortion_selected_choice.save()
        # hiring_selected_choice.save()
        # marriage_selected_choice.save()
        # god_selected_choice.save()
        # obamacare_selected_choice.save()
        # socialsec_selected_choice.save()
        # vouchers_selected_choice.save()
        # pollution_selected_choice.save()
        # punishment_selected_choice.save()
        # gun_selected_choice.save()
        # tax_selected_choice.save()
        # pathway_selected_choice.save()
        # trade_selected_choice.save()
        # exceptionalism_selected_choice.save()
        # military_selected_choice.save()
        # registration_selected_choice.save()
        # foreign_selected_choice.save()
        # green_selected_choice.save()
        # marijuana_selected_choice.save()
        # stimulus_selected_choice.save()

        # s = SessionStore()
        # s.create()

        # request.session['value'] = 'hi'
        # r = Response(session_id=s.session_key)
        request.session['q1_val'] = request.POST['abortion_select']
        request.session['q2_val'] = request.POST['hiring_select']
        request.session['q3_val'] = request.POST['marriage_select']
        request.session['q4_val'] = request.POST['god_select']
        request.session['q5_val'] = request.POST['obamacare_select']
        request.session['q6_val'] = request.POST['socialsec_select']
        request.session['q7_val'] = request.POST['vouchers_select']
        request.session['q8_val'] = request.POST['pollution_select']
        request.session['q9_val'] = request.POST['punishment_select']
        request.session['q10_val'] = request.POST['gun_select']
        request.session['q11_val'] = request.POST['tax_select']
        request.session['q12_val'] = request.POST['pathway_select']
        request.session['q13_val'] = request.POST['trade_select']
        request.session['q14_val'] = request.POST['exceptionalism_select']
        request.session['q15_val'] = request.POST['military_select']
        request.session['q16_val'] = request.POST['registration_select']
        request.session['q17_val'] = request.POST['foreign_select']
        request.session['q18_val'] = request.POST['green_select']
        request.session['q19_val'] = request.POST['marijuana_select']
        request.session['q20_val'] = request.POST['stimulus_select']


        # r.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:test'))


def SurveyView(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        # if form.is_valid():
        #     abortion_select = form.cleaned_data['abortion_select']
        #     hiring_select = form.cleaned_data['hiring_select']
        #     marriage_select = form.cleaned_data['marriage_select']
        #     return HttpResponseRedirect('/analysis/')
    else:
        form = SurveyForm()
    return render(request, 'polls/survey.html/', {'form': form})

