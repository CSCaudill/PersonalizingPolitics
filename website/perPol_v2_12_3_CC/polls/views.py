# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic,View

from .forms import SurveyForm
from .distance import candidate_distance, senator_distance

import pandas as pd

df_candidates = pd.DataFrame.from_csv("polls/model_data/candidate_fields.csv")
df_senators = pd.DataFrame.from_csv("polls/model_data/senator_2016_fields.csv")
df_heatmap = pd.DataFrame.from_csv("polls/model_data/heatmap.csv")

def index(request):
    return render(request, 'polls/index.html')

def explanation(request):
    return render(request, 'polls/explanation.html')

def questions(request):
    return render(request, 'polls/questions.html')

def AnalysisView(request):

    # Allow users to adjust their views and maintain their original
    form = SurveyForm(
        initial={
        'abortion_select':request.session['q1_val'],
        'hiring_select': request.session['q2_val'],
        'marriage_select': request.session['q3_val'],
        'god_select': request.session['q4_val'],
        'obamacare_select': request.session['q5_val'],
        'socialsec_select': request.session['q6_val'],
        'vouchers_select': request.session['q7_val'],
        'pollution_select': request.session['q8_val'],
        'punishment_select': request.session['q9_val'],
        'gun_select': request.session['q10_val'],
        'tax_select': request.session['q11_val'],
        'pathway_select': request.session['q12_val'],
        'trade_select': request.session['q13_val'],
        'exceptionalism_select': request.session['q14_val'],
        'military_select': request.session['q15_val'],
        'registration_select': request.session['q16_val'],
        'foreign_select': request.session['q17_val'],
        'green_select': request.session['q18_val'],
        'marijuana_select': request.session['q19_val'],
        'stimulus_select': request.session['q20_val'],
        'state_select': request.session['user_state']
        })


    d = {
    '1':float(request.session['q1_val']),
    '2':float(request.session['q2_val']),
    '3':float(request.session['q3_val']),
    '4':float(request.session['q4_val']),
    '5':float(request.session['q5_val']),
    '6':float(request.session['q6_val']),
    '7':float(request.session['q7_val']),
    '8':float(request.session['q8_val']),
    '9':float(request.session['q9_val']),
    '10':float(request.session['q10_val']),
    '11':float(request.session['q11_val']),
    '12':float(request.session['q12_val']),
    '13':float(request.session['q13_val']),
    '14':float(request.session['q14_val']),
    '15':float(request.session['q15_val']),
    '16':float(request.session['q16_val']),
    '17':float(request.session['q17_val']),
    '18':float(request.session['q18_val']),
    '19':float(request.session['q19_val']),
    '20':float(request.session['q20_val'])
    }

    user_df = pd.DataFrame.from_records([d])

    user_state = request.session['user_state']

    can_dist = candidate_distance(df_candidates, user_df)
    sen_dist = senator_distance(df_senators, user_df)
    can_json = can_dist.to_json(orient='records')
    sen_json = sen_dist.to_json(orient='records')

    # Modeling data to compare views between user and candidate to visualize in heat map
    df = df_heatmap.copy()
    df_diff = df.copy()
    for c_name in set(df['candidate']):
        df_diff.loc[(df_diff['topic']==1) & (df_diff['candidate']==c_name),'value'] = abs((float(d['1']) + df.loc[(df['topic']==1) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==2) & (df_diff['candidate']==c_name),'value'] = abs((float(d['2']) + df.loc[(df['topic']==2) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==3) & (df_diff['candidate']==c_name),'value'] = abs((float(d['3']) + df.loc[(df['topic']==3) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==4) & (df_diff['candidate']==c_name),'value'] = abs((float(d['4']) + df.loc[(df['topic']==4) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==5) & (df_diff['candidate']==c_name),'value'] = abs((float(d['5']) + df.loc[(df['topic']==5) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==6) & (df_diff['candidate']==c_name),'value'] = abs((float(d['6']) + df.loc[(df['topic']==6) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==7) & (df_diff['candidate']==c_name),'value'] = abs((float(d['7']) + df.loc[(df['topic']==7) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==8) & (df_diff['candidate']==c_name),'value'] = abs((float(d['8']) + df.loc[(df['topic']==8) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==9) & (df_diff['candidate']==c_name),'value'] = abs((float(d['9']) + df.loc[(df['topic']==9) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==10) & (df_diff['candidate']==c_name),'value'] = abs((float(d['10']) + df.loc[(df['topic']==10) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==11) & (df_diff['candidate']==c_name),'value'] = abs((float(d['11']) + df.loc[(df['topic']==11) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==12) & (df_diff['candidate']==c_name),'value'] = abs((float(d['12']) + df.loc[(df['topic']==12) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==13) & (df_diff['candidate']==c_name),'value'] = abs((float(d['13']) + df.loc[(df['topic']==13) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==14) & (df_diff['candidate']==c_name),'value'] = abs((float(d['14']) + df.loc[(df['topic']==14) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==15) & (df_diff['candidate']==c_name),'value'] = abs((float(d['15']) + df.loc[(df['topic']==15) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==16) & (df_diff['candidate']==c_name),'value'] = abs((float(d['16']) + df.loc[(df['topic']==16) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==17) & (df_diff['candidate']==c_name),'value'] = abs((float(d['17']) + df.loc[(df['topic']==17) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==18) & (df_diff['candidate']==c_name),'value'] = abs((float(d['18']) + df.loc[(df['topic']==18) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==19) & (df_diff['candidate']==c_name),'value'] = abs((float(d['19']) + df.loc[(df['topic']==19) & (df['candidate']==c_name),'value']))
        df_diff.loc[(df_diff['topic']==20) & (df_diff['candidate']==c_name),'value'] = abs((float(d['20']) + df.loc[(df['topic']==20) & (df['candidate']==c_name),'value']))

    can_views_diff = df_diff.to_json(orient='records')
    can_views = df_heatmap.to_json(orient='records')

    analysis_data = {
        'can_data': can_dist, 
        'sen_data': sen_dist, 
        'can_json': can_json, 
        'sen_json': sen_json, 
        'user_state': user_state, 
        'form': form, 
        'can_views': can_views,
        'can_views_diff': can_views_diff }

    return render(request, 'polls/analysis.html', analysis_data)

def vote(request):
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
        request.session['user_state'] = request.POST['state_select']

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:analysis'))


def SurveyView(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        # state_form = StateForm(request.POST)
        # if form.is_valid():
        #     state_select = form.cleaned_data['state_select']
        #     abortion_select = form.cleaned_data['abortion_select']
        # #     hiring_select = form.cleaned_data['hiring_select']
        # #     marriage_select = form.cleaned_data['marriage_select']
        #     return HttpResponseRedirect('/analysis/')
    else:
        form = SurveyForm()
    return render(request, 'polls/survey.html/', {'form': form})

