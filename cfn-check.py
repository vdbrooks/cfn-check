#!/usr/bin/python

import json, sys
import yaml
import requests, pprint
import boto3

template_file = open('top.json')
template = json.load(template_file)
template_file.close()

#config_file = open(config/config.json)
#config = json.load(config_file)
#config_file.json()

config_file = open('config/config.yml')
config = yaml.load(config_file)

aws_type = 'AWS::CloudFormation::Stack'

for resource in template['Resources']:
    health_type = ''
    try:
        if template['Resources'][resource]['Type'] == aws_type:
            for entity in config['tests']['scaling-policies'][0]['ignored-stacks']:
                if resource == entity:
                    print resource
                    print "This is an ignored stack"
                    pass
            health_type = template['Resources'][resource]['Properties']['Parameters']['ASGHealthCheckType']
            print "RESOURCE: " + str(resource) 
            print "HEALTH CHECK TYPE: " + str(health_type)
            print ""
            
    except KeyError, ke:
        print "RESOURCE: " + str(resource) 
        print "ERROR: " + "ASGHealthCheckType is not defined in this stack"
        print ""
        pass

