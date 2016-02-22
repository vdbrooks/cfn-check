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
    if template['Resources'][resource]['Type'] == aws_type:
        if entity in config['tests']['scaling-policies'][0]['ignored-stacks']:
                print resource
                print "This is an ignored stack"
        health_type = template['Resources'][resource]['Properties']['Parameters'].get('ASGHealthCheckType', None)
            if health_type:
                print "RESOURCE: " + str(resource) 
                print "HEALTH CHECK TYPE: " + str(health_type)
                print ""
            


