export IMAGE_NAME=devalbo/qroma-project-generator-tools:v2
export CONTAINER_NAME=qroma-project-generator-tools-1

rm -rf protofiles-out

export LOCAL_SOURCE_DIR=$PWD/protofiles-in
export DOCKER_SOURCE_DIR=/usr/src/app/protofiles

export LOCAL_BUILD_DIR=$PWD/protofiles-out
export DOCKER_BUILD_DIR=/usr/src/app/outfiles

echo docker container run -it --name $CONTAINER_NAME -v $LOCAL_SOURCE_DIR:$DOCKER_SOURCE_DIR -v $LOCAL_BUILD_DIR:$DOCKER_BUILD_DIR $IMAGE_NAME
docker container run -it --name $CONTAINER_NAME -v $LOCAL_SOURCE_DIR:$DOCKER_SOURCE_DIR -v $LOCAL_BUILD_DIR:$DOCKER_BUILD_DIR $IMAGE_NAME

docker container rm $CONTAINER_NAME
