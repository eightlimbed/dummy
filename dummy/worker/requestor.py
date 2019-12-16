import requests
from dummylogging import log


def make_request(url):
    r = requests.get(url)
    stuff = {
        'status_code': r.status_code,
        'content-type': r.headers.get('Content-Type')
    }
    log.bind(function=make_request, url=url)
    log.bind(stuff=stuff)
    log.info('finished making request')
    return True
