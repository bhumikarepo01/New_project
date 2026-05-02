from django.contrib import admin
from .models import Company, JobPost


class JobPostInline(admin.TabularInline):
    model = JobPost
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'industry']
    search_fields = ['name']
    inlines = [JobPostInline]


class JobPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'salary', 'posted_date']
    list_filter = ['company']
    search_fields = ['title']


admin.site.register(Company, CompanyAdmin)
admin.site.register(JobPost, JobPostAdmin)