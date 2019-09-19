from django.shortcuts import render
from django.http import HttpResponse
from .models import codeDb
from datetime import datetime


# Create your views here.


def homepage(request):
    return render(request=request,
                  template_name="main/index.html",
                  context={'codeDb': codeDb.objects.all})


def fetchpage(request):
    return render(request=request,
                  template_name="fetch/index.html",
                  context={'codeDb': codeDb.objects.all})


def save_to_db(request):
    if request.method == 'POST':
        post_code = request.POST['code']
        post_time = request.POST['datetime']
        post_count = 1
        flag = 1
        for entry in codeDb.objects.all():
            if entry.the_code == post_code:
                entry.count += 1
                entry.time_of_execution = post_time
                entry.save()
                flag = 0
        if flag == 1:
            codeDb.objects.create(
                the_code=post_code,
                time_of_execution=post_time,
                count=post_count
            )
            message = 'Succesfully stored to database :)'
        elif flag == 0:
            message = 'Database updated'

    else:
        message = 'unsuccesful. File not saved:('
    return HttpResponse(message)
