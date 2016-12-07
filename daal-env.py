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