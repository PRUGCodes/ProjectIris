from django.db import models

# Create your models here.

class Submission(models.Model):
    submission_text = models.TextField(max_length=300)