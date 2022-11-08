from django.urls import path
from.views import RegisterView, FirmRegisterView


urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("firm_register/", FirmRegisterView.as_view()),
]