from django.urls import path
from .views import *


app_name = 'socproject'
urlpatterns = [
    path('', BulletinsListView.as_view(), name='bulletins'),
    path('<int:pk>', BulletinDetailView.as_view(), name='bulletin'),
    path('create', BulletinCreateView.as_view(), name='bulletincreate'),
    path('<int:pk>/edit', BulletinEditView.as_view(), name='bulletinedit'),
    path('<int:pk>/delete', BulletinDeleteView.as_view(), name='bulletindelete'),
    path('showresponses', ResponsesListView.as_view(), name='showresponses'),
    path('respcreate/<int:pk>', ResponseCreateView.as_view(), name='respcreate'),
    path('acceptresponse/<int:pk>', acceptresponse, name='acceptresponse'),
    path('rejectresponse/<int:pk>', rejectresponse, name='rejectresponse')
]

