from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
# from .models import *
# from storage.models import *
from .forms import *
import json
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
              <a class="nav-link active" aria-current="page" href="/dm/reports/">Reports</a>
            </li>
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


def field_item(request, field_source_name, field_name):
    if field_source_name and field_name:
        field_source = Source.objects.get(source_alias=field_source_name)
        field = get_object_or_404(Field, field_source=field_source, field_name=field_name)
    else:
        field = None

    context = {
        'fields': (field,),
        'field': field,
        'field_source': field_source,
        'field_lists': None,
        'current_field_list': None,
        'nav_bar': nav_bar,
        'bootstrap_link': bootstrap_link
    }
    return render(request, 'dm/fields.html', context)

def field_lists(request):
    all_field_lists = FieldList.objects.all()
    context = {
        'field_lists': all_field_lists,
        'nav_bar': nav_bar
    }
    return render(request, 'dm/field_lists.html', context)


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
        # 'add': True,
        'nav_bar': nav_bar,
        'bootstrap_link': bootstrap_link
    }
    return render(request, 'dm/field_list.html', context)


def field_list_edit(request, field_list_name):
    context = {
        'nav_bar': nav_bar,
        'bootstrap_link': bootstrap_link
    }

    if field_list_name != 'new':
        fieldlist = get_object_or_404(FieldList, field_list_name=field_list_name)
        context['edit'] = True
        context['add'] = False
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


def source_list(request, source_list_):
    if source_list:
        # sourcelist = get_object_or_404(Source, source_alias=source_list_name)
        sourcelist = get_object_or_404(SourceList, source_list=source_list)
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


def source_list_edit(request, source_list):
    context = {
        'nav_bar': nav_bar,
        'bootstrap_link': bootstrap_link
    }
    if source_list != 'new':
        sourcelist = get_object_or_404(SourceList, source_list=source_list)
        context['edit'] = True
        context['add'] = False
    else:
        sourcelist = None
        context['edit'] = True
        context['add'] = True

    if request.method == 'POST':
        form = SourceListForm(request.POST, instance=sourcelist)
        if form.is_valid():
            form.save()
            return redirect('/dm/source_lists/')  # Redirect to a new URL
    else:
        form = SourceListForm(instance=sourcelist)

    context['form'] = form
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


# def source_list_item(request, source_list_name, type):
#     source_list = Source.objects.get(source_alias=source_list_name)
#     if type == 'union':
#         filtered_sources = Source.objects.filter(source_union_list_name=source_list)
#     else:
#         filtered_sources = Source.objects.filter(source_alias=source_list)
#         # filtered_sources = Source.objects.filter(source_list_name=source_list)
#     all_source_lists = SourceList.objects.all()
#     context = {
#         'sources': filtered_sources,
#         'source_lists': all_source_lists,
#         'current_source_list': source_list,
#         'nav_bar': nav_bar
#     }
#     return render(request, 'dm/sources.html', context)


def source_list_item(request, source_list, type):
    source_list = SourceList.objects.get(source_list=source_list)
    if type == 'union':
        filtered_sources = Source.objects.filter(source_union_list=source_list)
    else:
        filtered_sources = Source.objects.filter(source_alias=source_list)
        # filtered_sources = Source.objects.filter(source_list_name=source_list)
    all_source_lists = SourceList.objects.all()
    context = {
        'sources': filtered_sources,
        'source_lists': all_source_lists,
        'current_source_list': source_list,
        'nav_bar': nav_bar
    }
    return render(request, 'dm/sources.html', context)


def reports(request):
    all_reports = Report.objects.all()
    context = {
        'reports': all_reports,
        'nav_bar': nav_bar
    }
    return render(request, 'dm/reports.html', context)


def report(request, report_name):
    report_item = Report.objects.get(report_name=report_name)
    filtered_report = Report.objects.filter(report_name=report_item)
    # all_queries = report.objects.all()
    context = {
        'report': report_item,
        'filtered_report': filtered_report,
        # 'queries': all_queries,
        'nav_bar': nav_bar,
        'bootstrap_link': bootstrap_link
    }
    return render(request, 'dm/report.html', context)


