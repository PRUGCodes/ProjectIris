from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from better_profanity import profanity
from django.views import generic
from django.db.models import Max
import random

from .models import Submission, SubmissionForm

def getRandomSubmission(max):
    num = random.randint(2, max)
    try:
        submission = Submission.objects.get(id=num)
    except:
        submission = getRandomSubmission(max)

    if submission.reported == True:
        submission = getRandomSubmission(max)
    
    return submission


def index(request):
    submission = SubmissionForm()
    return render(request, 'submissions/index.html', {'form': submission})
        
def randompost(request):
    if request.method == 'POST':
        submission = SubmissionForm(request.POST)
        if submission.is_valid():
            submission = SubmissionForm(request.POST)
            new_submission = submission.save(commit=False)
            submission_text = new_submission.submission_text
            output = profanity.censor(submission_text)
            if submission_text != output:
                new_submission.reported = True
                randomsubmission = Submission.objects.get(id=1)
            else:
                new_submission.reported = False
                randomsubmission = getRandomSubmission(Submission.objects.count())
            new_submission.save()
            
            return render(request, 'submissions/randompost.html', {'rndpost': randomsubmission})
    else:
        return redirect('index')
