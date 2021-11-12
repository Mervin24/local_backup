from django.core.files.storage import FileSystemStorage
import datetime
from backup.models import File
from backup.dal import fileaccesslayer
from django.conf import settings
import mimetypes

def saveFiles(files, username):
	fss = FileSystemStorage()
	for file in files:
		filename = fss.save(username+"/"+file.name, file)
		url = fss.url(filename)
		fileData = File()
		fileData.url = url
		fileData.name = file.name
		fileData.extension = getFileExtension(file.name)
		fileData.uploaded_by = username
		fileData.uploaded_on = datetime.datetime.now()
		fileData.size = file.size
		fileaccesslayer.insertFile(fileData)

def getFileExtension(fname):
	return fname.split('.')[-1]

def getFilesForUserName(username):
	return fileaccesslayer.getFilesForUsername(username)

def getFileForId(id):
	return fileaccesslayer.getFile(id)

def getDownloadFileForId(id):
	file = getFileForId(id)
	path_to_file = settings.MEDIA_ROOT+".."+file.url
	filename = path_to_file.split('/')[-1]
	mime_type, _ = mimetypes.guess_type(path_to_file)
	return open(path_to_file, 'rb'), filename, mime_type