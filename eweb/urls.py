"""
URL configuration for eweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ewebApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("base/",views.base),
    path("ba/",views.ba),
    path("customer/",views.customer),
    path("customerreg/",views.customerreg),
    path("order/",views.order),
    path("contact/",views.contact),
    path("service/",views.service),
    path("manreg/",views.manreg),
    path("manager/",views.manager),
    path("viewmanager/",views.viewmanager),
    path("empreg/",views.empreg),
    path("employee/",views.employee),
    path("viewemployee/",views.viewemployee),
    path("login/",views.login),
    path("adminHome/",views.adminHome),
    path("vieworder/",views.vieworder),
    path("updel/",views.updel),
    path("update/",views.update),
    path("delete/",views.delete),
    path("emplist/",views.emplist),
    path("orderlist/",views.orderlist),
    path("status/",views.status),
    path("active/",views.active),
    path("complete/",views.complete),
    path("pricelist/",views.pricelist),
]
