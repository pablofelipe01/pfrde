from django.urls import path
from . import views

urlpatterns = [
    path('pferde/', views.PferdList.as_view(), name="pferd_list"),
    path('pferde/<int:pk>', views.PferdDetail.as_view(), name="pferd_detail")
]
