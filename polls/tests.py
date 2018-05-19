import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionModelTests(TestCase):

	def test_was_published_recently(self):
		"""
		was_published_recently() deve retornar False para questões que tenham
		no atributo pub_date uma data no futuro.
		"""

		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		"""
		was_published_recently() deve retornar False para Questões que foram
		publicadas a mais de 1 dia atrás.
		"""

		old_time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date=old_time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""
		was_published_recently() deve retornar True para Questões que foram
		publicadas até 1 dia atrás.
		""" 

		recent_time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=recent_time)
		self.assertIs(recent_question.was_published_recently(), True)

