from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import re
from django.db.models import Q
from django.contrib import messages
from .models import *
# Create your views here.
def home(request):
	context = {}
	if request.user.is_authenticated:
		context['courses'] = request.user.course_set.all()
	return render(request, 'attendance/manager.html', context)

def courseCreate(request):
	context = {}
	people = User.objects.all()
	context['tas'] = people.filter(profile__employment = 'TA')
	context['profs'] = people.filter(profile__employment = 'PR')

	if request.method == 'POST':
		ppl = prepareData(request.POST['tas'], request.POST['students'], request.POST['profs'])
		course = Course(name = request.POST['name'], code = request.POST['code'])
		course.save()
		for person in ppl:
			course.people.add(person)
		messages.success(request, f'{course} created successfully')
		return redirect('manager')
	return render(request, 'attendance/course_create.html', context)
















def prepareData(tas, students, profs):
	tas = list(map(int,tas))
	profs = list(map(int,profs))
	stud_list = re.sub('[\s+]', '', students).split(',')
	students = []
	for thing in stud_list:
		if '-' in thing:
			students+=makeRange(thing)
		else:
			students.append(thing)
	print(students)
	people = User.objects.filter(Q(id__in = tas+profs) | Q(profile__rollno__in = students))
	return people

def makeRange(s):
	start, finish = s.split('-')
	s =  list(range(int(start), int(finish)+1))
	s = list(map(str, s))
	return s