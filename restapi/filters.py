import django_filters

from motels.models import Motel

class MotelFilter(django_filters.FilterSet):
    """
    Filter Motel by town, price, amenities, rating
    """
    town = django_filters.CharFilter(name="town__name")
    amenities = django_filters.CharFilter(name="amenities__name")
    min_price = django_filters.NumberFilter(name="price_range",
                                            lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price_range",
                                            lookup_type='lte')

    class Meta:
        model = Motel
        fields = ['town', 'amenities', 'min_price', 'max_price', 'rating']
