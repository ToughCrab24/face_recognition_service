CONNECT_RESULT=$(docker run --rm -i -v /var/run/docker.sock:/var/run/docker.sock -e DOCKER_HOST dockercloud/client -u ${DOCKER_USER} -p ${DOCKER_PASSWORD} shaned24/things)

echo $CONNECT_RESULT

HOST_REGEX="DOCKER_HOST=?(.+)"
[[ $CONNECT_RESULT =~ $HOST_REGEX ]] && DOCKER_HOST_CONTAINER=${BASH_REMATCH[1]}
echo HOST=$DOCKER_HOST_CONTAINER
export DOCKER_HOST=${DOCKER_HOST_CONTAINER}
echo ${DOCKER_HOST}

docker stack deploy -c docker/prod.yml --with-registry-auth things_prod