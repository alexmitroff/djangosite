from django.db import models

# Create your models here.

class ContentType(models.Model):
	pos = models.PositiveIntegerField(
		"position", default=0)
	show = models.BooleanField()
	name = models.CharField(
		max_length=32)
	description = models.TextField(
		blank=True, null=True)
	created = models.DateField(
		auto_now_add=True)
	modified = models.DateField(
		auto_now=True)
	
	class Meta:
		ordering = ["pos", "name"]
		verbose_name = "Content type"
		verbose_name_plural = "Content types"
	
	def __str__(self):
		return self.name
