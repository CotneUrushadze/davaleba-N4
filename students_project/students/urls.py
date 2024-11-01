from django.urls import path
from students.views import main_page_view, students_page_view

urlpatterns = [
    path('', main_page_view),
    path('students/', students_page_view)
]