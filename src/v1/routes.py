from django.urls import path, include

urlpatterns = [
    path('user/', include('src.v1.user.urls')),
]
