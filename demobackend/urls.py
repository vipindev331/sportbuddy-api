"""demobackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url,include
# from django.contrib import admin
# from rest_framework import routers
from Learning.views import TodoView
from django.conf import settings  
from django.conf.urls.static import static  

# from django.urls import include, re_path
from django.contrib import admin
from Learning.views import *
from django.urls import path
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
# urlpatterns = router.urls
# router.register(r'tasks',TodoView)
# router.register(r'^admin', admin.site.urls,basename='model1')
# router.register('api/',urlpatterns,basename='model2')
router.register(r'tasks',TodoView)
urlpatterns = [
    path('admin/', admin.site.urls),

    # add another path to the url patterns
    # when you visit the localhost:8000/api
    # you should be routed to the django Rest framework
    # path('api/tasks/', TodoView.as_view()),
    path('api/', include(router.urls)),
]


# urlpatterns += router.urls



# # create a router object
# router = routers.SimpleRouter()
 
# # register the router
# router.register(r'tasks',TodoView)

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),

#     # add another path to the url patterns
#     # when you visit the localhost:8000/api
#     # you should be routed to the django Rest framework
#     url('api/', include(router.urls)),
# ]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  