from django.urls import path
from floors import views as floor_views
from . import views

urlpatterns = [
    path("parking-lots/", views.ParkingLotView.as_view()),
    path("parking-lots/<int:parking_lot_id>/", views.ParkingLotDetailView.as_view()),
    path("parking-lots/<int:parking_lot_id>/floors/", floor_views.FloorView.as_view()),
]
