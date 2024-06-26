from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import MovieViewSet, ActorViewSet, MovieActorAPIView, \
    CommentCreateAPIView, CommentListAPIView, CommentDeletApiView

from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path

schema_view = get_schema_view(
    openapi.Info(
        title="Netflix",
        default_version='v1',
        description="API documentation for Netflix project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="1.quvonchbek.ibragimov@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
router = DefaultRouter()
router.register(r'movies', MovieViewSet, 'movies')
router.register(r'actors', ActorViewSet, 'actors')

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('comments/', CommentListAPIView.as_view()),
    path('create-comment/', CommentCreateAPIView.as_view()),
    path('delete-comment/<int:id>/', CommentDeletApiView.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
