#!/bin/bash

CHECK_ENV=(VERSION BUILD_NUMBER DAAL_URL DISTRO GIT_TOKEN GIT_HASH)
for env in ${CHECK_ENV[*]}
do
  env | grep "$env=.*"
  if [ $? -gt 0 ]; then
    echo $env env variable isn\'t set
    exit 1
  fi
done

export PACKAGE_NAME=DAAL_LIB

RELEASE=$BUILD_NUMBER

echo daal-$VERSION.zip
if [ -f "daal-$VERSION.zip" ]; then
	wget $DAAL_URL -O daal-$VERSION
fi

rm -rf daal-$VERSION
rm -rf parcel/lib/

unzip -o daal-$VERSION.zip 
mkdir -p parcel/lib
cp -rv daal-$VERSION/* parcel/lib/




python alternatives.py
python parcel.py
python daal-env.py 

cp -Rv parcel $PACKAGE_NAME-$VERSION-$RELEASE

tar -zcvf $PACKAGE_NAME-$VERSION-$RELEASE-$DISTRO.parcel $PACKAGE_NAME-$VERSION-$RELEASE/ --owner=root --group=root