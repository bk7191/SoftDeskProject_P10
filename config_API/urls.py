from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from authentication.views import UserViewSet, CustomUserViewSet
from projects.views import ProjectViewSet

# from issues.views import IssuesViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename="users")

# Wire up our API using automatic URL routing.

router.register('projects', ProjectViewSet, basename="projects")
# router.register('issues', IssuesViewSet, basename="issues")
# router.register('comments', CommentsViewSet, basename="comments")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),

    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]
