from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='ng.html'), name='home'), # 2.0 re_path, path
    url(r'^admin/', admin.site.urls),
    # url(r'^api/$', TemplateView.as_view(template_name='api-home.html'), name='home'),
    url(r'^api/', include_docs_urls(title='Dj Ionic APIs')),
    url(r'^api/auth/', include('accounts.api.urls', namespace='api-auth')),
    url(r'^api/user/', include('accounts.api.user.urls', namespace='api-user')),
    url(r'^api/status/', include('status.api.urls', namespace='api-status')),
    # url(r'^api/updates/', include('updates.api.urls')), 
]
