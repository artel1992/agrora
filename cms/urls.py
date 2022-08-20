from rest_framework.routers import DefaultRouter

from cms.views import ComponentsViewSet

router = DefaultRouter()
router.register('components', ComponentsViewSet)
urlpatterns = router.urls
