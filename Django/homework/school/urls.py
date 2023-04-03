from django.urls import path
from school.views import students_list, student_detail, classes_list, school_detail

urlpatterns = [
    path('students', students_list),
    path('student/<int:pk>/', student_detail),
    path('classes', classes_list),
    path('school/<int:pk>/', school_detail)
]