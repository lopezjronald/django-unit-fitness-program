from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Airman


# def airman_list(request):
#     object_list = Airman.active.all()
#     paginator = Paginator(object_list, 10) # airmen in each page
#     page = request.GET.get('page')
#     try:
#         airmen = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         airmen = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         airmen = paginator.page(paginator.num_pages)
#     return render(request,
#                   'unit/airman/list.html',
#                   {'page': page,
#                    'airmen': airmen})

class AirmanListView(ListView):
    queryset = Airman.active.all()
    context_object_name = 'airmen'
    paginate_by = 10
    template_name = 'unit/airman/list.html'


def airman_detail(request, year, month, day, airman):
    airman = get_object_or_404(Airman,
                               airman_slug=airman,
                               active_status='active',
                               test_date__year=year,
                               test_date__month=month,
                               test_date__day=day)
    return render(request,
                  'unit/airman/detail.html',
                  {'airman': airman})
