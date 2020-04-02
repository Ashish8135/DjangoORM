from django.urls import path
from django.views.generic import RedirectView

from col import views

urlpatterns = [
    path('notice/',views.NoticeListView.as_view()),
    path('notice/<int:pk>',views.NoticeDetailView.as_view()),
    path('',RedirectView.as_view(url='notice/')),
]