def diagram(request, source_type, source_name):
    linear = {}
    linear = diagr_line(source_type, source_name)

    # if source_type == 'report':
    #     source = Report.objects.get(report_name=source_name)
    #     linear["content"] = f"<a href=\"/dm/report/{source_name}/\" target=\"_blank\">{source_name}</a>"
    #     # source_list = SourceList.objects.get(source_list_name=source.source_list)
    # elif source_type == 'query':
    #     source = Query.objects.get(query_name=source_name)
    #     linear["content"] = f"<a href=\"/dm/query/{source_name}/\" target=\"_blank\">{source_name}</a>"
    #     # source_list = SourceList.objects.get(source_list_name=source.source_list)
    # elif source_type == 'data_source':
    #     source = Source.objects.get(source_name=source_name)
    #     linear["content"] = f"<a href=\"/dm/source_list/{source_name}/\" target=\"_blank\">{source_name}</a>"
    #     # source_list = SourceList.objects.get(source_list_name=source.source_list)
    # elif source_type == 'table':
    #     # source = Query.objects.get(source_name=source_name)
    #     linear["content"] = source_name

    # source_list = SourceList.objects.get(source_list=source.source_list)
    # sources = Source.objects.filter(source_union_list=source_list)
    # field_list = FieldList.objects.get(data_source=source_list)
    # fields = Field.objects.filter(source_list=source_list)

    # for source in sources:
    #     if source.source_type == 'data_source':
    #         source_list = SourceList.objects.get(source_list_name=source.source_list_name)
    #         sources = Source.objects.filter(source_union_list_name=source.source_list)
    #         field_list = FieldList.objects.get(data_source=source_list)
    #         fields = Field.objects.filter(source_list=source_list)
    #     elif source.source_type == 'query':
    #         query = Query.objects.get(query_name=source.query_name)
    #         filtered_query = Query.objects.get(query_name=query)
    #         linear["children"].append(filtered_query.query_name)
    #         try:
    #             source_list = SourceList.objects.get(source_list_name=query.source_list)
    #         except SourceList.DoesNotExist:
    #             source_list = None
    #         try:
    #             field_list = FieldList.objects.get(field_list_name=query.field_list)
    #         except FieldList.DoesNotExist:
    #             field_list = None
    #         try:
    #             fields = Field.objects.filter(field_list=query.field_list)
    #         except Field.DoesNotExist:
    #             fields = None
    #     else:
    #         None

    # scheme = {}
    # scheme["content"] = f"<a href=\"/dm/report/{source_name}/\" target=\"_blank\">{source_name}</a>"
    # scheme["children"] = [
    #     {
    #         "content": f"<a href=\"/dm/fields/{source_name.field_list}/\" target=\"_blank\">Field List</a>",
    #         "children": [
    #             {
    #                 # "content": "Field List"
    #                 # "content": f"<a href=\"/dm/fields/{report.field_list}/\">Field List</a>"
    #             }
    #         ]},
    #     {
    #         "content": f"<a href=\"/dm/fields/{source_name.source_list}/\" target=\"_blank\">Source List</a>",
    #         "children": [
    #             {
    #                 # "content": "Source List"
    #                 # "content": f"<a href=\"/dm/fields/{report.source_list}/\">Source List</a>"
    #             }
    #         ]
    #     }
    # ]
    context = {"model": linear}
    return render(request, 'dm/diagram.html', context)


def linearization(sources):
    if sources is None:
        return None
        #     {
        #     "content": source_list.name,
        #     "children": []
        # }

    children = []
    for source in sources:
        if source.source_type == 'data_source':
            try:
                source_list = SourceList.objects.get(source_list=source.source_list)
                child_content = source_list.source_list_name
            except SourceList.DoesNotExist:
                source_list = None
            try:
                sources = Source.objects.filter(source_union_list=source.source_list)
            except Source.DoesNotExist:
                sources = None
            try:
                field_list = FieldList.objects.get(data_source=source_list)
            except FieldList.DoesNotExist:
                field_list = None
            try:
                fields = Field.objects.filter(source_list=source_list)
            except Field.DoesNotExist:
                fields = None

            child_content = source_list.source_list_name
            children.append(linearization(sources))
            # children.append(create_nested_dict(child_content, depth - 1, num_children))

        elif source.source_type == 'query':
            query = Query.objects.get(query_name=source.query_name)
            # filtered_query = Query.objects.get(query_name=query)
            try:
                source_list = SourceList.objects.get(source_list=query.source_list)
            except SourceList.DoesNotExist:
                source_list = None
            try:
                field_list = FieldList.objects.get(field_list_name=query.field_list)
            except FieldList.DoesNotExist:
                field_list = None
            try:
                fields = Field.objects.filter(field_list=query.field_list)
            except Field.DoesNotExist:
                fields = None
        else:
            None

    return {
        "content": source_list.name,
        "children": children
    }


