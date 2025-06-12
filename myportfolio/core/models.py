from django.db import models

# Create your models here.

class TechSkill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.percentage}%"
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_images/')
    live_demo_url = models.URLField(blank=True, null=True)
    source_code_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
