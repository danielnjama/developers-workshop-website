from django.contrib import admin
from django.urls import path,include

admin.site.site_header="Dynamic Technologies Workshop"
admin.site.site_title="Dynamic Technologies Workshop"
admin.site.index_title="Dtech Workshop ADMIN"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
