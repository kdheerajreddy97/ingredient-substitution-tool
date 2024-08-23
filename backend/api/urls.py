from django.urls import path
from .views import get_substitute, common_substitutes, submit_substitution

urlpatterns = [
    path('get-substitute/', get_substitute, name='get-substitute'),
    path('common-substitutes/', common_substitutes, name='common-substitutes'),
    path('submit-substitution/', submit_substitution, name='submit-substitution'),
]
