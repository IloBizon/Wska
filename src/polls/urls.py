from django.urls import path
from .views import PollFormView, PollResultsView, PollListView
urlpatterns = [
    path("", PollListView.as_view(), name='polls'),
    path("answer/<int:id>", PollFormView.as_view(), name="answer"),
    path('results/<int:id>', PollResultsView.as_view(), name='results')
]