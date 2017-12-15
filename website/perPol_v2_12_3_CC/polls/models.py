# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    
    def __str__(self):
	return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Response(models.Model):
	session_id = models.CharField(max_length=100)
	q1_val = models.IntegerField(default=0)
	q2_val = models.IntegerField(default=0)
	q3_val = models.IntegerField(default=0)
	q4_val = models.IntegerField(default=0)
	q5_val = models.IntegerField(default=0)
	q6_val = models.IntegerField(default=0)
	q7_val = models.IntegerField(default=0)
	q8_val = models.IntegerField(default=0)
	q9_val = models.IntegerField(default=0)
	q10_val = models.IntegerField(default=0)
	q11_val = models.IntegerField(default=0)
	q12_val = models.IntegerField(default=0)
	q13_val = models.IntegerField(default=0)
	q14_val = models.IntegerField(default=0)
	q15_val = models.IntegerField(default=0)
	q16_val = models.IntegerField(default=0)
	q17_val = models.IntegerField(default=0)
	q18_val = models.IntegerField(default=0)
	q19_val = models.IntegerField(default=0)
	q20_val = models.IntegerField(default=0)

	def __str__(self):
		return self.session_id
