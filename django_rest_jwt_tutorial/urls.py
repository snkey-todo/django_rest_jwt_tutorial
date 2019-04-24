"""django_rest_swagger_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from musics.views import MusicViewSet
# rest router
from rest_framework.routers import DefaultRouter
# swagger
from rest_framework_swagger.views import get_swagger_view
# jwt
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

router = DefaultRouter()
router.register('music', MusicViewSet, base_name='music')

schema_view = get_swagger_view(title='API')

urlpatterns = [
    path('docs/', schema_view), # swagger API文档
    path('admin/', admin.site.urls),    # admin模块
    path('api/', include(router.urls)), # 访问rest api
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]
