from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = 'home'),
    path('login/', log_in, name = 'login'),
    path('signup/', sign_up, name = 'signup'),
    path('logout/', log_out, name = 'logout'),
    path('check-username/', check_username, name="check"),
    path('post/', createPost ,name = 'createPost'),
    path('profile/', profile, name = "profile"),

]
