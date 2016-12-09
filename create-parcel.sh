#!/bin/bash
#
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


CHECK_ENV=(VERSION DAALVERSION BUILD_NUMBER DAAL_URL DISTRO GIT_TOKEN GIT_HASH)
for env in ${CHECK_ENV[*]}
do
  env | grep "$env=.*"
  if [ $? -gt 0 ]; then
    echo $env env variable isn\'t set
    exit 1
  fi
done

export REPO=daal-parcel
export ORG=trustedanalytics
export PACKAGE_NAME=DAAL_LIB

RELEASE=$BUILD_NUMBER

echo daal-$DAALVERSION.zip
if [ !  -f "daal-$DAALVERSION.zip" ]; then
	wget $DAAL_URL -O daal-$DAALVERSION.zip
fi

rm -rf daal-$DAALVERSION
rm -rf parcel/lib/

unzip -o daal-$DAALVERSION.zip 
mkdir -p parcel/lib
cp -rv daal-$DAALVERSION/* parcel/lib/




python alternatives.py
python parcel.py
python daal-env.py 

mkdir -p $PACKAGE_NAME-$VERSION-$RELEASE
cp -Rv parcel/* $PACKAGE_NAME-$VERSION-$RELEASE/

tar -zcvf $PACKAGE_NAME-$VERSION-$RELEASE-$DISTRO.parcel $PACKAGE_NAME-$VERSION-$RELEASE/ --owner=root --group=root

java -jar  cm_ext/validator/target/validator.jar -f $PACKAGE_NAME-$VERSION-$RELEASE-$DISTRO.parcel

mkdir -p repo
mv $PACKAGE_NAME-$VERSION-$RELEASE-$DISTRO.parcel repo/
pushd repo
    ../cm_ext/make_manifest/make_manifest.py
popd

