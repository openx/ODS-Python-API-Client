import ox3apiclient
import logging
import requests
import json
import post_config 
import my_creds

# LOAD CREDS FROM 'my_creds.py' file
email=my_creds.email
password=my_creds.password
domain=my_creds.domain
realm=my_creds.realm
consumer_key=my_creds.consumer_key
consumer_secret=my_creds.consumer_secret

ox = ox3apiclient.Client(
    email=email,
    password=password,
    domain=domain,
    realm=realm,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    api_path='/ox/4.0')
    
ox.logon(email, password)

ox.logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ox.logger.addHandler(ch)

# YOUR SETTINGS LOADED FROM 'post_config.py' file
settings = post_config.settings;

print(settings);

results = ox.post('/adunit/', data=settings);
