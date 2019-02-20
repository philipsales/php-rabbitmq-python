import json
import os 
import sys
import datetime as dt

from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery, N1QLError
from couchbase.exceptions import CouchbaseTransientError, CouchbaseError, CouchbaseNetworkError

from settings.base_conf import couchbase_config

import logging
logger = logging.getLogger("couchbase.n1q1")

conn = couchbase_config.CouchbaseConfig[couchbase_config.CouchbaseENV]

USERNAME = conn['USERNAME'] 
PASSWORD = conn['PASSWORD'] 
BUCKET = conn['BUCKET'] 
HOST = conn['HOST'] 
URL = HOST + conn['BUCKET']
IP_ADDRESS = conn['IP'] 
TIMEOUT = conn['TIMEOUT']
PROTOCOL = conn['PROTOCOL']
PORT = conn['PORT']
API_ENDPOINT = "_all_docs?"


def couchbase_get():
    try:
        statement = _set_statement()
        logger.info(statement)
        
    except FileNotFoundError:
        logger.info(statement)

    res = _get_all(statement)
    return _dict2json(res, True)

def _set_statement(**kwargs):
    statement = ("SELECT * from `awhcurisdb_local` awh ") 
    return statement 

def _authenticate():
    cluster = Cluster(HOST)
    authenticator = PasswordAuthenticator(USERNAME, PASSWORD)
    cluster.authenticate(authenticator)
    bucket = cluster.open_bucket(BUCKET)
    return bucket

def _get_all(statement): 
    try:
        #bucket = _authenticate()
        bucket = Bucket(URL)
        bucket.n1ql_timeout = TIMEOUT
        query = N1QLQuery(statement)
        query.timeout = TIMEOUT 
        res = bucket.n1ql_query(query)

        results = []
        for row in bucket.n1ql_query(query):
            results.append(row)
        print(results)

    except (CouchbaseError, CouchbaseTransientError, CouchbaseNetworkError) as err: 
        logger.info(err)
        sys.exit(1)

    return res

def _dict2json(results, is_etl):
    counter = 0
    data = []

    for row in results: 
        data.append(json.dumps(row))
        counter += 1
        logger.info(counter)

    return data
#run as standalone module
if __name__ == "__main__":
    couchbase_get()