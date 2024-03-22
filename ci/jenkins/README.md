## How to run 
```
    docker run -d --name jenkins-blueocean --detach --network jenkins --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --publish 8082:8080 --publish 50000:50000 --restart=on-failure --env JAVA_OPTS="-Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true" custom-jenkins-docker:latest 
```