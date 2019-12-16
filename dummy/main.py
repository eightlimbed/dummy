import sys
from dummylogging import log
from worker import requestor
from concurrent.futures import ThreadPoolExecutor


def run(url):
    requestor.make_request(url)

if __name__ == '__main__':
    with ThreadPoolExecutor() as ex:
        for url in sys.argv[1:]:
            log.info(f'submitting request for {url}')
            result = ex.submit(run, url)
