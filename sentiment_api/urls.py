from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from analyser.api import router as sentiment_router

api = NinjaAPI()
api.add_router("/sentiment/", sentiment_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
