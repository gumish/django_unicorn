from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
TemplateView




urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name='nested.html')),
    # Include django-unicorn urls
    path("unicorn/", include("django_unicorn.urls")),
]
