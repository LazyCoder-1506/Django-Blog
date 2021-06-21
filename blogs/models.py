from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=120)
  body = models.TextField()
  author = models.CharField(max_length=50)
  pub_date = models.DateField()

  def __str__(self):
    return self.title