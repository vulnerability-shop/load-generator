from request_types import http_basic

def do_http_basic(url):
    r = http_basic.http_request(url)
    return r
