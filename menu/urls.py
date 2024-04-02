from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # URL for displaying the menu page
    path('', views.menu_page, name='menu_page'),

    # URL for editing a specific menu item by its ID
    path('edit/<int:menu_item_id>',
         views.edit_menu_item, name='edit_menu_item'),

    # URL for adding a new menu item
    path('add/', views.add_menu_item, name='add_menu_item'),

    # URL for deleting a specific menu item by its ID
    path('delete/<int:menu_item_id>',
         views.delete_menu_item, name='delete_menu_item'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
