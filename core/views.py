from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRoot(APIView):
    """
    ###LimitOffsetPagination
    > Every endpoint includes both a "limit" and an "offset" query parameter. 
    The limit indicates the maximum number of items to return, and is equivalent to the page_size in other styles.
    The offset indicates the starting position of the query in relation to the complete set of unpaginated items.

    - ####Example:
        *  #####Paginated motels list with 10 results per page: [/api/motels/?limit=10](/api/motels/?limit=10)

    """
    def get(self, request):
        return Response({
            'motels': reverse('motels-list', request=request),
            'motels-retrieve': reverse('token-auth', request=request),
            'comments': reverse('comments-list', request=request),
            'ammenities': reverse('ammenities-list', request=request),
            'rooms': reverse('rooms-list', request=request),
            'towns': reverse('towns-list', request=request),
            'token-auth': reverse('token-auth', request=request),
        })
