from django.db import models
from django.utils import timezone

# Create your models here.


class Blog(models.Model):

	class Meta:
	#для упорядочивания списка постов по дате публикации
		ordering = ['-date']

	title = models.CharField(max_length=100, unique=True)
	text = models.TextField()
	date = models.DateTimeField('date published', null=True, blank = True)
	cover = models.ImageField(upload_to = 'covers/', null = True, blank = True)