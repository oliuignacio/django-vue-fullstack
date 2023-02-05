from django.db import models

# Create your models here.
class Task (models.Model):
  #title
  title = models.CharField(max_length=100)
  #description
  description = models.TextField(blank=True, null=True)
  #status
  completed = models.BooleanField(default=False)
  #created_at
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    #return the task title
    return self.title
    