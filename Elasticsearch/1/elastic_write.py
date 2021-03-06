from datetime import datetime
import random
from elasticsearch import Elasticsearch
import time
import random

hosts = ['localhost']
es = Elasticsearch(hosts)

for i in range(10):
    doc = {
        'timestamp': datetime.utcnow(),
        # Watch out for timezones. I spent two hours looking for my data, but it was in the future....
        'load': random.random() * 8,
        'rnd': random.randrange(100),
        'name': random.choice(['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptunus']),
        'yes': random.choice([True, False]),
    }

    index_name = 'experimental'
    print(index_name)
    print(doc)
    res = es.index(index=index_name, doc_type='samples', body=doc)
    print(res)
    time.sleep(random.random())