def diagr_line(source_type, source_name):
    if source_name == None:
        return {
            "content": "end"
        }
    elif source_type == 'table':
        return {
            "content": source_name
        }


    children = []
    if source_type == 'report':
        source = Report.objects.get(report_name=source_name)
        sources, source_list, field_list, fields = get_data_source(source)
        for source in sources:
            children.append(diagr_line(source.source_type, source.query_name))
    elif source_type == 'query':
        source = Query.objects.get(query_name=source_name)
        sources, source_list, field_list, fields = get_query_source(source)
        for source in sources:
            if source.source_type == 'data_source':
                f_source = source.source_list
            elif source.source_type == 'query':
                f_source = source.query_name
            elif source.source_type == 'table':
                f_source = source.table_name
            children.append(diagr_line(source.source_type, f_source))
    elif source_type == 'data_source':
        source = Source.objects.get(source_list=source_name)
        sources, source_list, field_list, fields = get_data_source(source)
        for source in sources:
            if source.source_type == 'data_source':
                f_source = source.source_list
            elif source.source_type == 'query':
                f_source = source.query_name
            elif source.source_type == 'table':
                f_source = source.table_name
            children.append(diagr_line(source.source_type, f_source))
    elif source_type == 'table':
        children.append(diagr_line('table', source_name))
    else:
        children.append(diagr_line(None, None))

    return {
        "content": str(source_name),
        "children": children
    }


def get_query_source(source):
    query = Query.objects.get(query_name=source.query_name)
    try:
        source_list = SourceList.objects.get(source_list=query.source_list)
    except SourceList.DoesNotExist:
        source_list = None
    try:
        sources = Source.objects.filter(source_union_list=source_list)
    except Source.DoesNotExist:
        sources = None
    try:
        field_list = FieldList.objects.get(field_list_name=query.field_list)
    except FieldList.DoesNotExist:
        field_list = None
    try:
        fields = Field.objects.filter(field_list=query.field_list)
    except Field.DoesNotExist:
        fields = None

    return sources, source_list, field_list, fields


def get_data_source(source):
    try:
        source_list = SourceList.objects.get(source_list=source.source_list)
    except SourceList.DoesNotExist:
        source_list = None
    try:
        sources = Source.objects.filter(source_union_list=source.source_list)
    except Source.DoesNotExist:
        sources = None
    try:
        field_list = FieldList.objects.get(data_source=source_list)
    except FieldList.DoesNotExist:
        field_list = None
    try:
        fields = Field.objects.filter(source_list=source_list)
    except Field.DoesNotExist:
        fields = None

    return sources, source_list, field_list, fields


def get_report_source(source):
    try:
        source_list = SourceList.objects.get(source_list=source.source_list)
    except Report.DoesNotExist:
        source_list = None
    try:
        sources = Source.objects.filter(source_union_list=source_list)
    except Source.DoesNotExist:
        sources = None
    try:
        field_list = FieldList.objects.get(data_source=source_list)
    except FieldList.DoesNotExist:
        field_list = None
    try:
        fields = Field.objects.filter(source_list=source_list)
    except Field.DoesNotExist:
        fields = None

    return sources, source_list, field_list, fields

# def test_source(request, source_list_name, ch_source_list_name):
#     if source_list_name != '0':
#         source_list = SourceList.objects.get(source_union_list_name=source_list_name)
#         filtered_sources = Source.objects.filter(source_union_list_name=source_list)
#     else:
#         source_list = SourceList.objects.get(source_list_name=ch_source_list_name)
#         filtered_sources = Source.objects.filter(source_union_list_name=source_list)
#
#     all_source_lists = SourceList.objects.all()
#     context = {
#         'sources': filtered_sources,
#         'source_lists': all_source_lists,
#         'current_source_list': source_list,
#         'nav_bar': nav_bar
#     }
#     return render(request, 'dm/sources.html', context)
#
#
# def test_static(request):
#     return render(request, 'dm/test_static.html')
