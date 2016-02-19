# cfn-check
A lambda function to validate cloudformation templates accoridng to a custom set of rules

Configuration: config.json is used to define a list of tests. Right now, the tests essentially map to functions defined in cfn-check.py.
Will extend this later so that people can declaritively define tests, using a very simple dsl.
