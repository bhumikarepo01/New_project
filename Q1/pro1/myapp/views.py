from django.shortcuts import render,redirect
from .models import Course,Student
from .forms import StudentForm,CourseForm

# Create your views here.

def add_course(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request,'student_form.html',{'form':form})

def course_list(request):
    courses = Course.objects.all()
    return render(request,'course_list.html',{'courses':courses})

def enroll_student(request,course_id):
    course = Course.objects.get(id=course_id)
    form = StudentForm(request.POST or None)

    if form.is_valid():
        student=form.save()
        student.courses.add(course)
        return redirect('student_courses',student.id)
    
    return render(request,'student_form.html',{'form':form})

def student_courses(request,student_id):
    student = Student.objects.get(id=student_id)
    return render(request,'student_courses.html',{'student':student})

