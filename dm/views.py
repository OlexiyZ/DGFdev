from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .models import *
from storage.models import *

nav_bar = '''
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="/dm/queries/">Queries</a>
            </li>
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="/dm/field_lists/">Field Lists</a>
            </li>
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="/dm/fields/">Fields</a>
            </li>
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="/dm/source_lists/">Source Lists</a>
            </li>
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="/dm/sources/">Sources</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
'''


def main(request):
    context = {
        'nav_bar': nav_bar
    }
    return render(request, 'dm/main.html', context)


def fields(request):
    all_fields = Field.objects.all()
    all_field_lists = FieldList.objects.all()
    context = {
        'fields': all_fields,
        'field_lists': all_field_lists,
        'nav_bar': nav_bar
    }
    return render(request, 'dm/fields.html', context)


def field_list_item(request, fields_list_name):
    field_list = FieldList.objects.get(field_list_name=fields_list_name)
    filtered_fields = Field.objects.filter(field_list=field_list)
    all_field_lists = FieldList.objects.all()
    context = {
        'fields': filtered_fields,
        'field_lists': all_field_lists,
        'current_field_list': field_list,
        'nav_bar': nav_bar
    }
    return render(request, 'dm/fields.html', context)


def field_lists(request):
    all_field_lists = FieldList.objects.all()
    context = {
        'field_lists': all_field_lists,
        'nav_bar': nav_bar
    }
    return render(request, 'dm/field_lists.html', context)


def queries(request):
    all_queries = Query.objects.all()
    context = {
        'queries': all_queries,
        'nav_bar': nav_bar
    }
    return render(request, 'dm/queries.html', context)


def source_lists(request):
    all_source_lists = SourceList.objects.all()
    context = {
        'source_lists': all_source_lists,
        'nav_bar': nav_bar
    }
    return render(request, 'dm/source_lists.html', context)


def sources(request):
    all_sources = Source.objects.all()
    all_source_lists = SourceList.objects.all()
    context = {
        'sources': all_sources,
        'source_lists': all_source_lists,
        'nav_bar': nav_bar
    }
    return render(request, 'dm/sources.html', context)


def source_list_item(request, source_list_name):
    source_list = SourceList.objects.get(source_list_name=source_list_name)
    filtered_sources = Source.objects.filter(source_union_list_name=source_list)
    all_source_lists = SourceList.objects.all()
    context = {
        'sources': filtered_sources,
        'source_lists': all_source_lists,
        'current_source_list': source_list,
        'nav_bar': nav_bar
    }
    return render(request, 'dm/sources.html', context)


def test_static(request):
    return render(request, 'dm/test_static.html')