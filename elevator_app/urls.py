from django.contrib import admin
from django.urls import path,include

from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'building_', BuildingView)
router.register(r'elevator_', ElevatorView)
building_list = BuildingView.as_view({
    'get': 'list',
    'post': 'create'
})
building_detail = BuildingView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
Elevator_list = ElevatorView.as_view({
    'get': 'list',
    'post': 'create'
})
Elevator_detail = ElevatorView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns=[
    path('buildings/', building_list, name='building-list'),
    path('buildings/<int:pk>/', building_detail, name='building-detail'),
    path('elevator/', Elevator_list, name='elevator-list'),
    path('elevator/<int:pk>/', Elevator_detail, name='elevator-detail'),
    path('request_of_elivator/',ElevatorRequestView.as_view()),
    path('ElevatorStaus',ElevatorStatus.as_view())
]