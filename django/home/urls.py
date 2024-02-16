from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    # dashboard
    path('dashboard-title/', views.dashboard_title, name='dashboard_title'),
    path('dashboard-status-pie-chart/', views.dashboard_status_pie_chart, name='dashboard_status_pie_chart'),
    path('dashboard-tenure-pie-chart/', views.dashboard_tenure_pie_chart, name='dashboard_tenure_pie_chart'),
    path('dashboard-land-title-pie-chart/', views.dashboard_land_title_pie_chart, name='dashboard_land_title_pie_chart'),
    path('dashboard-pie-chart-description/', views.dashboard_pie_chart_description, name='dashboard_pie_chart_description'),
    path('dashboard-property-type-bar-chart/', views.dashboard_property_type_bar_chart, name='dashboard_property_type_bar_chart'),
    path('dashboard-state-bar-chart/', views.dashboard_state_bar_chart, name='dashboard_state_bar_chart'),
    path('dashboard-city-bar-chart/', views.dashboard_city_bar_chart, name='dashboard_city_bar_chart'),
    path('dashboard-bar-chart-description/', views.dashboard_bar_chart_description, name='dashboard_bar_chart_description'),
    path('dashboard-price-box-plot/', views.dashboard_price_box_plot, name='dashboard_price_box_plot'),
    path('dashboard-price-hist-plot/', views.dashboard_price_hist_plot, name='dashboard_price_hist_plot'),
    path('dashboard-price-plot-description/', views.dashboard_price_plot_description, name='dashboard_price_plot_description'),
    path('dashboard-price-state-box-plot/', views.dashboard_price_state_box_plot, name='dashboard_price_state_box_plot'),
    path('dashboard-price-land-title-box-plot/', views.dashboard_price_land_title_box_plot, name='dashboard_price_land_title_box_plot'),
    path('dashboard-price-tenure-box-plot/', views.dashboard_price_tenure_box_plot, name='dashboard_price_tenure_box_plot'),
    path('dashboard-price-category-plot-description/', views.dashboard_price_category_plot_description, name='dashboard_price_category_plot_description'),
    path('dashboard-price-state-scatter-plot/', views.dashboard_price_state_scatter_plot, name='dashboard_price_state_scatter_plot'),
    path('dashboard-price-land-title-scatter-plot/', views.dashboard_price_land_title_scatter_plot, name='dashboard_price_land_title_scatter_plot'),
    path('dashboard-price-tenure-scatter-plot/', views.dashboard_price_tenure_scatter_plot, name='dashboard_price_tenure_scatter_plot'),
    path('dashboard-price-scatter-plot-description/', views.dashboard_price_scatter_plot_description, name='dashboard_price_scatter_plot_description'),

    # word cloud
    path('word-cloud/', views.word_cloud, name='word_cloud'),
    #path('typography/', views.typography, name='typography'),
    #path('color/', views.color, name='color'),
    #path('icon-tabler/', views.icon_tabler, name='icon_tabler'),
    #path('sample-page/', views.sample_page, name='sample_page'),

    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.user_logout_view, name='logout'),
    path('accounts/register/', views.registration, name='register'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done" ),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]
