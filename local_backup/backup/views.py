from django.shortcuts import render
from django.http import	HttpResponse
from .managers import fileStorageManager

GET = "GET"
POST = "POST"

uploadedFiles = "uploadedFiles"
USER_NAME = "mervindalmet"
USER_NAME_KEY = 'username'

# Create your views here.
def index(request):
	request.session[USER_NAME_KEY] = USER_NAME
	return render(request, "backup_index.html")

def fileUpload(request):
	username = request.session[USER_NAME_KEY]
	if request.method == POST and request.FILES:
		files = request.FILES.getlist(uploadedFiles)
		fileStorageManager.saveFiles(files, username)
	return HttpResponse(200)

def viewUploads(request):
	username = request.session[USER_NAME_KEY]
	files = fileStorageManager.getFilesForUserName(username)
	return render(request, "view_uploads.html", {'files' : files})