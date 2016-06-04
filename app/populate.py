from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': "localhost", 'port': 9200}])
# create index if it's not in the database
if not es.indices.exists('poly1'):
    settings = {
        "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
        },
        "mappings": {
            "list":{
                "properties": {
                    "location": {
                            "type": "geo_shape",
                            "tree": "quadtree",
                            "precision": "1m"
                        }
                    }

            }
        }
    }
    # create index
    try :
         es.indices.create(index='poly1', ignore=400, body=settings, request_timeout=60)
         print "index created"
    except:
        print "Error!!"
