from django.urls import include, path
from .views import *

urlpatterns = [
    path('', NoteListView.as_view(), name='notes-home'),
    path('detail/<int:pk>', NoteDetailView.as_view(), name='notes-detail'),
    path('new', NoteCreateView.as_view(), name='notes-create'),
    path('update/<int:pk>', NoteUpdateView.as_view(), name='notes-update'),
    path('delete/<int:pk>', NoteDeleteView, name='notes-delete'),
]