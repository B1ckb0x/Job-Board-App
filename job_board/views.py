from django.shortcuts import render, HttpResponse
from .models import JobPosting


# Create your views here.
def index(request):
    active_jobs = JobPosting.objects.filter(is_active=True)
    context = {
        'job_posting' : active_jobs
    }
    return render(request, 'job_board/index.html', context)


def job_detail(request, pk):
    job_post = JobPosting.objects.get(id=pk)
    context = {
        'post' : job_post
    }
    return render(request, 'job_board/detail.html', context)


def all_jobs( request):
    jobs_list = JobPosting.objects.all()
    context = {
        'all_jobs_list' : jobs_list
    }
    return render(request, 'job_board/all_job.html', context)