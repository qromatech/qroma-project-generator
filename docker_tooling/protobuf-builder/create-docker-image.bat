set IMAGE_NAME=devalbo/qroma-project-generator-tools
set IMAGE_VERSION=v2

docker build --tag %IMAGE_NAME%:%IMAGE_VERSION% .

docker push %IMAGE_NAME%:%IMAGE_VERSION%