from django.urls import path,include
from .import views

urlpatterns = [
    # path('stuinfo/<int:pk>',views.Student_Detail),
    # path('stuinfo/',views.Student_List),
    # path('studentapi/',views.StudentAPI.as_view()),
    path('studentapi/',views.hello_world),
]
