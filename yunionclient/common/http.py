"""
OpenStack Client interface. Handles the REST calls and responses.
"""

import copy
import logging
import os

import httplib2

import json

from yunionclient.common import exceptions

logging.basicConfig()
logger = logging.getLogger(__name__)
USER_AGENT = 'yunon-python-client'


class HTTPClient(httplib2.Http):

    def __init__(self, timeout, insecure):
        super(HTTPClient, self).__init__(timeout=timeout,
                        disable_ssl_certificate_validation=insecure)
        # httplib2 overrides
        self.force_exception_to_status_code = True

    def http_log(self, args, kwargs, resp, body):
        if os.environ.get('YUNIONCLIENT_DEBUG', False):
            ch = logging.StreamHandler()
            logger.setLevel(logging.DEBUG)
            logger.addHandler(ch)
        elif not logger.isEnabledFor(logging.DEBUG):
            return

        string_parts = ['curl -i']
        for element in args:
            if element in ('GET', 'POST'):
                string_parts.append(' -X %s' % element)
            else:
                string_parts.append(' %s' % element)

        for element in kwargs['headers']:
            header = ' -H "%s: %s"' % (element, kwargs['headers'][element])
            string_parts.append(header)

        logger.debug("REQ: %s\n" % "".join(string_parts))
        if 'raw_body' in kwargs:
            logger.debug("REQ BODY (RAW): %s\n" % (kwargs['raw_body']))
        if 'body' in kwargs:
            logger.debug("REQ BODY: %s\n" % (kwargs['body']))
        logger.debug("RESP: %s\nRESP BODY: %s\n", resp, body)


    def _strip_version(self, endpoint):
        """Strip a version from the last component of an endpoint if present"""

        # Get rid of trailing '/' if present
        while endpoint.endswith('/'):
            endpoint = endpoint[:-1]
        url_bits = endpoint.split('/')
        # regex to match 'v1' or 'v2.0' etc
        import re
        if re.match('v\d+\.?\d*', url_bits[-1]):
            endpoint = '/'.join(url_bits[:-1])
        return endpoint

    def _get_urllib2_raw_request(self, endpoint, auth_token, method, url,
                                    **kwargs):
        import urllib.request, urllib.error, urllib.parse
        url = endpoint + url
        url = url.encode('UTF-8')
        req = urllib.request.Request(url)
        headers = copy.deepcopy(kwargs.get('headers', {}))
        headers.setdefault('User-Agent', USER_AGENT)
        headers.setdefault('Connection', 'Close')
        if auth_token:
            headers.setdefault('X-Auth-Token', auth_token)
        for h in list(headers.keys()):
            req.add_header(h, headers[h])
        if 'body' in kwargs:
            req.add_data(kwargs['body'])
        return urllib.request.urlopen(req)

    def _http_request(self, endpoint, auth_token, url, method, **kwargs):
        """ Send an http request with the specified characteristics.
        Wrapper around httplib2.Http.request to handle tasks such as
        setting headers, JSON encoding/decoding, and error handling.
        """
        url = endpoint + url

        # Copy the kwargs so we can reuse the original in case of redirects
        kwargs['headers'] = copy.deepcopy(kwargs.get('headers', {}))
        kwargs['headers'].setdefault('User-Agent', USER_AGENT)
        #kwargs['headers'].setdefault('Accept-Encoding', 'identity')
        if auth_token:
            kwargs['headers'].setdefault('X-Auth-Token', auth_token)

        if 'body' not in kwargs and method in ['POST', 'PUT']:
            kwargs['headers'].setdefault('Content-length', '0')

        #print url
        #print kwargs['headers']
        resp, body = super(HTTPClient, self).request(url, method, **kwargs)
        self.http_log((url, method,), kwargs, resp, body)

        #print resp
        #print 'BODY', body

        if 400 <= resp.status < 600:
            #logger.exception("Request returned failure status.")
            raise exceptions.from_response(resp, body)
        elif resp.status in (301, 302, 305):
            # Redirected. Reissue the request to the new location.
            return self._http_request(resp['location'], method, **kwargs)

        return resp, body

    def _json_request(self, endpoint, auth_token, method, url, **kwargs):
        kwargs.setdefault('headers', {})

        if 'body' in kwargs and kwargs['body'] is not None:
            kwargs['headers'].setdefault('Content-Type', 'application/json')
            kwargs['body'] = json.dumps(kwargs['body'])

        resp, body = self._http_request(endpoint, auth_token, url, method,
                                        **kwargs)

        if body:
            try:
                body = json.loads(body)
            except ValueError:
                logger.debug("Could not decode JSON from body: %s" % body)
        else:
            logger.debug("No body was returned.")
            body = None

        return resp, body

    def _raw_request(self, endpoint, auth_token, method, url, **kwargs):
        kwargs.setdefault('headers', {})

        if 'body' in kwargs and kwargs['body'] is not None:
            kwargs['headers'].setdefault('Content-Type',
                                     'application/octet-stream')
        return self._http_request(endpoint, auth_token, url, method, **kwargs)
