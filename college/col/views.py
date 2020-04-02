from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from col.models import Notice


class NoticeListView(ListView):
    model = Notice


@method_decorator(login_required, name='dispatch')
class NoticeDetailView(DetailView):
    model = Notice
