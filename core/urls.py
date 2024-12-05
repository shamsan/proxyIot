# proxy/urls.py
from django.urls import path
from .views import GenerateVerificationCodeView, StoreHostDataView #, RetrieveHostDataView

urlpatterns = [
    path('connect-box/', GenerateVerificationCodeView.as_view(), name='connect-box'),
    path('connect-db/', StoreHostDataView.as_view(), name='connect-db'),
]