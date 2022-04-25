from django.shortcuts import render

from quiz.models import Case, Question, QuestionList, Score
from userprofile.models import Course
from .forms import CaseForm, QuestionForm, QuizForm, CaseResultForm
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone


# Create your views here.
def quiz_detail(request,title):
    if request.method == 'POST':
        print(request.POST)
        quiz = get_object_or_404(QuestionList, title=title)
        questions=quiz.question_list.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        user_score=Score.objects.create(user=request.user, quiz=quiz, score=percent)
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'quiz/quiz_result.html',context)
    else:
        quiz = QuestionList.objects.get(title=title)
        questions=quiz.question_list.all()
        course= Course.objects.get(questionlist__pk=quiz.pk)
        
        context = {
            'quiz': quiz,
            'questions':questions,
            'course':course
        }
        return render(request,'quiz/quiz_detail.html',context)

#def quiz_detail(response,title):
 #   quiz = get_object_or_404(QuestionList, title=title)
  #  return render(response, "quiz/quiz_detail.html", {'quiz': quiz})

def quiz_create(request, title):
    course=Course.objects.get(title=title)    
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.user = request.user
            quiz.course = course
            quiz.save()
            return redirect('quiz_detail', title=quiz.title)
    else:
        form = QuizForm()
        return render(request, 'quiz/quiz_create.html', {'form': form, 'title': title})

def question_add(request,title):    
    form=QuestionForm()
    quiz = QuestionList.objects.get(title=title)
        
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            question=form.save(commit=False)
            question.save()
            quiz.question_list.add(question.pk)
            quiz.save()

            return redirect('quiz_detail', title=title)

    context={'form':form}
    return render(request,'quiz/question_add.html',context)
   

def quiz_delete(request, title):
    quiz = QuestionList.objects.get(title=title)
    course= Course.objects.get(questionlist__pk=quiz.pk)

    quiz.delete()
    return redirect('course_detail', title=course.title)

def case_create(request,title):
    course=Course.objects.get(title=title)
    form = CaseForm()
    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.user = request.user
            case.course = course
            case.save()
            return redirect('case_detail', title=case.title)
    return render(request, 'quiz/case_create.html', {'course': course, 'form':form})

def case_detail(request,title):
    case=Case.objects.get(title=title)
    course=Course.objects.get(case=case)

    form= CaseResultForm()

    if request.method == 'POST':  
        form = CaseResultForm(request.POST, request.FILES)  
        if form.is_valid():  
            result = form.save(commit=False)
            result.user=request.user
            result.shared_date = timezone.now()
            result.case=case
            result.save()
            return redirect('course_detail', title=course.title)  
    else:  
        form= CaseResultForm()
        return render(request, 'quiz/case_detail.html', {'case':case, 'form': form, 'course': course})