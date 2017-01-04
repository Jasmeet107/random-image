import httplib, urllib, base64, random, string, json, pprint, cStringIO
from PIL import Image
import io 

def get_random_image(): 
    search_term = "".join(random.choice(string.ascii_lowercase) for j in range(random.randint(1,6)))

    headers = {
        'Ocp-Apim-Subscription-Key': '9eca18ad3a9f4d16990d07cf0b86221b',
    }

    params = urllib.urlencode({
        'q': search_term
    })
    try:
        conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("POST", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        image_json = json.loads(data)
        match_number = random.randint(0, len(image_json['value'])-1)
        url = image_json['value'][match_number]['contentUrl']
        img_file = io.BytesIO(urllib.urlopen(url).read())
        img = Image.open(img_file)
        img.show()
    except Exception as e:
        print e

def main():
  get_random_image()

if __name__ == '__main__':
  main()






  







