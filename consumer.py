#!/usr/local/bin/python
# coding: utf-8
''' SOOOO FAAAAKE, This generates no objective truths. '''

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

NAME = u"fakeconsumer"
DEFAULT = datetime(1970, 01, 01)

def copy_to_unicode(element):
    encoding = 'utf-8'
    element = ''.join(element)
    if isinstance(element, unicode):
        return element
    else:
        return unicode(element, encoding=encoding)

def makefakenormalizeddocument():  # returns one document
    faker = Factory.create()

    emails = [
        u'coral@sheldon-hess.org',
        u'erin@cos.io',
        u'chrisseto@cos.io',
        u'fabian@cos.io',
        u'petenagraj@gmail.com',
        u'jh92710@gmail.com',
        u'bgeiger@cos.io',
        u'jeff@cos.io',
        u'andrew@cos.io',
        u'nosek@cos.io',
        u'nope@nope.no',
    ]
              
    random.shuffle(emails)
    contributors = []
    contribnum = random.randrange(0,len(emails))
    
    for j in range(contribnum):
        rando = string.uppercase + ' '
        email = copy_to_unicode(emails[j])
        given = copy_to_unicode(faker.first_name())
        surname = copy_to_unicode(faker.last_name())
        prefix = copy_to_unicode(faker.prefix())
        suffix = copy_to_unicode(faker.suffix())
        contributors.append( {
            'email': email,
            'prefix': prefix,
            'given': given,
            'middle': random.choice(rando),
            'family': surname,
            'suffix': suffix,
            'ORCID': u'',
            })

    description = copy_to_unicode(faker.sciencetext())

    title = copy_to_unicode(faker.sciencesentence())

    if random.choice(['yes', 'yes', 'yes', 'no']) == 'yes': # Chris told me to
        index = random.randrange(1, len(title)-1)
        title = list(title)
        title[index] = random.choice([u'ä', u'ê', u'ī', u'ö', u'ù', u'ÿ', u'ç', u'ñ', u'æ'])
        title = u''.join(title)
        title = title[:-1] # removing the period from the sentence
        title = title.title() # caps first letter of each word

    tags = faker.sciencewords()

    tags = [copy_to_unicode(tag) for tag in tags]

    date_created = parse(faker.date(), yearfirst=True, default=DEFAULT).isoformat()

    doi = copy_to_unicode('10.123A/' + str(uuid.uuid4()).replace('-','')[:16])

    url = copy_to_unicode(faker.url())

    doc_id = copy_to_unicode('journalofscientificopenness.org:' + str(abs(faker.longitude())))

    timestamp = datetime.now().isoformat()

    date_updated = datetime.now() - timedelta(hours=random.randrange(1,6)) - timedelta(minutes=random.randrange(1,60))
    date_updated = date_updated.isoformat()

    dctypeoptions = ['letter', 'text', 'image', 'text', 'article', 'text', 'text', 'research paper', 'text']
    dctype = copy_to_unicode(random.choice(dctypeoptions))

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
        'source': NAME,
        'tags': tags,
        'dateCreated': copy_to_unicode(date_created),
        'dateUpdated': copy_to_unicode(date_updated),
        'timestamp': copy_to_unicode(timestamp),
    }

    #return(json.dumps(normalized_dict, indent=4))

    return NormalizedDocument(normalized_dict)

if __name__ == '__main__':
    #print(makefakenormalizeddocument())
    makefakenormalizeddocument()


