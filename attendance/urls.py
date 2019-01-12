from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name="manager"),
	path('course_create/', views.courseCreate, name = 'course-create'),
]
