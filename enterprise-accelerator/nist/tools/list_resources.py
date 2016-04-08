#!/usr/bin/python
# Outputs a list of all resources deployed in this template to a CSV file, grouped by stack (template)
# Syntax:  python ./list_resources.py <outputfile>
#
#############################################################################################################
# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved. 									#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in		#
# compliance with the License. A copy of the License is located at  http://aws.amazon.com/apache2.0/		#																		#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT    #
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific         #
# language governing permissions and limitations under the License.                                         #
#############################################################################################################



import json
import os
import csv
import sys

if len(sys.argv) <= 1:
	print "Syntax: python ./list_resources.py <outputfile>"
	sys.exit(1)
else:
	outfile = sys.argv[1]


allfiles = os.listdir("../templates/")

header = [ 'Name', 'Type', 'Template' ]
with open(outfile, 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(header)

for file in allfiles:
        if (("main" in file ) or ("stack" in file)) and (file.endswith(".json")):
		filename = "../templates/" +  file
		with open(filename) as json_file:
			data = json.load(json_file)
			for resource in data['Resources']:
				linedata = [ resource, data['Resources'][resource]['Type'], file ]
				with open(outfile, 'a') as myfile:
    					wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    					wr.writerow(linedata)
