from django.urls import path

from .views import IndexView, UpdatePixelsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('update_pixels', UpdatePixelsView.as_view(), name='pixels'),
]