from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .models import *
# from storage.models import *
from .forms import *
# FormSourceList

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

bootstrap_link = '''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">'''


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


# def field_list(request, field_list_name):
#     field_list = get_object_or_404(FieldList, field_list_name=field_list_name)
#     form = FieldListDisplayForm(instance=field_list)
#     context = {
#         'form': form,
#         'nav_bar': nav_bar,
#         'bootstrap_link': bootstrap_link
#     }
#     return render(request, 'dm/field_list.html', context)


def field_list(request, field_list_name):
    if field_list_name:
        fieldlist = get_object_or_404(FieldList, field_list_name=field_list_name)
    else:
        fieldlist = None

    form = FieldListForm(instance=fieldlist)

    for field in form.fields:
        form.fields[field].disabled = True

    context = {
        'form': form,
        'edit': False,
        'add': True,
        'nav_bar': nav_bar,
        'bootstrap_link': bootstrap_link
    }
    return render(request, 'dm/field_list.html', context)


def field_list_edit(request, field_list_name):
    context = {
        # 'form': form,
        # 'edit': True,
        'nav_bar': nav_bar,
        'bootstrap_link': bootstrap_link
    }

    if field_list_name != 'new':
        fieldlist = get_object_or_404(FieldList, field_list_name=field_list_name)
        context['edit'] = True
    else:
        fieldlist = None
        context['edit'] = True
        context['add'] = True

    if request.method == 'POST':
        form = FieldListForm(request.POST, instance=fieldlist)
        if form.is_valid():
            form.save()
            return redirect('/dm/field_lists/')
    else:
        form = FieldListForm(instance=fieldlist)

    # context = {
    #     'form': form,
    #     # 'edit': True,
    #     'nav_bar': nav_bar,
    #     'bootstrap_link': bootstrap_link
    # }
    context['form'] = form

    return render(request, 'dm/field_list.html', context)


def queries(request):
    all_queries = Query.objects.all()
    context = {
        'queries': all_queries,
        'nav_bar': nav_bar
    }
    return render(request, 'dm/queries.html', context)


def query(request, query_name):
    query_item = Query.objects.get(query_name=query_name)
    filtered_query = Query.objects.filter(query_name=query_item)
    # all_queries = Query.objects.all()
    context = {
        'query': query_item,
        'filtered_query': filtered_query,
        # 'queries': all_queries,
        'nav_bar': nav_bar,
        'bootstrap_link': bootstrap_link
    }
    return render(request, 'dm/query.html', context)


def source_lists(request):
    all_source_lists = SourceList.objects.all()
    context = {
        'source_lists': all_source_lists,
        'nav_bar': nav_bar
    }
    return render(request, 'dm/source_lists.html', context)


def source_list(request, source_list_name):
    if source_list_name:
        sourcelist = get_object_or_404(SourceList, source_list_name=source_list_name)
    else:
        sourcelist = None

    form = SourceListForm(instance=sourcelist)

    for field in form.fields:
        form.fields[field].disabled = True

    context = {
        'form': form,
        'edit': False,
        'nav_bar': nav_bar,
        'bootstrap_link': bootstrap_link
    }
    return render(request, 'dm/source_list.html', context)


def source_list_edit(request, source_list_name):
    if source_list_name != 'new':
        sourcelist = get_object_or_404(SourceList, source_list_name=source_list_name)
    else:
        sourcelist = None

    if request.method == 'POST':
        form = SourceListForm(request.POST, instance=sourcelist)
        if form.is_valid():
            form.save()
            return redirect('/dm/source_lists/')  # Redirect to a new URL
    else:
        form = SourceListForm(instance=sourcelist)

    context = {
        'form': form,
        'edit': True,
        'nav_bar': nav_bar,
        'bootstrap_link': bootstrap_link
    }
    return render(request, 'dm/source_list.html', context)


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


def test_source(request, source_list_name, ch_source_list_name):
    if source_list_name != '0':
        source_list = SourceList.objects.get(source_union_list_name=source_list_name)
        filtered_sources = Source.objects.filter(source_union_list_name=source_list)
    else:
        source_list = SourceList.objects.get(source_list_name=ch_source_list_name)
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
