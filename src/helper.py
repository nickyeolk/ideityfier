def get_arg(request, string):
	if string in request.args:
		return request.args[string]
	else:
		return ''

import mimetypes
import requests

def is_url_image(url):    
    mimetype,encoding = mimetypes.guess_type(url)
    return (mimetype and mimetype.startswith('image'))

def check_url(url):
    """Returns True if the url returns a response code between 200-300,
       otherwise return False.
    """
    try:
        response = requests.get(url)
        print(response.code)
        return response.code in range(200, 209)
    except:
        return False

def is_image_and_ready(url):
    return is_url_image(url) and check_url(url)