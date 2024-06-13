from authentication.views import CustomUserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", CustomUserViewSet, basename="user")
urlpatterns = router.urls
