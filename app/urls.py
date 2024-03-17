from django.urls import path
from .views import index,PrintPdf,exportCSV,InsertStudentFromCSV
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static


urlpatterns = [
    path('',index,name='Index'),
    path('print-pdf/',PrintPdf,name='printPdf'),
    path('export-csv/',exportCSV,name='exportCSV'),
    path('import-csv/',InsertStudentFromCSV,name='importData'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
