import json
import requests
import boto3

template_file = open('top.json')
template = json.load(template_file)
template_file.close()

aws_type = ''AWS::CloudFormation::Stack

for resource in template['Resources']:
    if template['Resources'][resource]['Type'] == aws_type:
        template['Resources'][resource]['Properties']['Parameters']['ASGHealthCheckType']

