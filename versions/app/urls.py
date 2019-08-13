from django.conf.urls import url


from app import views

urlpatterns = [
  url('^$', views.index, name='index'),
  url('^versions/', views.show_app_version, name='versions'),

]


