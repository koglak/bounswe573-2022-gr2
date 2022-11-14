from django.contrib import admin
from .models import Question, QuestionList, Score, Case, CaseResult, CaseRating, Comment, ReplyComment


# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionList)
admin.site.register(Score)
admin.site.register(Case)
admin.site.register(CaseResult)
admin.site.register(CaseRating)
admin.site.register(Comment)
admin.site.register(ReplyComment)


