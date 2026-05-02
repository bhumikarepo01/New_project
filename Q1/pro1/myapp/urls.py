from django.urls import path
from . import views

urlpatterns = [
    path('',views.course_list,name='course_list'),
    path('add/',views.add_course,name='add_course'),
    path('enroll/<int:course_id>/',views.enroll_student,name='enroll_student'),
    path('student/<int:student_id>/',views.student_courses,name='student_courses'),
]
