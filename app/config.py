import os

elastic = {
    'host': os.environ['ELASTIC_HOST'] if 'ELASTIC_HOST' in os.environ else '127.0.0.1',
    'port': os.environ['ELASTIC_PORT'] if 'ELASTIC_PORT' in os.environ else 9200,
}

index = {
    "segments": "uql-segments",
    "rules": "uql-rules",
    "goals": "uql-goals",
    "scopes": "uql-scopes",
}

unomi = {
    'host': os.environ['UNOMI_HOST'] if 'UNOMI_HOST' in os.environ else '127.0.0.1',
    'protocol': os.environ['UNOMI_PROTOCOL'] if 'UNOMI_PROTOCOL' in os.environ else 'http',
    'port': os.environ['UNOMI_PORT'] if 'UNOMI_PORT' in os.environ else 8181,
    'username': os.environ['UNOMI_USERNAME'] if 'UNOMI_USERNAME' in os.environ else 'karaf',
    'password': os.environ['UNOMI_PASSWORD'] if 'UNOMI_PASSWORD' in os.environ else 'karaf',
}
