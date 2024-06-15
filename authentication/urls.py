from authentication.views import CustomUserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"api/users", CustomUserViewSet, basename="user")
urlpatterns = router.urls
