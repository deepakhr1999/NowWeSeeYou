from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Note(models.Model):
	title = models.CharField(max_length = 200, default='')
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	TAG_CHOICES=[
		('primary', 'Blue'),
		('secondary', 'Grey'),
		('success', "Green"),
		('danger', 'Red'),
		('warning', 'Yellow'), 
		('info', 'Light-Blue'),
		('light', 'White'),
		('dark' , 'Dark-Grey'),
	]
	tag = models.CharField(max_length=10, choices = TAG_CHOICES, default='info')

	def __str__(self):
		return self.title

	@property
	def snippet(self):
		lim = 200
		if self.content.count('\n')>6:
			snip = '\n'.join(self.content.split('\n')[:6])
			if len(snip)<lim:
				return snip
			else:
				return snip[:lim] + '...'
		elif len(self.content)<lim:
			return self.content
		else:
			return self.content[:lim]+'...'

	def get_absolute_url(self):
		return reverse('notes-detail', kwargs={'pk':self.pk})


	class Meta:
		ordering = ['date_posted',]
