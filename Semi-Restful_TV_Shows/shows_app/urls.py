from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.shows),
    path('shows/new', views.new_show),
    path('shows/create', views.create),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>', views.show_profile),
    path('shows/<int:id>/update', views.update),
    path('shows/<int:id>/delete', views.destroy),
    
]