from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cms.models import Component
from cms.serializers import ComponentSerializer


class ComponentsViewSet(ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

    def filter_queryset(self, queryset):
        if self.action == 'list':
            return queryset.filter(parent__isnull=True)
        return queryset

    @action(methods=['get'], detail=False,
            url_path='by_page')
    def by_page(self, *args, **kwargs):
        try:
            component = Component.objects.get(path=self.request.query_params.get('path', '/'), parent__isnull=True)
        except Component.DoesNotExist:
            component = Component.objects.get(path='/', parent__isnull=True)
        return Response(self.get_serializer(component).data)
