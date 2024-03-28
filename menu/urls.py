from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.menu_page, name='menu_page'),
    path('edit/<int:menu_item_id>', views.edit_menu_item, name='edit_menu_item'),
    path('add/', views.add_menu_item, name='add_menu_item'),
    path('delete/', views.delete_menu_item, name='delete_menu_item'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)