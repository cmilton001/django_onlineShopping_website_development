from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import cart.views
import orders.views
import payment.views
import shop.views
import coupons.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', cart.views.cart_add, name='cart'),
    url(r'^orders/', orders.views.order_create, name='orders'),
    url(r'^payment/', payment.views.payment_done, name='payment'),
    url(r'^', shop.views.product_list, name='shop'),
    url(r'^coupons/', coupons.views.coupon_apply, name='coupons'),
    #url(r'^paypal/', 'paypal.standard.ipn.urls'),

]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT )
