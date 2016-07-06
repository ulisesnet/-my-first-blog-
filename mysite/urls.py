from django.conf.urls import include, url
#from django.contrib import admin
from blog import views
#from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#url(r'^admin/', include(admin.site.urls)),
#url(r'', include('blogs.urls')),
url(r'^$', views.post_list),
url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
]
