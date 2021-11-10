from django.core.files.storage import FileSystemStorage
import datetime
from backup.models import File
from backup.dal import fileaccesslayer

def saveFiles(files):
	fss = FileSystemStorage()
	for file in files:
		filename = fss.save(file.name, file)
		url = fss.url(filename)
		fileData = File()
		fileData.url = url
		fileData.name = file.name
		fileData.extension = getFileExtension(file.name)
		fileData.uploaded_by = "mervindalmet"
		fileData.uploaded_on = datetime.datetime.now()
		fileData.size = file.size
		fileaccesslayer.insertFile(fileData)

def getFileExtension(fname):
	return fname.split('.')[1]