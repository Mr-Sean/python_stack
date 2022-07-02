from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # index is a variable. can be called anything.
    path('helloWorld', views.helloWorld),
    path('hello/<str:name>', views.heydude),
    path('krustykrab', views.krustykrab),
    path('submission', views.submission),
    path('thanks', views.thanks),
    path('<url>', views.catch_all), # catch_all route must always be last line executed.
]