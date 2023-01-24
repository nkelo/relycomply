from flask import Flask
import requests
import threading

app = Flask(__name__)

@app.route("/")
def social_network_activity():
    # TODO: your code here

    def twitter_url():
      try:
         twitter = requests.get('https://takehome.io/twitter').json()
         return twitter
      except:
          print("An exception occurred: twitter")

    def facebook_url():
      try:
         facebook = requests.get('https://takehome.io/facebook').json()
         return facebook
      except:
         print("An exception occurred: facebook")   

    def instagram_url():
      try:
         instagram = requests.get('https://takehome.io/instagram').json()
         return instagram
      except:
         print("An exception occurred: instagram")      

    t_twitter = threading.Thread(target=twitter_url)
    t_facebook = threading.Thread(target=facebook_url)
    t_instagram = threading.Thread(target=instagram_url)

    t_twitter.start()
    t_facebook.start()
    t_instagram.start()

    t_twitter.join()
    t_facebook.join()
    t_instagram.join()

    twitter_endpoint = twitter_url()
    facebook_endpoint = facebook_url()
    instagram_endpoint = instagram_url()

    json_response = {"Twitter": twitter_endpoint, 'Facebook': facebook_endpoint, 'Instagram': instagram_endpoint}

    return json_response