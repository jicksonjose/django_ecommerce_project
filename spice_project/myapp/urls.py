from django.contrib.auth import admin
from django.urls import path
from . import views

import authentication. views
urlpatterns = [


    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('base', views.base, name="base"),
    path('login', views.login, name="login"),
    path('sign_up', views.sign_up, name="signup"),
    path('product_page', views.product_page, name="product_page"),
    path('user_search_item_view', views.user_search_item_view, name="user_search_item_view"),

    path('search', views.autocomplete, name="autocomplete"),


    path('user_home', views.user_home, name="user_home"),
    path('logout', views.logout, name="logout"),
    path('user_product_page', views.user_product_page, name="user_product_page"),
    path('category_item', views.category_item, name="category_item"),
    path('all_review', views.all_review, name='all_review'),

    path('addtocart',views.addtocart, name="addtocart"),
    path('add_to_wishlist', views.add_to_wishlist, name="add_to_wishlist"),
    path('wishlist', views.wishlist_view, name="wishlist"),
    path('delete_wishlist', views.delete_wishlist, name="delete_wishlist"),
    path('my-cart',views.mycart, name='my-cart'),

    path('contact', views.contact_supporting, name="contact"),
    path('non_user_contact', views.non_contact, name="contact"),
    path('non_user_about', views.non_about, name="contact"),
    path('base_category', views.base_category , name="base_category"),


    path('managecart/<int:id>/', views.managecart, name="managecart"),
    path("empty-cart/", views.emptycart),
    path("checkout", views.checkout),
    path("checkout_session", views.checkout_session, name="checkout_session"),
    path('pay_success', views.pay_success, name="pay_success"),
    path('pay_cancel', views.pay_cancel, name="pay_cancel"),
    path('user_order_status', views.user_order_status, name="user_order_status"),
    path('confirm_payment', views.confirm_payment, name="confirm_payment"),

    path('user_profile', views.user_profile, name="user_profile"),
    path('user_address_view', views.user_address_view, name="user_address_view"),
    path('user_address_edit', views.user_address_edit, name="user_address_edit"),

    path('cancel_order', views.cancel_order, name="cancel_order"),
    path('user_login_details_view', views.user_login_details_view, name="user_login_details_view"),
    path('user_change_email', views.user_change_email, name="user_change_email"),
    path('user_change_password',views.user_change_password, name="user_change_password"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    #
    # path('https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?client_id=65474074056-3aj3vnsbogv9ql1oq4ro5t797vn1dnjt.apps.googleusercontent.com&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Faccounts%2Fgoogle%2Flogin%2Fcallback%2F&scope=profile&response_type=code&state=TV0ADmd3IEmf&service=lso&o2v=2&flowName=GeneralOAuthFlow',
    #      views.google_auth_callback, name='google_auth_callback'),
    path('google_login',  views.google_auth_callback, name='google_auth_callback'),

    path('invoice', views.invoice, name="invoice"),
]


