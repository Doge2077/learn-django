def self_middleware(get_response):

    def middleware(request):

        print('Before request called.')

        response = get_response(request)

        print('After request called.')

        return response

    return middleware