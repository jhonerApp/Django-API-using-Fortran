"""
URL configuration for fortran_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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


from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)
from django.contrib import admin
from django.urls import path,include,reverse
from drf_spectacular.renderers import OpenApiJsonRenderer


class InlineSpectacularAPIView(SpectacularAPIView):
    renderer_classes = [OpenApiJsonRenderer]
    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)

        # force inline JSON display
        response['Content-Type'] = 'application/json; charset=utf-8'
        response['Content-Disposition'] = 'inline'
        return response

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('swagger/schema/', BrowserFriendlySpectacularAPIView.as_view(), name='api-schema'),#
    path('swagger/v1/swagger.json', InlineSpectacularAPIView.as_view(), name='api-schema'),

    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    path('computation/', include('fortran_api.urls'))
]
