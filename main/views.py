from django.shortcuts import render
from django.http import HttpResponse
from .models import codeDb
from datetime import datetime


# Create your views here.


def homepage(request):
    return render(request=request,
                  template_name="main/index.html",
                  context={'codeDb': codeDb.objects.all})


def save_to_db(request):
    if request.method == 'POST':
        codez = request.POST['code']
        toe = request.POST['datetime']
        countz = 1
        message = 'Succesfully stored to database :)'

        codeDb.objects.create(
            the_code=codez,
            time_of_execution=toe,
            count=countz
        )
    else:
        message = 'unsuccesful. File not saved:('
    return HttpResponse(message)
