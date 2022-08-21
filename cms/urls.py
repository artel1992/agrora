from rest_framework.routers import DefaultRouter

from cms.views import ComponentsViewSet, AppScriptViewSet

router = DefaultRouter()
router.register('components', ComponentsViewSet)
router.register('scripts', AppScriptViewSet)
urlpatterns = router.urls
