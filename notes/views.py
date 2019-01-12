from django.shortcuts import render, redirect
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .models import *

# Create your views here.

#create class based views
# looks for app/model_viewtype.html

class NoteListView(LoginRequiredMixin, ListView):
	model = Note
	login_url = '/login/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['css'] = 'notes/noteStyles.css'
		context['highlight'] = 'notes'
		return context


class NoteDetailView(LoginRequiredMixin, DetailView):
	model = Note
	login_url = '/login/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['css'] = 'notes/noteStyles.css'
		context['highlight'] = 'notes'
		return context

class NoteCreateView(LoginRequiredMixin, CreateView):
	model = Note
	fields = ['title', 'content', 'tag']
	login_url = '/login/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['css'] = 'notes/noteStyles.css'
		context['highlight'] = 'notes'
		context['isCreate'] = True
		return context

class NoteUpdateView(LoginRequiredMixin, UpdateView):
	model = Note
	fields = ['title', 'content', 'tag']
	login_url = "/login/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['css'] = 'notes/noteStyles.css'
		context['highlight'] = 'notes'
		context['isCreate'] = False
		return context

@login_required(login_url="/login/")
def NoteDeleteView(request, pk):
	Note.objects.get(pk = pk).delete()
	messages.info(request, 'Your note was successfully deleted')
	return redirect('notes-home')