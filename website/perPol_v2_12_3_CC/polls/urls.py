from django.conf.urls import url


from . import views



app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vote/$', views.vote, name='vote'),
    url(r'^analysis/$', views.AnalysisView, name='analysis'),
    url(r'^survey/$', views.SurveyView, name='survey'),
    url(r'^explanation/$', views.explanation, name='explanation'),
    url(r'^questions/$', views.questions, name='questions'),

]