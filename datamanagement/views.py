from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .models import *
from storage.models import *


def main(request):
    return render(request, 'datamanagement/main.html')

def fields(request):
    all_fields = Field.objects.all()
    all_field_lists = FieldList.objects.all()
    context = {
        'fields': all_fields,
        'field_lists': all_field_lists
    }
    return render(request, 'datamanagement/fields.html', context)


def field_list_item(request, fields_list_name):
    field_list = FieldList.objects.get(field_list_name=fields_list_name)
    filtered_fields = Field.objects.filter(field_list=field_list)
    all_field_lists = FieldList.objects.all()
    context = {
        'fields': filtered_fields,
        'field_lists': all_field_lists,
        'current_field_list': field_list
    }
    return render(request, 'datamanagement/fields.html', context)


def field_lists(request):
    all_field_lists = FieldList.objects.all()
    context = {
        'field_lists': all_field_lists
    }
    return render(request, 'datamanagement/field_lists.html', context)


def queries(request):
    all_queries = Query.objects.all()
    context = {
        'queries': all_queries
    }
    return render(request, 'datamanagement/queries.html', context)

