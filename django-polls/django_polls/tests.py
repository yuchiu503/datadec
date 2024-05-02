
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() 这个函数（或方法）对于 pub_date（发布日期）在未来的问题返回 False
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() 函数会返回一个布尔值（False），如果问题的 pub_date（发布日期）超过（早于）1天的话。
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() 是一个函数（或方法），当某个问题的 pub_date（发布日期）是在过去的一天内时，它返回 True。
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


    