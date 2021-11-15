from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserModelViewSet, basename='users')
urlpatterns = router.urls
