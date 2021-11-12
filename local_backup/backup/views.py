from django.shortcuts import render
from django.http import	HttpResponse
from .managers import fileStorageManager
from django.conf import settings

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

def download(request, id):
	username = request.session[USER_NAME_KEY]
	path, filename, mime_type = fileStorageManager.getDownloadFileForId(id)
	print(filename)
	response =  HttpResponse(path, content_type=mime_type)
	response['Content-Disposition'] = "attachment; filename=%s" % filename
	print(response)
	return response
