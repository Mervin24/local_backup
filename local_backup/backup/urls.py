from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
		path('', views.index, name='index'),
		path('file-upload', views.fileUpload, name='fileUpload'),
		path('view-uploads', views.viewUploads, name='viewUploads'),
		path('downloadfile/<str:id>', views.download, name="downloadfile")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)