import json
import sys
import io
import os
import glob
JSON_FILE="parcel/meta/alternatives.json"
PRIORITY=1
CDH_PATH="/opt/cloudera/parcels/CDH"
LIB_PATH=CDH_PATH+"/lib64"
YARN_JAR_PATH=CDH_PATH+"/lib/hadoop-yarn/lib"
#opt/cloudera/parcels/CDH/lib/hadoop-yarn/lib/
alternatives = {}

def alt(destination, source):
  return {
      "destination": destination,
      "source": source,
      "priority": PRIORITY,
      "isDirectory": False
      }

"""
lib_jars = glob.glob("parcel/jars/*")
for jar in lib_jars:
  name = os.path.basename(jar)
  alternatives["{0}_{1}".format("jars",name)] = alt("{0}/{1}".format(YARN_JAR_PATH,name),
  "{0}/{1}".format("jars",name))
"""


alternatives["daal.jar"] = alt(YARN_JAR_PATH+"/daal.jar", 
"lib/daal.jar")


alternatives["libDaalTkJavaAPI.so"] = alt(LIB_PATH+"/libDaalTkJavaAPI.so", 
"lib/libDaalTkJavaAPI.so")


alternatives["libiomp5.so"] = alt(LIB_PATH+"/libiomp5.so", 
"lib/libiomp5.so")


alternatives["libJavaAPI.so"] = alt(LIB_PATH+"/libJavaAPI.so", 
"lib/libJavaAPI.so")

alternatives["libtbb.so.2"] = alt(LIB_PATH+"/libtbb.so.2", 
"lib/libtbb.so.2")

"""
alternatives["mkl.conf"] = alt("/etc/ld.so.conf.d/mkl.conf", 
"mkl.conf", 
False)
alternatives["ld_path.sh"] = alt("/etc/profile.d/ld_path.sh", 
"ld_path.sh", 
False)
"""
try:
    config_json_open = io.open(JSON_FILE, encoding="utf-8", mode="w")
    config_json_open.write(unicode(json.dumps(alternatives, indent=True, sort_keys=True)))
    config_json_open.close()
except IOError:
    print("couldn't write {0}".format(JSON_FILE))
    

