from django.urls import path
from .views import homePageView, HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about")
]
