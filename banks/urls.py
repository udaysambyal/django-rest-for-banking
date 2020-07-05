from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('banks', views.bankViewset)
router.register('branches', views.branchesViewset)


urlpatterns = [
  #  path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('banks/', views.bankViewset.as_view()),
    path('branches/', views.branchesViewset.as_view()),
]