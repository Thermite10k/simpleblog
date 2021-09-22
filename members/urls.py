from django.urls import path
#from django.contrib.auth import views as auth_views
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from . import views
urlpatterns = [
	
	path('register/', UserRegisterView.as_view(), name='register'),
	path('login_user', views.login_user, name='login2'),
	path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
	#path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
	path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
	path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile_page'),
	path('<int:pk>/edit_profile', EditProfilePageView.as_view(), name='edit_profile_page'),
	path('create_profile_page', CreateProfilePageView.as_view(), name='create_profile_page'),
]
