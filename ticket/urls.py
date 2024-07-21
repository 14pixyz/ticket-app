from django.urls import path
from .views import supporter_event_list, supporter_feature,customuser


app_name = 'ticket'

urlpatterns = [
    path('supporter/home/', supporter_feature.HomeView.as_view(), name='supporter-home'),

    path('supporter/event-list/', supporter_event_list.EventlistView.as_view(), name='supporter-event-list'),
    path('supporter/customuser-list/', customuser.CustomUserListView.as_view(), name='supporter-customuser-list'),
    path('supporter/customuser-create/', customuser.CustomUserCreateView.as_view(), name='supporter-customuser-create'),

    # ログイン・ログアウト
    path('supporter/login/',supporter_feature.SupporterLoginView.as_view(),name='supporter-login'),
    path('supporter/logout/',supporter_feature.SupporterLogoutView.as_view(),name='supporter-logout'),
]

