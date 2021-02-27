from django.db import models
from django.forms import ModelForm

# Create your models here.

class Submission(models.Model):
    submission_text = models.TextField(max_length=300)
    reported = models.BooleanField(default=False)

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['submission_text']