from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from notebookapi.views import register_user, login_user
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from notebookapi.views import NoteView, NoteTakerView, TasksView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'notes', NoteView, 'note')
router.register(r'notetakers', NoteTakerView, 'notetaker')
router.register(r'tasks', TasksView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('register', register_user),
    path('', include(router.urls))
] 