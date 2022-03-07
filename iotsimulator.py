#!/usr/bin/python

'''
To generate <number> JSON data: 
$ ./iotsimulator.py <number>

'''

import sys
import datetime
import random
from random import randrange
import re
import copy


# Set number of simulated messages to generate
if len(sys.argv) > 1:
  num_msgs = int(sys.argv[1])#10
else:
  num_msgs = 1

# mapping of a guid and a state {guid: state}
device_state_map = {}  # initialising variable

# average annual temperature of each state : to simulate the data we are using below code
temp_base = {'WA': 48.3, 'DE': 55.3, 'DC': 58.5, 'WI': 43.1, 
		  'WV': 51.8, 'HI': 70.0, 'FL': 70.7, 'WY': 42.0, 
		  'NH': 43.8, 'NJ': 52.7, 'NM': 53.4, 'TX': 64.8, 
		  'LA': 66.4, 'NC': 59.0, 'ND': 40.4, 'NE': 48.8, 
		  'TN': 57.6, 'NY': 45.4, 'PA': 48.8, 'CA': 59.4, 
		  'NV': 49.9, 'VA': 55.1, 'CO': 45.1, 'AK': 26.6, 
		  'AL': 62.8, 'AR': 60.4, 'VT': 42.9, 'IL': 51.8, 
		  'GA': 63.5, 'IN': 51.7, 'IA': 47.8, 'OK': 59.6, 
		  'AZ': 60.3, 'ID': 44.4, 'CT': 49.0, 'ME': 41.0, 
		  'MD': 54.2, 'MA': 47.9, 'OH': 50.7, 'UT': 48.6, 
		  'MO': 54.5, 'MN': 41.2, 'MI': 44.4, 'RI': 50.1, 
		  'KS': 54.3, 'MT': 42.7, 'MS': 63.4, 'SC': 62.4, 
		  'KY': 55.6, 'OR': 48.4, 'SD': 45.2}

# latest temperature measured by sensors {guid: temperature}
current_temp = {}   # initialising variable

# Fixed values
guid_base = "0-ZZZ12345678-"
destination = "0-AAA12345678"
format = "urn:example:sensor:temp"

# Choice for random letter
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # initialising variable
#  just initialising the data format
iotmsg_header = """\
{ "guid": "%s", 
  "destination": "0-AAA12345678", 
  "state": "NV", """

iotmsg_eventTime = """\
  "eventTime": "%sZ", """

iotmsg_payload ="""\
  "payload": {"format": "%s", """

iotmsg_data ="""\
	 "data": { "temperature": %.1f  }   
	 }
}"""


##### Generate JSON output:
if __name__ == "__main__":
	for counter in range(0, num_msgs):#10
		rand_num = str(random.randrange(0, 9)) + str(random.randrange(0, 9))#46
		rand_letter = random.choice(letters)#P
		temp_init_weight = random.uniform(-5, 5)#3
		temp_delta = random.uniform(-1, 1)#1

		guid = guid_base + rand_num + rand_letter # 0-ZZZ12345678-46P
		state = random.choice(temp_base.keys()) #NV

		if (not guid in device_state_map): # first entry
			device_state_map[guid] = state #NV
			current_temp[guid] = temp_base[state] + temp_init_weight	 #52.9
			
		elif (not device_state_map[guid] == state):		# The guid already exists but the randomly chosen state doesn't match
			state = device_state_map[guid]

		temperature = current_temp[guid] + temp_delta #53.9
		current_temp[guid] = temperature  # update current temperature#53.9	
		today = datetime.datetime.today() #19092021110102
		datestr = today.isoformat()#19092021110102

		print re.sub(r"[\s+]", "", iotmsg_header) % (guid, destination, state),
		print re.sub(r"[\s+]", "", iotmsg_eventTime) % (datestr),
		print re.sub(r"[\s+]", "", iotmsg_payload) % (format),
		print re.sub(r"[\s+]", "", iotmsg_data) % (temperature)