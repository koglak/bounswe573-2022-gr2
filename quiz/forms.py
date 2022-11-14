from django.forms import ModelForm
from .models import *
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={ 
               'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Text',
                })
            }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = ReplyComment
        fields = ('body',)
        labels = {
        'body': (''),
         }

 
class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields="__all__"

class QuizForm(ModelForm):

    #question_quantity = forms.IntegerField(widget=forms.NumberInput, max_value=10)

    class Meta:
        model=QuestionList
        fields=('title', )


class CaseForm(ModelForm):
    
    class Meta:
        model=Case
        fields=('title','description', 'due_date')



class CaseResultForm(ModelForm):

    class Meta:
        model=CaseResult
        fields=('upload',)

    def clean_file(self):
        file= self.cleaned_data['file']

        try:
            #validate content type
            main, sub = file.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'png']):
                raise forms.ValidationError(u'Please use a JPEG or PNG image.')

            #validate file size
            if len(file) > (10000 * 1024):
                raise forms.ValidationError(u'File size may not exceed 10M.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return file

class ScoreForm(ModelForm):
    class Meta:
        model=CaseResult
        fields=('score',)