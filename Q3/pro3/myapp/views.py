from django.shortcuts import render, redirect, get_object_or_404
from .models import JobPost, Company
from .forms import JobPostForm


def job_list(request):
    company_id = request.GET.get('company')
    jobs = JobPost.objects.all()

    if company_id:
        jobs = jobs.filter(company_id=company_id)

    companies = Company.objects.all()

    return render(request, 'job_list.html', {
        'jobs': jobs,
        'companies': companies
    })


def job_create(request):
    form = JobPostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('job_list')

    return render(request, 'job_form.html', {'form': form})


def job_detail(request, pk):
    job = get_object_or_404(JobPost, id=pk)
    return render(request, 'job_detail.html', {'job': job})