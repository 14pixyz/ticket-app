from django.urls import path
from .views import supporter_customuser, supporter_event, supporter_function, supporter_ticket

# 画像用
from django.conf import settings
from django.conf.urls.static import static


app_name = 'ticket'

urlpatterns = [
    path('supporter/home/', supporter_function.HomeView.as_view(), name='supporter-home'),

    # イベント管理
    path('supporter/event-list/', supporter_event.EventListView.as_view(), name='supporter-event-list'),
    path('supporter/event-create/', supporter_event.EventCreateView.as_view(), name='supporter-event-create'),
    path('supporter/event-delete/<int:pk>/', supporter_event.EventDeleteView.as_view(), name='supporter-event-delete'),
    path('supporter/event-update/<int:pk>/', supporter_event.EventUpdateView.as_view(), name='supporter-event-update'),

    # サポーター管理
    path('supporter/customuser-list/', supporter_customuser.CustomUserListView.as_view(), name='supporter-customuser-list'),
    path('supporter/customuser-create/', supporter_customuser.CustomUserCreateView.as_view(), name='supporter-customuser-create'),
    path('supporter/customuser-delete/<int:pk>/', supporter_customuser.CustomUserDeleteView.as_view(), name='supporter-customuser-delete'),
    path('supporter/customuser-update/<int:pk>/', supporter_customuser.CustomUserUpdateView.as_view(), name='supporter-customuser-update'),

    # チケット管理
    path('supporter/ticket-list/', supporter_ticket.TicketListView.as_view(), name='supporter-ticket-list'),
    path('supporter/ticket-create/', supporter_ticket.TicketCreateView.as_view(), name='supporter-ticket-create'),
    path('supporter/ticket-delete/<int:pk>/', supporter_ticket.TicketDeleteView.as_view(), name='supporter-ticket-delete'),
    path('supporter/ticket-update/<int:pk>/', supporter_ticket.TicketUpdateView.as_view(), name='supporter-ticket-update'),

    # ログイン・ログアウト
    path('supporter/signup/',supporter_function.signup,name='supporter-signup'),
    path('supporter/login/',supporter_function.SupporterLoginView.as_view(),name='supporter-login'),
    path('supporter/logout/',supporter_function.SupporterLogoutView.as_view(),name='supporter-logout'),
]

# 画像用
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
