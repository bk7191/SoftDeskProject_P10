from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from authentication.views import UserViewSet, CustomUserViewSet
from comments.views import CommentViewSet
from issues.views import IssueViewSet
from projects.views import ProjectViewSet, ContributorViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
# from issues.views import IssuesViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename="users")

# Wire up our API using automatic URL routing.

router.register('api/projects', ProjectViewSet, basename="projects")
router.register('api/issue', IssueViewSet, basename="issues")
router.register('api/comments', CommentViewSet, basename="comments")
router.register('api/contributor', ContributorViewSet, basename="contributor")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
                  # path('api-auth/', include('rest_framework.urls')),
                  # path('api-auth/', include('config_API.urls.jwt')),
                  # path('api/issue/', IssueViewSet.as_view({'get': 'list'}), name='issues'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

              ] + router.urls
