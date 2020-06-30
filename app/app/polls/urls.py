from django.urls import include, path
from rest_framework import routers
from .views import PollViewSet, QuestioniewSet

router = routers.DefaultRouter()
router.register(r'polls', PollViewSet)
router.register(r'questions', QuestioniewSet)

urlpatterns = [
    path('', include(router.urls)),
]