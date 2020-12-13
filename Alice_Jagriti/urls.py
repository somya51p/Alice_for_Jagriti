from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from notes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', userlogin, name='login'),
    path('signup/', signup1, name='signup'),
    path('logout/', Logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('upload_notes/', upload_notes, name='upload_notes'),
    path('view_mynotes/', view_mynotes, name='view_mynotes'),
    path('login_admin/', login_admin, name='login_admin'),
    path('admin_home/', admin_home, name='admin_home'),
    path('', index, name='index'),
    path('delete_mynotes/<int:pid>', delete_mynotes, name='delete_mynotes'),
    path('Book/', include('Book.urls')),
    path('quiz/', include('quiz.urls'))

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
