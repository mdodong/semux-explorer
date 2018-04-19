"""For Semux API access """

import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

HOST = 'http://localhost:5271/v2.0.0'
USERNAME = 'mddsemux'
PASSWORD = 'mdd@123pass'

configuration = swagger_client.Configuration()
configuration.host = HOST
configuration.username = USERNAME
configuration.password = PASSWORD

"""For Flask """
from app import app
