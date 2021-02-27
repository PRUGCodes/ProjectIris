from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from better_profanity import profanity
from django.views import generic

from .models import Submission, SubmissionForm

def index(request):
    if request.method == 'POST':
        submission = SubmissionForm(request.POST)
        if submission.is_valid():
            submission = SubmissionForm(request.POST)
            new_submission = submission.save(commit=False)
            submission_text = new_submission.submission_text
            output = profanity.censor(submission_text)
            if submission_text != output:
                new_submission.reported = True
            else:
                new_submission.reported = False
            new_submission.save()
            return redirect('index')
    else:
        submission = SubmissionForm()
    return render(request, 'submissions/index.html', {'form': submission})
        
def submitpost(request):
    submission = SubmissionForm(request.POST)
    new_submission = submission.save(commit=False)
    submission_text = new_submission.submission_text
    output = profanity.censor(submission_text)
    if submission_text != output:
        new_submission.reported = True
    else:
        new_submission.reported = False
    new_submission.save()

