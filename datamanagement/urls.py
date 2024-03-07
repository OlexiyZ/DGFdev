from django.urls import path
from .views import *

urlpatterns = [
    # path("upload/", upload_file),
    path("", main),
    path("fields/", fields),
    path("field_lists/", field_lists),
    path("fields/<str:fields_list_name>/", field_list_item),
    # path("fields/field_list/<str:fields_list_name>/", field_list_item),
    path("queries/", queries),
]