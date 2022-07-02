from django.urls import path

# from . import views # alt method of writing line below
from .views import index, new, create, show, edit, destroy

urlpatterns = [
    # path('admin/', admin.site.urls),

        # path('', views.index), # alt method of writing line below
    path('', index), # = "/"
    path('new', new), # "/new"
    path('create', create), # "/create"
    path('<int:number>', show), # "/number"
    path('<int:number>/edit', edit), # "/number/edit"
    path('<int:number>/delete', destroy), # "/number/delete"
]