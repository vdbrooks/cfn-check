#!/usr/bin/python

import json
import requests
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
    except KeyError, ke:
        print "ran into an error: " + ke
        sys.exit(1)

