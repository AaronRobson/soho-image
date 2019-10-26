#!/usr/bin/python

import webbrowser
try:
    from urllib.parse import urljoin
except ImportError:
    # python2
    from urlparse import urljoin

'''Finds the most recent images of the sun from SOHO, displays them
on the command-line and attempts to open them in the default web browser.
'''

rootSite = 'https://sohowww.nascom.nasa.gov'


def ImagePathMask(animated, small):
    if animated:
        pathMask = '/data/LATEST/current_%%s%s.gif' % ('small'*small)
    else:
        pathMask = '/data/realtime/%%s/%d/latest.jpg' % ((1024, 512)[small])

    return urljoin(rootSite, pathMask)


# These aren't lined up: 'mdi_igr', 'mdi_mag', 'c2', 'c3'.
imageTypes = ('eit_171', 'eit_195', 'eit_284', 'eit_304')


def ImageAddresses(animated, small):
    return (ImagePathMask(animated, small) % (type) for type in imageTypes)


aboutPath = urljoin(rootSite, '/data/realtime/image-description.html')


def OpenWebpage(url):
    '''Open a webpage and print addresses and status to screen.
    '''
    try:
        webbrowser.open(url)
    except webbrowser.Error:
        prefix = 'Could not open'
    else:
        prefix = 'Opened'

    return '%s: "%s"' % (prefix, url)


def Main(animated=True, small=True):
    print('Please see: "%s".\n' % (aboutPath))
    print('Settings:\n\tAnimated: %s\n\tSmall: %s\n' % (animated, small))

    for message in (OpenWebpage(imageAddress)
                    for imageAddress in ImageAddresses(animated, small)):
        print(message)


if __name__ == "__main__":
    Main()
