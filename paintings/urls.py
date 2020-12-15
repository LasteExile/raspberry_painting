from django.urls import path

from .views import IndexView, UpdatePixelsView, AddPageView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('update_pixels', UpdatePixelsView.as_view(), name='update_pixels'),
    path('add_page', AddPageView.as_view(), name='add_page'),
]