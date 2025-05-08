from django.urls import path
from blog.views import category_view,about_view,contact_view,home_view,single_post_view

urlpatterns=[
    path("category/" ,category_view),
    path("about/" ,about_view),
    path("contact/" ,contact_view),
    path("home/" ,home_view),
    path("single_post/" ,single_post_view),
   
    
]