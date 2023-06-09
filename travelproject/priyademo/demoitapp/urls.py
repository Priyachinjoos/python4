from .import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo')
    # path('add/', views.function,name='function'),
    # path('subs/',views.function,name="function"),
    # path('mult/',views.function,name="function"),
    # path('div/',views.function,name="function")

    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('details/',views.details,name='details'),
    # path('thanks/',views.thanks,name='thanks')

]