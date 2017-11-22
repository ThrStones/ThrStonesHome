"""readnovel URL Configuration
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
        # novel list
    url(r'^cards/$', views.cards, name='cards'),

]
