from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from authentication.views import CustomUserViewSet, CustomUserSignupViewSet, Home
from comments.views import CommentViewSet
from issues.views import IssueViewSet
from projects.views import ProjectViewSet, ContributorViewSet, AdminProjectsViewSet
from rest_framework_nested import routers

schema_view = get_schema_view(
    openapi.Info(
        title="SoftDesk API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"signup", CustomUserSignupViewSet, basename="signup")
router.register(r"users", CustomUserViewSet, basename="users")
router.register(r"projects", ProjectViewSet, basename="projects")

projects_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
projects_router.register(r"issues", IssueViewSet, basename="issues")

projects_router.register(r"contributors", ContributorViewSet, basename="contributors")

issues_router = routers.NestedSimpleRouter(projects_router, r"issues", lookup="issue")
issues_router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("login/", LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/", include(router.urls)),
    path("api/", include(projects_router.urls)),
    path("api/", include(issues_router.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

""" router.register(r"api/users", CustomUserViewSet, basename="users")
# urls.py


# Wire up our API using automatic URL routing.

router.register("api/projects", ProjectViewSet, basename="projects")
router.register("api/issue", IssueViewSet, basename="issues")
router.register("api/comments", CommentViewSet, basename="comments")
router.register("api/contributor", ContributorViewSet, basename="contributor")
router.register("signup", CustomUserViewSet, basename="signup")

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("login/", LoginView.as_view(redirect_authenticated_user=True), name="login"),
                  path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
                  path("api/", include(router.urls)),
                  path("api-auth/", include("rest_framework.urls")),
                  path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
                  path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
                  path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
              ] + router.urls
 """
