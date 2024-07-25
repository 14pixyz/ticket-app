from django.urls import path
from .views import supporter_event_list, supporter_feature,customuser

# 画像用
from django.conf import settings
from django.conf.urls.static import static


app_name = 'ticket'

urlpatterns = [
    path('supporter/home/', supporter_feature.HomeView.as_view(), name='supporter-home'),

    # イベント管理
    path('supporter/event-list/', supporter_event_list.EventListView.as_view(), name='supporter-event-list'),
    path('supporter/event-create/', supporter_event_list.EventCreateView.as_view(), name='supporter-event-create'),
    path('supporter/customuser-delete/<int:pk>/', supporter_event_list.EventDeleteView.as_view(), name='supporter-event-delete'),
    path('supporter/customuser-update/<int:pk>/', supporter_event_list.EventUpdateView.as_view(), name='supporter-event-update'),

    # サポーター管理
    path('supporter/customuser-list/', customuser.CustomUserListView.as_view(), name='supporter-customuser-list'),
    path('supporter/customuser-create/', customuser.CustomUserCreateView.as_view(), name='supporter-customuser-create'),
    path('supporter/customuser-delete/<int:pk>/', customuser.CustomUserDeleteView.as_view(), name='supporter-customuser-delete'),
    path('supporter/customuser-update/<int:pk>/', customuser.CustomUserUpdateView.as_view(), name='supporter-customuser-update'),

    # ログイン・ログアウト
    path('supporter/login/',supporter_feature.SupporterLoginView.as_view(),name='supporter-login'),
    path('supporter/logout/',supporter_feature.SupporterLogoutView.as_view(),name='supporter-logout'),
]

# 画像用
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
