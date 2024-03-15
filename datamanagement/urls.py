from django.urls import path
from .views import *

urlpatterns = [
    # path("upload/", upload_file),
    path("", main),
    path("fields/", fields),
    path("fields/<str:fields_list_name>/", field_list_item),
    path("field_lists/", field_lists),
    path("sources/", sources),
    path("sources/<str:source_list_name>/", source_list_item),
    path("source_lists/", source_lists),
    path("queries/", queries),
    path("test_static/", test_static),
]