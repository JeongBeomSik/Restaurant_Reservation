
from django.contrib import admin
from django.urls import path, include
import base.views
import createboard.views

urlpatterns = [
    path('readboard/', createboard.views.readboard, name="readboard"),
    path('readReservation/', createboard.views.readReservation, name="readReservation"),
    path('post/',createboard.views.post, name="post"),
    path('postReservation/',createboard.views.postReservation, name="postReservation"),
    path('search/',createboard.views.search, name="search"),
    path('searchReservation/',createboard.views.searchReservation, name="searchReservation"),
    path('post/<int:img_board_id>/',createboard.views.detail,name="detail"),
    path('postReservation/<int:board_id>/',createboard.views.detailReservation,name="detailReservation"),
    path('delete/<int:pk>/',createboard.views.delete, name="delete"),
    path('deleteReservation/<int:pk>/',createboard.views.deleteReservation, name="deleteReservation"),
    path('update/<int:pk>/',createboard.views.update, name="update"),
    path('updateReservation/<int:pk>/',createboard.views.updateReservation, name="updateReservation")
]
