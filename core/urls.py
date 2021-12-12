from django.urls import path
from .views import IndexView, MoveisView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('moveis', MoveisView.as_view(), name='moveis')
]


