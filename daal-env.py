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
import io
import os
import glob

MKL_ENV_FILE="parcel/meta/daal_env.sh"
LIB_SEARCH="parcel/lib/*.so"
LIB_SEARCH="parcel/lib/*.jar"
PARCEL_PATH="$PARCELS_ROOT/$PARCEL_DIRNAME"

try:
    config_json_open = io.open(MKL_ENV_FILE, encoding="utf-8", mode="w")
    
    config_json_open.write(u"export LD_LIBRARY_PATH={0}/lib/:$LD_LIBRARY_PATH\n".format(PARCEL_PATH))
    
    classpath = []
    for i in glob.glob(LIB_SEARCH):
        classpath.append("{0}/{1}".format(PARCEL_PATH, os.path.basename(i)))

    
    config_json_open.write(u"export YARN_CLASSPATH={0}:$YARN_CLASSPATH\n".format(":".join(classpath)))

    config_json_open.close()
except IOError:
    print("couldn't write {0}".format(MKL_ENV_FILE))