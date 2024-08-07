from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from authentication.views import CustomUserViewSet, CustomUserRegisterViewSet
from comments.views import CommentViewSet
from issues.views import IssueViewSet
from projects.views import ProjectViewSet, ContributorViewSet

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

router.register(r"users", CustomUserViewSet, basename="users")
router.register(r"projects", ProjectViewSet, basename="projects")
# registered= routers.NestedSimpleRouter(router, r'register', lookup='register-user')
router.register(r"register", CustomUserRegisterViewSet, basename="register")

projects_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
projects_router.register(r"issues", IssueViewSet, basename="issues")

projects_router.register(r"contributors", ContributorViewSet, basename="contributors")

issues_router = routers.NestedSimpleRouter(projects_router, r"issues", lookup="issue")
# issues_router.register(r"comments", CommentViewSet, basename="comments")
issues_router.register(r'comments', CommentViewSet,
                       basename='comment')

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", Home.as_view(), name="home"),
    # path("login/", LoginView.as_view(redirect_authenticated_user=True), name="login"),
    # path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    # path('api/internal/register', CreateUserView.as_view(),name='register'),
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

