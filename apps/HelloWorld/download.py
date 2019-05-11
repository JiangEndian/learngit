from django.http import HttpResponseRedirect 
from django.shortcuts import render
import os

def download(request):
    file_list = os.listdir("statics/files")
    file_dict = {'file_list':file_list}
    return render(request, 'download.html', file_dict)

