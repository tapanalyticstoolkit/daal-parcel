# vim: set encoding=utf-8

#  Copyright (c) 2016 Intel Corporation 
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import json
import sys
import os
import io
JSON_FILE="parcel/meta/parcel.json"

NAME = "DAAL_LIB"
VERSION = os.environ['VERSION'] if os.environ['VERSION'] else "0.1"
RELEASE = os.environ['RELEASE'] if os.environ['RELEASE'] else "1" 
CDH_START = "5.7.1"
CDH_END = "5.7.1"
PACKAGES = [{"name":"daal", "version": "0.7.4"}]

print "{0}-{1}".format(VERSION,RELEASE)
parcel = {}
parcel["schema_version"] = 1
parcel["name"] = NAME
parcel["version"] = "{0}-{1}".format(VERSION,RELEASE)
parcel["setActiveSymlink"] = True

parcel["depends"] = "CDH (>="+ CDH_START+" ), CDH (<< "+CDH_END+")"

parcel["scripts"] = {}
parcel["scripts"]["defines"] = "daal_env.sh"

parcel["packages"] = PACKAGES

parcel["components"] = []
for p in PACKAGES:
  temp = p.copy()
  temp["pkg_version"] = p["version"]
  parcel["components"].append(temp)
  
parcel["components"] = PACKAGES

parcel["provides"] = ["yarn-plugin","spark-plugin","DAAL"]

parcel["groups"] = []
parcel["users"] = {}
try:
    config_json_open = io.open(JSON_FILE, encoding="utf-8", mode="w")
    config_json_open.write(unicode(json.dumps(parcel, indent=True, sort_keys=True)))
    config_json_open.close()
except IOError:
    print("couldn't write {0}".format(JSON_FILE))
