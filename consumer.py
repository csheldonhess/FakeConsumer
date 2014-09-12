''' SOOOO FAAAAKE, This generates no objective truths. '''

from datetime import date, timedelta
import requests
import time
from scrapi_tools import lint
from scrapi_tools.document import RawDocument, NormalizedDocument
from faker import Factory
import random
import json
import uuid

TODAY = date.today()
NAME = "fakeconsumer"

random_uuid = uuid.uuid4

def makerecords(numrecords=1):
    faker = Factory.create()

    records = []
    emails = [
        'coral@sheldon-hess.org',
        'erin@cos.io',
        'chrisseto@cos.io',
        'fabian@cos.io',
        'petenagraj@gmail.com',
        'jh92710@gmail.com',
        'bgeiger@cos.io',
        'jeff@cos.io',
        'andrew@cos.io',
        'nosek@cos.io',
        'nope@nope.no',
    ]
        

    for i in range(numrecords):
        
        random.shuffle(emails)
        #emails = random.shuffle(emails)
        contributors = []
        contribnum = random.randrange(0,len(emails))
        
        for j in range(contribnum):
            email = emails[j]
            name = faker.name()
            contributors.append({'name': name, 'email': email})

        description = faker.text()

        title = faker.sentence()

        tags = faker.words()

        date_created = faker.date()

        url = faker.url()

        doc_id = 'journalofscientificopenness.org:' + str(abs(faker.longitude()))

        record = json.dumps({'contributors':contributors, 
            'description':description,
            'title':title,
            'tags':tags,
            'url':url,
            'doc_id': doc_id,
            'doi': '',
            'date_created':date_created
            })

        records.append(record)

    return records


def consume(days_back=0):

    records = makerecords(5)

    json_list = []
    for record in records:
        ## TODO: make lack of contributors continue the loop
        json_list.append(RawDocument({
                    'doc': record,
                    'source': NAME,
                    'doc_id': 'gmail',
                    'filetype': 'json'
                }))

    return json_list

def normalize(raw_doc, timestamp):
    doc = raw_doc.get('doc')

    doc = json.loads(doc)

    contributor_list = []
    contributors = doc['contributors']
    for contributor in contributors:
        name = contributor.get('name').encode('utf-8') or ''
        email = contributor.get('email').encode('utf-8') or ''
        contributor_list.append({'full_name': name, 'email': email})

    ids = {}
    ids['url'] = doc.get('url')
    if ids['url'] == None:
        raise Exception('Warning: No URL provided...')
    ids['doi'] = doc.get('doi')
    ids['service_id'] = doc.get('doc_id')

    normalized_dict = { 
        'title': (doc.get('title', ['No title.']))[:-1], # take off period
        'contributors': contributor_list,
        'properties': {},
        'description': (doc.get('description') or ['']),
        'meta': {},
        'id': ids,
        'source': NAME,
        'tags': doc.get('tags') or [],
        'date_created': doc.get('date_created'),
        'timestamp': str(timestamp)
    }

    print(json.dumps(normalized_dict, sort_keys=True, indent=4))
    return NormalizedDocument(normalized_dict)

if __name__ == '__main__':
    print(lint(consume, normalize))
