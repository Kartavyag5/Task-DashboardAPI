from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('TaskAPI',views.TaskAPIViewSet, basename='task')

router.register('TagAPI',views.TagAPIViewset, basename='tag')
router.register('TaskInPhaseAPI',views.TaskInPhaseViewset, basename='phase')
router.register('TaskInPhaseAPI/1',views.TaskInPhaseViewset, basename='phaseTask')
router.register('TaskInPhaseAPI2',views.TaskInPhaseViewset2, basename='phaseTask2')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('api/', include('api.urls')),
    path('api-auth/',include('rest_framework.urls')),
    
]
