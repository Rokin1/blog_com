from django.urls import path
from . views import blog, index, post, search
app_name = 'blog'

urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('post/<id>/', post, name="end-detail"),
    path('search/', search, name='search'),

]
