from django.core.files.storage import FileSystemStorage
import datetime
from backup.models import File
from backup.dal import fileaccesslayer

from django.conf import settings



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
	parts = fname.split('.')
	return parts[1] if len(parts) > 1 else parts[0]

def getFilesForUserName(username):
	return fileaccesslayer.getFilesForUsername(username)