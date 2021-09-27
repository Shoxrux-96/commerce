from django.urls import path
from .views import HomePageView, PostDetailView,ProductPage,AboutPage,ContactPage,PostDetailView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('watches/',ProductPage.as_view(),name='watches'),
    path('about/',AboutPage.as_view(),name='about'),
    path('contact/',ContactPage.as_view(),name='contact'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail')
]