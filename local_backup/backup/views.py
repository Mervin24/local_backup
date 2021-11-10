from django.shortcuts import render
from django.http import	HttpResponse
from .utils.filestorage import saveFiles

GET = "GET"
POST = "POST"

uploadedFiles = "uploadedFiles"

# Create your views here.
def index(request):
	return render(request, "backup_index.html")

def fileUpload(request):
	if request.method == POST and request.FILES:
		files = request.FILES.getlist(uploadedFiles)
		saveFiles(files)
	return HttpResponse(200)