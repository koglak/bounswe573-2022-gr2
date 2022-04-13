
# Create your views here.
from django.utils import timezone
from django.shortcuts import render
from .models import Course, Profile, Rating, Lecture
from .forms import CourseForm
from django.shortcuts import redirect, get_object_or_404
from taggit.models import Tag
from django.template.defaultfilters import slugify

# Create your views here.

def user_profile(response):
    courses=Course.objects.filter(user = response.user).order_by('published_date')
    user_profile=Profile.objects.get(user=response.user)

    return render(response, "userprofile/profile.html", {'courses':courses, 'user_profile':user_profile})

def course_detail(request, title):
    course = get_object_or_404(Course, title=title)
    return render(request, 'userprofile/course_detail.html', {'course':course})

def course_edit(request, title):
    course = get_object_or_404(Course, title=title)
     
    if request.method == "POST":
        form = CourseForm(request.POST or None, request.FILES or None, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.published_date = timezone.now()
            course.save()
            form.save_m2m()
            return redirect('course_detail', title=course.title)
    else:
        form = CourseForm(instance=course)
    return render(request, 'userprofile/course_edit.html', {'form': form, 'title': title})

def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.published_date = timezone.now()
            course.save()
            form.save_m2m()

            return redirect('course_detail', title=course.title)
    else:
        form = CourseForm()
        title ="none"
    return render(request, 'userprofile/course_edit.html', {'form': form, 'title':title})


def course_tag_detail(response,tag):
    courses = Course.objects.filter(tags__name__in=[tag])
    return render(response, "userprofile/course_tag_details.html", {'courses': courses, 'tag': tag})


def delete_course(request, title):
    course = Course.objects.get(title=title)
    course.delete()
    return redirect('/myspace/profile')


def course_rate(request, title):
    course = get_object_or_404(Course, title=title)
    rating=request.POST["rating"]
    if course.rating_set.filter(user=request.user, rating=rating ):
        print('already rated')
    elif course.rating_set.filter(user=request.user):
        obj= Rating.objects.get(user=request.user, course=course)
        obj.rating = rating
        obj.save()
        course.averagereview()

    else:
        obj = Rating.objects.create(course=course, user=request.user, rating=rating)
        obj.save()
        course.averagereview()

    return redirect('course_detail', title=course.title)


def other_user_profile(response, name):
    courses=Course.objects.filter(user__username=name).order_by('published_date')
    user_profile=Profile.objects.filter(user__username=name)

    return render(response, "userprofile/profile.html", {'courses': courses, 'user_profile': user_profile})

def lecture_detail(response, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    course = Course.objects.filter(lecture__title=lecture.title)

    return render(response, "userprofile/lecture_detail.html",{'course': course, 'lecture':lecture})