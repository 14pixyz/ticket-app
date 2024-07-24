from django.urls import path
from .views import supporter_event_list, supporter_feature,customuser


app_name = 'ticket'

urlpatterns = [
    path('supporter/home/', supporter_feature.HomeView.as_view(), name='supporter-home'),

    # イベント管理
    path('supporter/event-list/', supporter_event_list.EventlistView.as_view(), name='supporter-event-list'),

    # サポーター管理
    path('supporter/customuser-list/', customuser.CustomUserListView.as_view(), name='supporter-customuser-list'),
    path('supporter/customuser-create/', customuser.CustomUserCreateView.as_view(), name='supporter-customuser-create'),
    path('supporter/customuser-delete/<int:pk>/', customuser.CustomUserDeleteView.as_view(), name='supporter-customuser-delete'),
    path('supporter/customuser-update/<int:pk>/', customuser.CustomUserUpdateView.as_view(), name='supporter-customuser-update'),

    # ログイン・ログアウト
    path('supporter/login/',supporter_feature.SupporterLoginView.as_view(),name='supporter-login'),
    path('supporter/logout/',supporter_feature.SupporterLogoutView.as_view(),name='supporter-logout'),
]

