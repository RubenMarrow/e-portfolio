from django.urls import path

from .views import home_page_view, about_page_view, contact_page_view, proj_page_view, exp_page_view

urlpatterns = [
    path("about/", about_page_view.as_view(), name="about"),
    path("", home_page_view.as_view(), name="home"),
    path("contact/", contact_page_view.as_view(), name="contact"),
    path("projects/", proj_page_view.as_view(), name="proj"),
    path("experience/", exp_page_view.as_view(), name="exp"),
]