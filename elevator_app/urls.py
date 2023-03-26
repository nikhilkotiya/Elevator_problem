from django.contrib import admin
from django.urls import path,include

from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'elevator_system', ElevatorSystemList)
router.register(r'elevator_', Elevator_)
building_list = ElevatorSystemList.as_view({
    'get': 'list',
    'post': 'create'
})
building_detail = ElevatorSystemList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
Elevator_list = Elevator_.as_view({
    'get': 'list',
    'post': 'create'
})
Elevator_detail = Elevator_.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns=[
    path('buildings/', building_list, name='building-list'),
    path('buildings/<int:pk>/', building_detail, name='building-detail'),
    path('building/elevator_/', Elevator_list, name='elevator-list'),
    path('elevator_/<int:pk>/', Elevator_detail, name='elevator-detail'),
    path('request_of_elivator',ElevatorRequestView.as_view())
]