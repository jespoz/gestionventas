from django.shortcuts import render_to_response, RequestContext, get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import *
from django.db.models import *
from forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import logout


@login_required(login_url='login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    dimensiones = Proyecto.objects.values('objetivo__dimension__id', 'objetivo__dimension__dimension').annotate(total=Avg('cumplimiento')).order_by('objetivo__dimension_id')
    objetivos = Proyecto.objects.values('objetivo__dimension__dimension', 'objetivo__ciclo').annotate(total=Avg('cumplimiento'), count=Count('titulo'), cerrados=Sum('cerrado'), abiertos=Sum('abierto')).order_by('objetivo_id')
    return render_to_response('dashboard.html', {'dimensiones': dimensiones, 'objetivos': objetivos}, context_instance=RequestContext(request))


class ListCicloView(ListView):
    model = Ciclo
    template_name = 'ciclos/ciclos.html'


class CreateCicloView(FormView):
    model = Ciclo
    template_name = 'ciclos/ciclos_save_or_update.html'
    form_class = CicloForm

    def get_success_url(self):
        return reverse('ciclos_list')

    def get_context_data(self, **kwargs):
        context = super(CreateCicloView, self).get_context_data(**kwargs)
        context['action'] = reverse('ciclos_add')

        return context


class UpdateCicloView(UpdateView):
    model = Ciclo
    template_name = 'ciclos/ciclos_save_or_update.html'
    form_class = CicloForm

    def get_success_url(self):
        return reverse('ciclos_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateCicloView, self).get_context_data(**kwargs)
        context['action'] = reverse('ciclos_update', kwargs={'pk': self.get_object().id})

        return context


class DeleteCicloView(DeleteView):
    model = Ciclo
    template_name = 'ciclos/ciclos_delete.html'

    def get_success_url(self):
        return reverse('ciclos_list')


class ListDimensionView(ListView):
    model = Dimension
    template_name = 'dimensiones/dimensiones.html'


class CreateDimensionView(CreateView):
    model = Dimension
    template_name = 'dimensiones/dimensiones_save_or_update.html'
    form_class = DimensionForm

    def get_success_url(self):
        return reverse('dimensiones_list')

    def get_context_data(self, **kwargs):
        context = super(CreateDimensionView, self).get_context_data(**kwargs)
        context['action'] = reverse('dimensiones_add')

        return context


class UpdateDimensionView(UpdateView):
    model = Dimension
    template_name = 'dimensiones/dimensiones_save_or_update.html'
    form_class = DimensionForm

    def get_success_url(self):
        return reverse('dimensiones_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateDimensionView, self).get_context_data(**kwargs)
        context['action'] = reverse('dimensiones_update', kwargs={'pk': self.get_object().id})

        return context


class DeleteDimensionView(DeleteView):
    model = Dimension
    template_name = 'dimensiones/dimensiones_delete.html'

    def get_success_url(self):
        return reverse('dimensiones_list')

@login_required
def ListObjetivoView(request):
    objetivo = Proyecto.objects.values('objetivo__dimension__dimension', 'objetivo__objetivo', 'objetivo__ciclo', 'objetivo__id').annotate(total=Avg('cumplimiento')).order_by('objetivo__id')
    dimensiones = Dimension.objects.all()
    columnas = 12 / Dimension.objects.count()
    return render_to_response('objetivos/objetivos.html', {'objetivo': objetivo, 'dimension': dimensiones, 'columnas': columnas}, context_instance=RequestContext(request))


class UpdateObjetivoView(UpdateView):
    model = Objetivo
    template_name = 'objetivos/objetivos_save_or_update.html'
    form_class = ObjetivoForm

    def get_success_url(self):
        return reverse('objetivos_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateObjetivoView, self).get_context_data(**kwargs)
        context['action'] = reverse('objetivos_update', kwargs={'pk': self.get_object().id})

        return context


@login_required()
def ViewObjetivo(request, pk):
    objetivo = Objetivo.objects.values('ciclo').filter(id=pk).order_by('id')
    subobjetivos = Proyecto.objects.filter(objetivo=pk).order_by('cumplimiento', '-fecha_plazo')
    lideres = Proyecto.objects.values('lider__username', 'objetivo__objetivo', 'objetivo__ciclo', 'perfil__foto').filter(objetivo=pk).annotate(dcount=Count('lider'))
    return render_to_response('objetivos/objetivos_detail.html', {'objetivo': objetivo, 'subobjetivos': subobjetivos, 'lideres': lideres}, context_instance=RequestContext(request))


class UpdateProyectoView(UpdateView):
    model = Proyecto
    template_name = 'proyectos/update.html'
    form_class = ProyectoForm

    def get_success_url(self):
        return reverse('proyectos_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateProyectoView, self).get_context_data(**kwargs)
        context['action'] = reverse('proyectos_update', kwargs={'pk': self.get_object().id})

        return context

@login_required()
def ListProyectoView(request):
    proyecto_filtrado = Proyecto.objects.all().filter(lider__username=request.user.username)
    proyecto = Proyecto.objects.all()
    return render_to_response('proyectos/proyectos.html', {'object_list': proyecto, 'filtrado': proyecto_filtrado}, context_instance=RequestContext(request))


class DeleteProyectoView(DeleteView):
    model = Proyecto
    template_name = 'proyectos/proyectos_delete.html'

    def get_success_url(self):
        return reverse('proyectos_list')


class CreateProyectoView(CreateView):
    model = Proyecto
    template_name = 'proyectos/proyectos_save_or_update.html'
    form_class = ProyectoForm

    def get_success_url(self):
        return reverse('proyectos_list')


def DetalleDimension(request, pk):
    dimension = Proyecto.objects.values('objetivo__dimension__id', 'objetivo__dimension__dimension').annotate(total=Avg('cumplimiento')).order_by('objetivo__dimension_id').filter(objetivo__dimension__id=pk)
    proyectosAbiertos = Proyecto.objects.values('objetivo__ciclo', 'lider__username', 'titulo', 'fecha_plazo', 'cumplimiento', 'id').filter(dimension__id=pk, abierto=1).order_by('objetivo__ciclo', 'cumplimiento')
    proyectosCerrados = Proyecto.objects.values('objetivo__ciclo', 'lider__username', 'titulo', 'fecha_plazo', 'cumplimiento', 'id').filter(dimension__id=pk, abierto=0).order_by('objetivo__ciclo', 'cumplimiento')
    return render_to_response('dashboard/detalleDimension.html', {'dimension': dimension, 'proyectos': proyectosAbiertos, 'cerrados': proyectosCerrados}, context_instance=RequestContext(request))

from django.core import serializers
import json


def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]


def cargar_proyecto(request, id):
    if request.is_ajax():
        avance = Avance.objects.values('proyecto__dimension__id').filter(proyecto__id=id)
        avances_json = serializers.serialize('json', Avance.objects.all().filter(proyecto__id=id).order_by('ciclo_id'))
        avances_list = json.loads(avances_json)
        acumulado = Avance.objects.values('ciclo__clave').annotate(promedio=Avg('avance')).filter(proyecto__dimension=avance).order_by('ciclo_id')
        acumulado_dict = ValuesQuerySetToDict(acumulado)
        observaciones_json = serializers.serialize('json', Observacion.objects.all().filter(proyecto__id=id).order_by('-id'))
        observaciones_list = json.loads(observaciones_json)
        json_data = json.dumps({'avances': avances_list, 'observaciones': observaciones_list, 'acumulado': acumulado_dict})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404

def filtrar_objetivos(request, id):
        objetivos_json = serializers.serialize('json', Objetivo.objects.all().filter(dimension__id=id))
        objetivos_list = json.loads(objetivos_json)
        json_data = json.dumps({'objetivos': objetivos_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')

@login_required()
def carga_observacion(request, id):
        observacion = Observacion.objects.values('observacion', 'usuario__username').filter(id=id)
        observacion_list = ValuesQuerySetToDict(observacion)
        return HttpResponse(
            json.dumps({'observaciones': observacion_list}),
            content_type='application/json; charset=utf8'
        )


@login_required()
def agregar_observacion(request):
    if request.is_ajax():
        id = request.POST['id']
        if request.POST['observacion']:
            observacion_input = Observacion(observacion=request.POST['observacion'], proyecto_id=request.POST['id'], usuario_id=request.user.id)
            observacion_input.save()
        observaciones_json = serializers.serialize('json', Observacion.objects.all().filter(proyecto__id=id).order_by('-id'))
        observaciones_list = json.loads(observaciones_json)
        json_data = json.dumps({'observaciones': observaciones_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404


@login_required()
def carga_acumulado(request):
    if request.is_ajax():
        ciclo_json = serializers.serialize('json', Ciclo.objects.all())
        ciclo_list = json.loads(ciclo_json)
        acumulado = Avance.objects.values('ciclo__clave').annotate(promedio=Avg('avance')).order_by('ciclo_id')
        acumulado_dict = ValuesQuerySetToDict(acumulado)
        json_data = json.dumps({'acumulado': acumulado_dict, 'ciclo': ciclo_list})
        return HttpResponse(json_data, content_type='application/json; charset=utf8')
    else:
        raise Http404


@login_required()
def revisiones(request):
    ciclo = Ciclo.objects.values('clave').filter(status=False)
    proyecto_filtrado = Proyecto.objects.all().filter(lider__username=request.user.username).filter(abierto=1)
    proyecto = Proyecto.objects.all()
    return render_to_response('revisiones/revisiones.html', {'ciclo': ciclo, 'proyecto': proyecto, 'filtrado': proyecto_filtrado}, context_instance=RequestContext(request))


@login_required()
def detalle_revision(request, id):
    if request.is_ajax():
        proyecto = get_object_or_404(Proyecto, id=id)
        return render(request, 'revisiones/cuadroRevision.html', {'proyecto': proyecto})
    else:
        raise Http404

@login_required()
def agregar_revision(request):
    if request.is_ajax():
        proyecto = get_object_or_404(Proyecto, id=request.POST['proyecto'])
        proyecto.revision = request.POST['valor']
        proyecto.observacion_revision = request.POST['obs']
        proyecto.actualizado = True
        proyecto.save()
        return HttpResponse('revisiones')
    else:
        raise Http404

@login_required()
def agregar_check(request):
    if request.is_ajax():
        ciclo = Ciclo.objects.all().filter(status=False)
        avance = Avance()
        avance.avance = request.POST['avance']
        avance.ciclo = ciclo
        avance.proyecto_id = request.POST['proyecto']
        avance.checkeado = True
        avance.save()
    else:
        raise Http404

@login_required()
def check_revision(request, id):
    if request.is_ajax():
        proyecto = get_object_or_404(Proyecto, id=id)
        return render(request, 'revisiones/cuadroFinal.html', {'proyecto': proyecto})
    else:
        raise Http404