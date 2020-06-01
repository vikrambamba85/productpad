from django.urls import  path 
from . import views 
from .views import AboutPageView
from .views import WebinarPageView
from .views import ConsultingPageView
from .views import WorkPageView

urlpatterns = [
    path('work/', WorkPageView.as_view(), name='work'),
    path('consulting/', ConsultingPageView.as_view(), name='consulting'),
    path('webinar/', WebinarPageView.as_view(), name='webinar'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('',views.home, name = 'home' )
]