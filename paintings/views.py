from django.http import HttpResponse
from django.views.generic import TemplateView


from .services import get_color
from .tasks import render

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['field'] = self.request.session.get('field')
        render()
        return context


class UpdatePixelsView(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        if request.is_ajax():
            if request.session.get('field') is None or request.GET.get('clear'):
                render()
            else:
                pixel_id = list(map(int, request.GET.get('pixel_id').split(',')))
                color = get_color(25, list(map(int, request.GET.get('color').split(', '))))
                render(color, pixel_id)
            return HttpResponse(200)
        return HttpResponse(404)
