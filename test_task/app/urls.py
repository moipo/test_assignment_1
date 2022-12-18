from django.urls import path
from .views import *
from .api import *

urlpatterns = [

    #populate database
    path("populate_shops", Main.populate_shops, name = "populate_shops"),
    path('populate_products', Main.populate_products, name = "populate_products"),

    #api
    path('api/v1/programs/page/<int:page_num>',ProgramAPIView.as_view(),name = "get_program_page"  ),
    path('api/v1/categories/all',CategoryAPIView.as_view(), name = "get_categories_all"),
    path('api/v1/categories/<int:pk>',CategoryAPIView.as_view(), name = "get_categories"),
    path('api/v1/categories/page/<int:page_num>',CategorySecondAPIView.as_view(), name = "get_categories_page"),


    #views
    path('', Main.homepage, name = "homepage"),
    path('login_view', Main.login_view, name = "login_view"),
    path('homepage', Main.homepage, name = "homepage"),
    path('api_test', Main.api_test, name = "api_test"),
    path('rest_service', Main.rest_service, name = "rest_service"),
    path('custom_admin', Main.custom_admin, name = "custom_admin"),
    path('rest_categories', Main.rest_categories, name = "rest_categories"),
    path('search', Main.search, name = "search"),
    path('search/<int:page_num>/<str:search_string_pag>', Main.search, name = "search"),
    path('edit_category/<int:pk>', Main.edit_category, name = "edit_category"),

]
