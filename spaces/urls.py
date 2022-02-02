from django.urls import path

from .views import CreateSpace, ListSpaces, DeleteSpace


urlpatterns = [
    path("spaces/<int:user_id>", ListSpaces.as_view(), name="list_spaces"),
    path("create_space", CreateSpace.as_view(), name="create_space"),
    path("delete_space/<int:space_id>", DeleteSpace.as_view(), name="delete_space"),
]
