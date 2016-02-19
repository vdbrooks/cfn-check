#!/usr/bin/python

import json, sys
import requests, pprint
import boto3

template_file = open('top.json')
template = json.load(template_file)
template_file.close()

aws_type = 'AWS::CloudFormation::Stack'

for resource in template['Resources']:
    health_type = ''
    try:
        if template['Resources'][resource]['Type'] == aws_type:
            health_type = template['Resources'][resource]['Properties']['Parameters']['ASGHealthCheckType']
            print "RESOURCE: " + str(pprint.pprint(template['Resources'][resource])) + "\n"
            print "HEALTH CHECK TYPE: " + str(health_type)
            print "\n" + str(resource)
    except KeyError, ke:
        print "RESOURCE: " + str(pprint.pprint(template['Resources'][resource])) + "\n"
        print "ERROR: " + "ASGHealthCheckType is not defined in this stack"
        pass

