from . import views
from django.urls import path

urlpatterns = [
    path('createbuilding/', views.create_building, name='create-elevator'),
    path('createelevator', views.create_elevator, name='elevator'),
    path('request/', views.request_elevator, name='request-elevator'),
    path('press/', views.press_button, name='press-button'),
    path('getelevator/', views.get_elevator, name='get-elevator'),
    path('getrequests/', views.get_requests, name='get-requests'),
    path('getmanager/', views.get_elevator_manager, name='get-manager'),
    path('status/', views.get_status, name='get-status')

]
