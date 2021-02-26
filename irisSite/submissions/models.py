from django.db import models

# Create your models here.

class Submission(models.Model):
    submission_text = models.TextField(max_length=300)
    reported = models.BooleanField(default=False)