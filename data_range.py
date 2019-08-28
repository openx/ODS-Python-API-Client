import ox3apiclient
import logging
import requests
import json
import report_config

ox = ox3apiclient.client_from_file().logon()

ox.logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ox.logger.addHandler(ch)

# YOUR SETTINGS LOADED FROM 'report_config.py' file
date_range = report_config.date_range

report = ox.post('/date-range/', data=json.dumps(date_range));

