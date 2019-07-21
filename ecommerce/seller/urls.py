from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'seller'
urlpatterns = [
    url(r'^$',auth_views.LoginView.as_view(template_name='seller/seller_login.html'),
                                        name='login'),
    url(r'^signup/$',views.SellerProfileCreateView.as_view(),name='signup'),
    url(r'^login/$', views.SellerLoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(
        r'^(?P<username>[-\w]{5,30})/$',
        views.DetailAccountView.as_view(),
        name='profile'
    ),
]
