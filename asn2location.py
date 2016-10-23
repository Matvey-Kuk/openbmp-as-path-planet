#!/usr/bin/python3

import requests
import json
import sys
import re
import pprint

def getASN(asn):
    ASN_URL= "https://whois.arin.net/rest/asn/AS%s"
    ASN_HEADER = {'Accept':'application/json'}
    r = requests.get(ASN_URL % asn, headers=ASN_HEADER)
    print (json.dumps(r.json(),indent=4))

def getPOC(asn):
    ASN_URL= "https://whois.arin.net/rest/asn/AS%s/pocs"
    ASN_HEADER = {'Accept':'application/json'}
    r = requests.get(ASN_URL % asn, headers=ASN_HEADER)
    return r.json()['pocs']['pocLinkRef']['@handle']
def poc2address(poc):
    POC_URL= "https://whois.arin.net/rest/poc/%s"
    POC_HEADER = {'Accept':'application/json'}
    r = requests.get(POC_URL % poc, headers=POC_HEADER)
    rj = r.json()['poc']
    address = {}
    address['country'] = rj['iso3166-1']['code2']['$']
    address['state'] = rj['iso3166-2']['$']
    address['city'] = rj['city']['$']
    address['postal'] = rj['postalCode']['$']
    address['label'] = '%s %s,%s' % (address['city'],address['postal'],address['country'])
    return address
def getARIN(asn):
    try:
        return poc2address(getPOC(asn))
    except:
        return None
def getAFRINIC(asn):
    URL= "https://rdap.afrinic.net/rdap/autnum/%s"
    try:
        r = requests.get(URL % asn)
        address={}
        label = ''
        for item in r.json()['entities'][0]['vcardArray'][1][-1][3]:
            if item != '':
                label = label + ',' + item
        label = label[1:]
        address['country'] = ''
        address['city'] = ''
        address['postal'] = ''
        address['label'] = label
        return address
    except:
        return None

def getAPNIC(asn):
    URL= "https://rdap.apnic.net/autnum/%s"
    try:
        r = requests.get(URL % asn)
        address={}
        rj = r.json()['entities'][0]['vcardArray'][1][3][3]
        address={}
        address['country'] = rj[6]
        address['city'] = rj[3]
        address['postal'] = rj[5]
        address['label'] = '%s %s,%s' % (address['city'],address['postal'],address['country'])
        return address
    except:
        return None

def getRIPE(asn):
    URL= "https://rest.db.ripe.net/search.json?query-string=as%s&flags=no-filtering"
    HEADER = {'Accept':'application/json'}
    r = requests.get(URL % asn)
    if 'ASN block not managed by the RIPE NCC' in json.dumps(r.json()):
        return None
    else:
        #print (json.dumps(r.json(),indent=4))
        try:
            rj = r.json()['objects']['object'][2]['attributes']['attribute']
            address = {}
            address['country'] = rj[6]['value']
            address['city'] = rj[5]['value']
            address['postal'] = rj[4]['value']
            address['label'] = '%s %s,%s' % (address['city'],address['postal'],address['country'])
            return address
        except:
            return None


def getCoordinates(asn):
    address=getRIPE(asn)
    if address is not None:
        return address2location(address)
    address=getARIN(asn)
    if address is not None:
        return address2location(address)
    address=getAPNIC(asn)
    if address is not None:
        return address2location(address)
    address=getAFRINIC(asn)
    if address is not None:
        return address2location(address)
    address=getLACNIC(asn)
    if address is not None:
        return address2location(address)
    return None

def address2location(address):
    URL= "http://maps.googleapis.com/maps/api/geocode/json?address=%s"
    try:
        r = requests.get(URL % address)
        coordinates={}
        result = r.json()
        return result['results'][0]['geometry']['location']
    except:
        return None

if __name__ == "__main__":
    asn = sys.argv[1]
    #print(json.dumps( poc2address(getPOC(asn)),indent=4))
    print(getCoordinates(asn))
