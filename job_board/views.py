from django.shortcuts import render, get_object_or_404

from .models import JobPosting


# Create your views here.
def index(request):
    active_jobs = JobPosting.objects.all()
    context = {
        'job_posting': active_jobs
    }
    return render(request, 'job_board/index.html', context)


def job_detail(request, pk):
    job_post = get_object_or_404(JobPosting, id=pk)
    context = {
        'post': job_post
    }
    return render(request, 'job_board/detail.html', context)

