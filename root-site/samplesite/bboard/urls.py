from django.urls import path
from .views import index, rubric_bbs, BdCreateView

urlpatterns = [
    path('add/', BdCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', rubric_bbs, name='rubric_bbs'),
    path('', index, name='index'),
]
