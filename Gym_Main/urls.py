
from django.contrib import admin
from django.urls import re_path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from app import views


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.login, name='login'),
    re_path(r'^Trainer_index/$', views.Trainer_index, name='Trainer_index'),
    re_path(r'^Trainer_dashboard/$',views.Trainer_dashboard,name='Trainer_dashboard'),
    re_path(r'^Trainer_Trainees_card/$', views.Trainer_Trainees_card, name='Trainer_Trainees_card'),
    re_path(r'^Trainer_Current_Trainees_table/$', views.Trainer_Current_Trainees_table, name='Trainer_Current_Trainees_table'),
    re_path(r'^Trainer_Current_Trainees_profile/(?P<id>\d+)/$', views.Trainer_Current_Trainees_profile, name='Trainer_Current_Trainees_profile'),
    re_path(r'^Trainer_Previous_Trainees_table/$', views.Trainer_Previous_Trainees_table, name='Trainer_Previous_Trainees_table'),
    re_path(r'^Trainer_Previous_Trainees_profile/(?P<id>\d+)/$', views.Trainer_Previous_Trainees_profile, name='Trainer_Previous_Trainees_profile'),
    re_path(r'^Trainer_Accsetting/$',views.Trainer_Accsetting,name='Trainer_Accsetting'),
    re_path(r'^Trainer_Profile_Imagechange/(?P<id>\d+)/$',views.Trainer_Profile_Imagechange,name='Trainer_Profile_Imagechange'),
    re_path(r'^Trainer_Changepwd/(?P<id>\d+)/$',views.Trainer_Changepwd,name='Trainer_Changepwd'),
    re_path(r'^SuperAdmin_Accountsett/$',views.SuperAdmin_Accountsett,name='SuperAdmin_Accountsett'),
    re_path(r'^Trainee_Accsetting/$',views.Trainee_Accsetting,name='Trainee_Accsetting'),
    re_path(r'^Trainee_index/$',views.Trainee_index,name='Trainee_index'),
    re_path(r'^SuperAdmin_index/$', views.SuperAdmin_index, name='SuperAdmin_index'),
    re_path(r'^SuperAdmin_logout/$', views.SuperAdmin_logout, name='SuperAdmin_logout'),
    re_path(r'^Trainee_logout/$', views.Trainee_logout, name='Trainee_logout'),
    re_path(r'^Trainee_Profile_Imagechange/(?P<id>\d+)/$',views.Trainee_Profile_Imagechange,name='Trainee_Profile_Imagechange'),
    re_path(r'^Trainee_Changepwd/(?P<id>\d+)/$',views.Trainee_Changepwd,name='Trainee_Changepwd'),
    re_path(r'^Registration/$',views.Registration,name='Registration'),
    re_path(r'^Trainer_logout/$',views.Trainer_logout,name='Trainer_logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
