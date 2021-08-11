from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('TaskAPI',views.TaskAPIViewSet, basename='task')


router.register('PhaseAPI',views.PhaseViewSet, basename='Phase')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('id/', include('api.urls')),
    path('api-auth/',include('rest_framework.urls')),
    
]
