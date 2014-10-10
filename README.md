# Airseed.py

TODO: Write a gem description

## Installation

To install it, simply:

    $ pip install airseed

## Usage

    import os

    import Airseed
    from lib import *

    client_id = os.environ["CLIENT_ID"]
    client_secret = os.environ["CLIENT_SECRET"]

    airseed = Airseed.Airseed(client_id, client_secret)

    oauth = OAuth.OAuth(airseed, callback_url = 'https://www.example.com/callback')
    oauth.login(provider = 'google_auth2')

    user_api = UserApi.UserApi(airseed)
    user_profile = user_api.get_user_by_id(id = 'c2edddfaefe2c81a8696291c6fc5c97f6f75461b', bearer_token = 'a_bearer_token')
    user_products = user_api.get_data_for_user(id = 'c2edddfaefe2c81a8696291c6fc5c97f6f75461b', bearer_token = 'a_bearer_token', category = 'product')


## Contributing

1. Fork it ( https://github.com/[my-github-username]/airseed.py/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

