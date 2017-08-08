from django.conf.urls import include, url
from miapp.views import ShowAllInformation, ShowResult
from rest_framework import routers
router = routers.SimpleRouter()


urlpatterns = [
    url(r'^employeeinfo', ShowAllInformation.as_view()),
    url(r'^searchdetail', ShowResult.as_view()),
    url(r'^', include(router.urls)),
]