from .views import IndexView, LoginView, LogoutView
from common.reports_views import DailyReports, WeeklyRreports, MonthlyReports
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('daily/report', DailyReports.as_view(), name='daily_report'),
    path('weekly/report', WeeklyRreports.as_view(), name='weekly_report'),
    path('monthly/report', MonthlyReports.as_view(), name='monthly_report'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
