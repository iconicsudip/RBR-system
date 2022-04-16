from django.contrib import admin
from django.urls import path
from rmmain import views

urlpatterns = [
    path('', views.home,name='home'),
    path('addroomtype', views.addroomtype,name='addroomtype'),
    path('addroom', views.addroom,name='addroom'),
    path('search', views.search,name='search'),
    path('bookroom/<str:user>/<int:id>/<str:day>/<str:year>', views.bookroom,name='bookroom'),
    path('bookroom/<str:user>/<int:id>', views.bookroom,name='bookroom'),
    path('bookings', views.bookings,name='bookings'),
    path('customer_bookings', views.customer_bookings,name='customer_bookings'),
    path('check/<int:id>', views.check,name='check'),
    path('slotrange', views.slotrange,name='slotrange'),
    path('roomdelete/<int:id>', views.roomdelete,name='roomdelete'),
    path('bookdelete/<int:id>', views.bookdelete,name='bookdelete'),
    path('cancelbook', views.cancelbook,name='cancelbook'),
    path('cancelslot', views.cancelslot,name='cancelslot'),
    path('roomedit/<str:user>/<int:id>', views.roomedit,name='roomedit'),
    path('addlocation', views.addlocation,name='addlocation'),
    path('customer_login', views.customer_login,name='customer_login'),
    path('manager_login', views.manager_login,name='manager_login'),
    path('customer_register', views.customer_register,name='customer_register'),
    path('manager_register', views.manager_register,name='manager_register'),
    path('customer_dashboard/<str:user>/', views.customer_dashboard,name='customer_dashboard'),
    path('manager_dashboard/<str:user>/', views.manager_dashboard,name='manager_dashboard'),
    path('logout', views.logout,name='logout'),
]
