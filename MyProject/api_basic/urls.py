# TODO: This import is used This import is used only for first 3 types of views(API View, Class Based View and Generic View)
# For Viewsets & Routers it need to be comented
# from MyProject.api_basic.serializers import ArticleSerializer
from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet, ArticleGenericViewSet, ArticleModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('article', ArticleViewSet, basename='article')
# router.register('article', ArticleGenericViewSet, basename='article')
router.register('article', ArticleModelViewSet, basename='article')

urlpatterns = [
    # api_view() Decorator In Function Based API Views - routes:
    # path('article/', article_list),
    # path('detail/<int:pk>', article_detail),

    # Class based API Views - routes:
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>', ArticleDetails.as_view()),

    # Generic Views & Mixins - routes:
    path('generic/article/<int:id>', GenericAPIView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),

    # Viewsets & Routers - routes:
    # path('viewset/', include(router.urls)),
    # path('viewset/<int:pk>', include(router.urls)),

    # Generic ViewSets - routes:
    # path('generic-viewset/', include(router.urls)),
    # path('generic-viewset/<int:pk>', include(router.urls)),

    # Model ViewSet - routes:
    path('model-viewset/', include(router.urls)),
    path('', include(router.urls)),
]