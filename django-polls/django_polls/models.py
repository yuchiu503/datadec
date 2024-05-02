from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin


# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("data published")

    def __str__(self) -> str:
        return self.question_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        # return slef.pub_date >= timezone.now() - datetime.timedelta(days=1) #这个存在bug

        #修改bug后：
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0, help_text="请选择")

    def __str__(self) -> str:
        return self.choice_text
