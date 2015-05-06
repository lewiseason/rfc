import click
import sys
from contextlib import closing

RFC_URL = 'http://www.rfc-editor.org/rfc/rfc{0}.txt'
ENCODING = sys.getdefaultencoding()

try:
    # Python 3
    import urllib.request as urllib
    formfeed = bytes(chr(12), ENCODING)
except ImportError:
    # Python 2
    import urllib2 as urllib
    formfeed = chr(12)


def strip_formfeeds(response_bytes):
    """
    Click escapes them, and less can't use them anyway,
    so strip formfeed characters from the response
    """

    return response_bytes.replace(formfeed, b'')


def fetch_url(url):
    """
    Fetch the given url, strip formfeeds and decode
    it into the defined encoding
    """

    with closing(urllib.urlopen(url)) as f:
        if f.code is 200:
            response = f.read()
            return strip_formfeeds(response).decode(ENCODING)


@click.command()
@click.argument('number', nargs=1, type=int)
def main(number):
    url = RFC_URL.format(number)
    response = fetch_url(url)

    try:
        click.echo_via_pager(response)
    except BrokenPipeError:
        pass
