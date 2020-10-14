from django.urls import path
from .views import RegisterUser, CategoriesView, ServicesView, FollowingServicesView

urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('services-list/', ServicesView.as_view()),
    path('following-services/', FollowingServicesView.as_view()),
]