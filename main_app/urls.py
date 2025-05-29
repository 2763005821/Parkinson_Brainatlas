from django.urls import path
from .views import CellAtlasListView

urlpatterns = [
    path('cellatlas/', CellAtlasListView.as_view(), name='cellatlas-list'),
]
