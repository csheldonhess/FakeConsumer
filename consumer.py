#!/usr/local/bin/python
# coding: utf-8
''' SOOOO FAAAAKE, This generates no objective truths. '''

from __future__ import unicode_literals

from datetime import date
import requests
import time
from scrapi_tools import lint
from scrapi_tools.document import RawDocument, NormalizedDocument
#import faker
from faker import Factory
import random
import json
import uuid

NAME = "fakeconsumer"

def makefakenormalizeddocument():  # returns one document
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
              
    random.shuffle(emails)
    contributors = []
    contribnum = random.randrange(0,len(emails))
    
    for j in range(contribnum):
        email = emails[j].encode('utf-8')
        name = faker.name().encode('utf-8')
        contributors.append({'name': name, 'email': email})

    description = faker.sciencetext()

    title = faker.sciencesentence()

    if random.choice(['yes', 'yes', 'yes', 'no']) == 'yes': # Chris told me to
        index = random.randrange(1, len(title)-1)
        title = list(title)
        title[index] = random.choice(['ä', 'ê', 'ī', 'ö', 'ù', 'ÿ', 'ç', 'ñ', 'æ'])
        title = u''.join(title)
        title = title[:-1] # removing the period from the sentence
        title = title.title() # half-disbelieving that this is a thing; caps first letter of each word

    tags = faker.sciencewords()

    date_created = faker.date()

    doi = '10.123A/' + str(uuid.uuid4()).replace('-','')[:16]

    url = faker.url()

    doc_id = 'journalofscientificopenness.org:' + str(abs(faker.longitude()))

    timestamp = date.today()


    ids = {
        'url': url,
        'service-id': doc_id,
        'doi': doi,
    }

    normalized_dict = { 
        'title': title,
        'contributors': contributors,
        'properties': {},
        'description': description,
        'meta': {},
        'id': ids,
        'source': str(NAME),
        'tags': tags,
        'date_created': date_created,
        'timestamp': str(timestamp)
    }

    print(json.dumps(normalized_dict, indent=4))

    return NormalizedDocument(normalized_dict)

makefakenormalizeddocument()


