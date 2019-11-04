from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.index,name = 'index'),
   
    url(r'^project_posts/', views.project_posts, name='project_posts'),
    url(r'^viewProject_details/', views.viewProject_details, name='viewProject_details'),
    url(r'^new_post/',views.new_post,name='new_post'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^update_profile/',views.update_profile,name = 'update_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)