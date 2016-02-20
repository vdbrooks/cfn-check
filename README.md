# cfn-check
A lambda function to validate cloudformation templates accoridng to a custom set of rules

Configuration: config.yml is used to define a list of tests, and a few properties. Right now, the cofniguration essentially maps to functions defined in cfn-check.py. Will extend this later so that people can declaritively define tests, using a very simple dsl that maps more closely to the json structures of various cloud formation resources. 
