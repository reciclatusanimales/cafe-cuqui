from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls', namespace='about')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('', include('home.urls', namespace='home')),
    path('meals/', include('meals.urls', namespace='meals')),
    path('reserve_table/', include('reservation.urls', namespace='reservation')),

    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Restaurant Admin Panel"
admin.site.site_title = "Restaurant App Admin"
admin.site.site_index_title = "Welcome to Restaurant Admin Panel"