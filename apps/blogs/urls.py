from django.conf.urls import url, patterns
from django.views.generic import TemplateView


urlpatterns = patterns(
    'blogs.views',
    url(r'^oauth2callback$', 'oauth2callback', name='blogs_oauth2callback'),
    url(r'^login$', TemplateView.as_view(
        template_name='blogs/google.html'
    )),
)