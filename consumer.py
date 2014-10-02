#!/usr/local/bin/python
# coding: utf-8
''' SOOOO FAAAAKE, This generates no objective truths. '''
# zope.interface==4.1.1
from __future__ import unicode_literals

from datetime import date, datetime, timedelta
from dateutil.parser import *
import requests
import time
import string
from scrapi.linter import lint
from scrapi.linter.document import RawDocument, NormalizedDocument
from faker import Factory
import random
import json
import uuid

NAME = "fakeconsumer"
DEFAULT = datetime(1970, 01, 01)

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
        rando = string.uppercase + ' '
        email = emails[j].encode('utf-8')
        given = faker.first_name().encode('utf-8')
        surname = faker.last_name().encode('utf-8')
        prefix = faker.prefix().encode('utf-8')
        suffix = faker.suffix().encode('utf-8')
        contributors.append( {
            'email': email,
            'prefix': prefix,
            'given': given,
            'middle': random.choice(rando),
            'family': surname,
            'suffix': suffix,
            'ORCID': '',
            })

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

    date_created = parse(faker.date(), yearfirst=True, default=DEFAULT).isoformat()

    doi = '10.123A/' + str(uuid.uuid4()).replace('-','')[:16]

    url = faker.url()

    doc_id = 'journalofscientificopenness.org:' + str(abs(faker.longitude()))

    timestamp = datetime.now().isoformat()

    date_updated = datetime.now() - timedelta(hours=random.randrange(1,6)) - timedelta(minutes=random.randrange(1,60))
    date_updated = date_updated.isoformat()

    dctypeoptions = ['letter', 'text', 'image', 'text', 'article', 'text', 'text', 'research paper', 'text']
    dctype = random.choice(dctypeoptions)

    ids = {
        'url': url,
        'serviceID': doc_id,
        'doi': doi,
    }

    normalized_dict = { 
        'title': title,
        'contributors': contributors,
        'properties': {
            'type': dctype,
        },
        'description': description,
        'id': ids,
        'source': str(NAME),
        'tags': tags,
        'dateCreated': date_created,
        'dateUpdated': date_updated,
        'timestamp': str(timestamp)
    }

    #return(json.dumps(normalized_dict, indent=4))

    return NormalizedDocument(normalized_dict)

if __name__ == '__main__':
    #print(makefakenormalizeddocument())
    makefakenormalizeddocument()


