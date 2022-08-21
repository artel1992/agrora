from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cms.models import Component, AppScript
from cms.serializers import ComponentSerializer, AppScriptSerializer
from cms.services import get_empty_components, get_empty_pages


class ComponentsViewSet(ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

    def filter_queryset(self, queryset):
        if self.action == 'list':
            return queryset.filter(parent__isnull=True)
        return queryset

    @action(methods=['get'],
            detail=False,
            url_path=r'pages')
    def empty_pages(self, *args, **kwargs):
        return Response(get_empty_pages())

    @action(methods=['get'],
            detail=False,
            url_path='empty')
    def empty_components(self, *args, **kwargs):
        data = get_empty_components(kwargs.get('level'))
        return Response(data)

    @action(methods=['get'], detail=False,
            url_path='by_page')
    def by_page(self, *args, **kwargs):
        try:
            component = Component.objects.get(path=self.request.query_params.get('path', '/'), parent__isnull=True)
        except Component.DoesNotExist:
            try:
                component = Component.objects.get(path='/', parent__isnull=True)
            except Component.DoesNotExist:
                return Response(None)
        return Response(self.get_serializer(component).data)


class AppScriptViewSet(ModelViewSet):
    queryset = AppScript.objects.all()
    serializer_class = AppScriptSerializer
