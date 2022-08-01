from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('createUser/', views.createUser, name='create-user'),
    path('votes/', views.requestVotes, name='request-votes'),
    path('votes/all/', views.requestVotesAll, name='request-votes-all'),
    path('candidates/', views.requestCandidates, name='request-candidates'),
]