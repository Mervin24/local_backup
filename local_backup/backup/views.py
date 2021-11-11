from django.shortcuts import render
from django.http import	HttpResponse
from .managers import fileStorageManager
from django.conf import settings
import mimetypes

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
	print(files[0].url)
	return render(request, "view_uploads.html", {'files' : files})

def download(request, id):
	username = request.session[USER_NAME_KEY]
	file = fileStorageManager.getFileForId(id)
	path_to_file = settings.MEDIA_ROOT+".."+file.url
	filename = path_to_file.split('/')[-1]
	path = open(path_to_file, 'rb')
	mime_type, _ = mimetypes.guess_type(path_to_file)
	response =  HttpResponse(path, content_type=mime_type)
	response['Content-Disposition'] = "attachment; filename=%s" % filename
	return response
