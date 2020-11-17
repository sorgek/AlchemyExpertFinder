from django.urls import path
from . import views

app_name = "expertFinder"

urlpatterns = [
    path("", views.index, name="search"),
    path("<int:pk>/", views.display_expert, name="display_expert"),
    path("search_results", views.search_results, name='search_results'),
    path("add", views.AddExpert.as_view(), name='add'),
    path("edit/<int:pk>", views.edit, name='edit'),
]
handler400 = 'expertFinder.error_handlers.bad_request'
