from django import forms
from django.db import models
from django.conf import settings
from userprofile.models import Course
from django.template.defaulttags import register


OPTION_CHOICES = (
    ('option1','option1'),
    ('option2', 'option2'),
    ('option3','option3'),
    ('option4','option4'),
)

 
# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200, choices=OPTION_CHOICES, default='option1')
    
    def __str__(self):
        return self.question





class QuestionList(models.Model):
    title=models.CharField(max_length=200,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, default=None, on_delete=models.CASCADE)
    question_list = models.ManyToManyField(Question, blank=True, related_name='question_list')


    def __str__(self):
        return f'{self.title} {self.course.title}'


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.CharField(max_length=200,null=True)
    quiz =models.ForeignKey(QuestionList, default=None, on_delete=models.CASCADE)

    @register.filter
    def get_all_scores(self,quiz):
        return self.filter(quiz=quiz).last()

    def __str__(self):
        return self.score
