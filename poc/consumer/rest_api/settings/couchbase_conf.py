
#SERVER Configuration
CouchbaseENV = "local"

CouchbaseConfig = {
    'local': {
        'BUCKET': 'awhcurisdb_local',
        'USERNAME': 'adminadmin',
        'PASSWORD': 'adminadmin',
        'PROTOCOL': 'http',
        'SCHEME': 'couchbase',
        'IP': '127.0.0.1',
        'HOST': 'couchbase://127.0.0.1/',
        'PORT': '8093',
        'TIMEOUT': 7200
    },
    'test': {
        'BUCKET': 'awhcurisdb_local',
        'USERNAME': 'adminadmin',
        'PASSWORD': 'adminadmin',
        'PROTOCOL': 'http',
        'SCHEME': 'couchbase',
        'IP': '127.0.0.1',
        'HOST': 'couchbase://127.0.0.1/',
        'PORT': '4984',
        'TIMEOUT': 7200
    }
}

