from django.conf.urls import url
from StudentApp.views import *

urlpatterns = [
    url('add-student/',addStudent),
    url('add/',add),
    url('view-student/',viewStudent),
    url('edit-preview/',editView),
    url('edit-student/',editStudent),
    url('edit/',edit),
    url('delete-preview/',deleteView),
    url('delete-student/',deleteStudent),

    url('search-student/',Search),
]