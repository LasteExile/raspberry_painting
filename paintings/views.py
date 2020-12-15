import time

from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

from .services import get_color, render


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.get('field') is None:
                self.request.session['field'] = []
                self.request.session['field'].append([[[i, j, '255, 255, 255'] for j in range(0, 16)] for i in range(0, 16)])
                self.request.session.save()
        if self.request.session.get('active_page') is None:
                self.request.session['active_page'] = 0
                self.request.session.save()
        context['field'] = self.request.session.get('field')
        context['active_page'] = self.request.session.get('active_page')
        return context


class AddPageView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        if request.is_ajax():
            request.session['field'].append(request.session['field'][-1])
            request.session.save()
            return JsonResponse({'field': request.session['field'][-1]}, status=200)
        return HttpResponse(404)


class UpdatePixelsView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        if request.is_ajax():
            if request.GET.get('timeout'):
                timeout = int(request.GET.get('timeout'))
                reapets = int(request.GET.get('reapets'))
                for i in range(0, reapets):
                    for j in self.request.session['field']:
                        render(j)
                        time.sleep(timeout/1000)
            elif request.GET.get('active_page'):
                self.request.session['active_page'] = request.GET.get('active_page')
                self.request.session.save()
            elif request.GET.get('clear_session'):
                self.request.session['field'] = []
                self.request.session['active_page'] = 0
                self.request.session['field'].append([[[i, j, '255, 255, 255'] for j in range(0, 16)] for i in range(0, 16)])
                self.request.session.save()
            elif request.GET.get('clear'):
                page = int(request.GET.get('page'))
                request.session['field'] = []
                request.session.save()
                request.session['field'][page] = [[[i, j, '255, 255, 255'] for j in range(0, 16)] for i in range(0, 16)]
                request.session.save()
            else:
                pixel_id = list(map(int, request.GET.get('pixel_id').split()))
                color = request.GET.get('color')
                page = int(request.GET.get('page'))
                request.session['field'][page][pixel_id[0]][pixel_id[1]][2] = color
                request.session.save()
            return HttpResponse(request.session['field'])
        return HttpResponse(404)
