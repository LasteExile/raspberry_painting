from django.http import HttpResponse
from django.views.generic import TemplateView

from .services import get_color, render


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.get('field') is None:
            self.request.session['field'] = [[[i, j, '255, 255, 255'] for j in range(0, 16)] for i in range(0, 16)]
            self.request.session.save()
            render()
        context['field'] = self.request.session.get('field')
        return context

class UpdatePixelsView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        if request.is_ajax():
            if request.GET.get('clear'):
                request.session['field'] = [[[i, j, '255, 255, 255'] for j in range(0, 16)] for i in range(0, 16)]
                request.session.save()
                render()
            else:
                pixel_id = list(map(int, request.GET.get('pixel_id').split(',')))
                color = request.GET.get('color')
                request.session['field'][pixel_id[0]][pixel_id[1]][2] = color
                request.session.save()
                render(get_color(10, color), pixel_id)
            return HttpResponse(200)
        return HttpResponse(404)
