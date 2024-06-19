
from django.contrib import admin
from django.urls import path
from torts.views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from users.views import *
urlpatterns = [


    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('table', table, name='table'),
    path('torts/<int:id>/', torts, name = 'torts'),
    path('torts_1/<int:id>/',torts_1,name='torts_1'),
    path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('<int:cake_id>/delete/', delete_cake, name='delete_cake'),
    path('update/<int:id>/',profile_update,name='profile_update'),
    path('zakaz/', zakaz, name='zakaz'),
    path('<int:cake_id>/delete_zakaz/', delete_zakaz, name='delete_zakaz'),
    path('update_zakaz/<int:id>/', zakaz_update, name='zakaz_update'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
