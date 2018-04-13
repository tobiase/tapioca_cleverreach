class CleverreachTokenAcquireException(Exception):

    def __init__(self, response, data=None):
        message = "response status code: {}".format(response.status_code)

        if data is not None and 'error' in data:
            message += '\n' + data['error']['message']

        super(CleverreachTokenAcquireException, self).__init__(message)
