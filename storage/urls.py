from django.urls import path
from .views import *

urlpatterns = [
    path("import/", excelImport),
    path("upload_file/", upload_file),
    path("select_table/", select_table),
]