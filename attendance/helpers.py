from django.contrib.auth.models import User
from django.db.models import Q
import re
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