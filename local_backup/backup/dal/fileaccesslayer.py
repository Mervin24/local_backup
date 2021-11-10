from backup.models import File

def insertFile(file):
	file.save()

def getFileForUsername(username):
	return File.objects.filter(uploaded_by=username)
	
def getFile(id):
	return File.objects.get(pk=id)