import base64
import cStringIO
import PIL
import random 
import requests
import string 
import urllib 
from PIL import Image

def get_random_image(): 
    search_term = "".join(random.choice(string.ascii_lowercase) for character in xrange(random.randint(1,6)))

    headers = {
        'Ocp-Apim-Subscription-Key': '9eca18ad3a9f4d16990d07cf0b86221b',
    }

    params = urllib.urlencode({
        'q': search_term
    })
    try:
        response = requests.post('https://api.cognitive.microsoft.com/bing/v5.0/images/search', params=params, headers=headers)
        response.raise_for_status()
        image_json = response.json()
        match_number = random.randint(0, len(image_json['value'])-1)
        url = image_json['value'][match_number]['contentUrl']
        img_file = cStringIO.StringIO(urllib.urlopen(url).read())
        img = Image.open(img_file)
        img.show()
    except requests.exceptions.RequestException as e:
        print e

def main():
  get_random_image()

if __name__ == '__main__':
  main()






  







