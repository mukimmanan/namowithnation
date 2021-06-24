from rest_framework.pagination import PageNumberPagination


class TweetsPagination(PageNumberPagination):
    """ Paginating Tweets In The Response """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_query_param = 'page_num'
