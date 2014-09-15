#!/usr/local/bin/python
# coding: utf-8
''' SOOOO FAAAAKE, This generates no objective truths. '''

from __future__ import unicode_literals

from datetime import date, timedelta
import requests
import time
from scrapi_tools import lint
from scrapi_tools.document import RawDocument, NormalizedDocument
#import faker
from faker import Factory
import random
import json
import uuid


# TODO: Insert random Unicode into our strings!

TODAY = date.today()
NAME = "fakeconsumer"

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
        contributors = []
        contribnum = random.randrange(0,len(emails))
        
        for j in range(contribnum):
            email = emails[j]
            name = faker.name()
            contributors.append({'name': name, 'email': email})

        description = faker.sciencetext()

        title = faker.sciencesentence()

        if random.choice(['yes', 'yes', 'yes', 'no']) == 'yes': # Chris told me to
            index = random.randrange(1, len(title)-1)
            title = list(title)
            title[index] = random.choice(['ä', 'ê', 'ī', 'ö', 'ù', 'ÿ', 'ç', 'ñ'])
            title = u''.join(title) 

        tags = faker.sciencewords()

        date_created = faker.date()

        doi = '10.1234/' + str(uuid.uuid4()).replace('-','')[:16]

        url = faker.url()

        doc_id = 'journalofscientificopenness.org:' + str(abs(faker.longitude()))

        record = json.dumps({'contributors':contributors, 
            'description':description,
            'title':title,
            'tags':tags,
            'url':url,
            'doc_id': doc_id,
            'doi': doi,
            'date_created':date_created
            })

        records.append(record)

    return records


def consume(days_back=0):

    records = makerecords(5)

    json_list = []
    for record in records:
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
        'source': str(NAME),
        'tags': doc.get('tags') or [],
        'date_created': doc.get('date_created'),
        'timestamp': str(timestamp)
    }

    #print(json.dumps(normalized_dict, sort_keys=True, indent=4))
    return NormalizedDocument(normalized_dict)

if __name__ == '__main__':
    print(lint(consume, normalize))
