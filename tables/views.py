from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.files.storage import FileSystemStorage
from config.settings import MEDIA_ROOT
from django.views.static import serve
from .utils import imageToTable
import os



def landing(request):
    return render(request, 'tables/landing_page.html')


def home(request):
    return render(request, 'tables/home.html')





# AJAX process route
def process(request):
    if request.method == 'POST' and request.FILES['photo']:
        myfile = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        image_path = os.path.join(MEDIA_ROOT, filename)
        dataF = imageToTable(image_path)
        os.remove(image_path)
        return HttpResponse(dataF)


# Download excel file
def downloadX(request):
    file_path = os.path.join(MEDIA_ROOT, 'downloadData', 'outputX.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


# Download csv file
def downloadC(request):
    csv_file_path = os.path.join(MEDIA_ROOT, 'downloadData', 'outputC.csv')
    return serve(csv_file_path, csv_file_path)


def exportJson(request):
    file_path = os.path.join(MEDIA_ROOT, 'downloadData', 'outputJ.json')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/json')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404