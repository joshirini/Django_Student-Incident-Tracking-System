from django.conf.urls import url
from django.contrib import admin
from ed4all import views

urlpatterns = [
    url(r'^$', views.home, name="home"),

    # =========== student login ===========
    url(r'^student_home', views.student_home, name='student_home'),
    url(r'^student_view_detail', views.student_view_detail, name='student_view_detail'),
    url(r'^student_view_incident', views.student_view_incident, name='student_view_incident'),

    # =========== educator login ===========
    url(r'^educator_home', views.educator_home, name='educator_home'),
    url(r'^educator_create_incident', views.educator_create_incident, name='educator_create_incident'),
    url(r'^educator_student_list', views.educator_student_list, name='educator_student_list'),
    url(r'^educator_incident_list', views.educator_incident_list, name='educator_incident_list'),
    url(r'^educator_student_view/(?P<pk>[\w-]+)$', views.educator_student_view, name='educator_student_view'),

    # =========== counselor login ===========
    url(r'^counselor_home', views.counselor_home, name='counselor_home'),
    url(r'^student_list', views.student_list, name='student_list'),
    url(r'^student_view/(?P<pk>[\w-]+)$', views.student_view, name='student_view'),
    url(r'^incident_form', views.incident_create, name='incident_create'),
    url(r'^incident_list', views.incident_list, name='incident_list'),
    url(r'^incident_view/(?P<pk>[\w-]+)/$', views.incident_view, name='incident_view'),
    url(r'^incident_edit/(?P<pk>[\w-]+)/$', views.incident_edit, name='incident_edit'),
    url(r'^incident_delete/(?P<pk>[\w-]+)$', views.incident_delete, name='incident_delete'),

]
