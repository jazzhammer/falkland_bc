"""
URL configuration for falkland_bc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('inventory_item/', InventoryItemView.as_view()),
    path('inventory_status', InventoryStatusView.as_view()),
    path('inventory_status_assign', InventoryStatusAssignView.as_view()),
    path('inventory_location', InventoryLocationView.as_view()),
    path('inventory_location_assign', InventoryLocationAssignView.as_view()),
    path('donor_person', DonorPersonView.as_view())
]
