from create_api import create_api
from existentialrick import existentialrick

def post_tweet(event="", context=""):
    api = create_api()
    print("API created")

    rick = existentialrick()
    rick.get_random_word()
    tweet = rick.write_tweet()
    try:
        if tweet: 
            api.update_status(status=tweet)
            #print(tweet)
    except Exception as e:
        raise e