from django_filters import FilterSet
from .models import Responses


class ResponsesFilter(FilterSet):
    class Meta:
        model = Responses
        fields = {
            'respbulletins',
        }
