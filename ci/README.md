# Continues integration(CI)

### Get ready with most popular and common tool to build and manager the artifect

1. Jenkins 
2. Nexus

### How i can run 
```
docker-compose build
docker-compose status
docker-compose up -d
```

### Publish the artifect into nexus 
1. Local push
   - setting.xml
        ```
            <?xml version="1.0" encoding="UTF-8" standalone="no"?>
            <settings xmlns="http://maven.apache.org/SETTINGS/1.1.0"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.1.0 http://maven.apache.org/xsd/settings-1.1.0.xsd">
                <servers>
                    <server>
                        <id>nexus</id>
                        <username>admin</username>
                        <password>admin</password>
                    </server>
                </servers>
                <profiles>
                    <profile>
                        <id>nexus</id>
                        <repositories>
                            <repository>
                                <id>central</id>
                                <url>https://central</url>
                                <releases>
                                    <enabled>true</enabled>
                                </releases>
                                <snapshots>
                                    <enabled>true</enabled>
                                </snapshots>
                            </repository>
                        </repositories>
                        <pluginRepositories>
                            <pluginRepository>
                                <id>central</id>
                                <url>https://central</url>
                                <releases>
                                    <enabled>true</enabled>
                                </releases>
                                <snapshots>
                                    <enabled>true</enabled>
                                </snapshots>
                            </pluginRepository>
                        </pluginRepositories>
                    </profile>
                </profiles>
                <pluginGroups>
                    <pluginGroup>org.sonatype.plugins</pluginGroup>
                </pluginGroups>
                <activeProfiles>
                    <activeProfile>nexus</activeProfile>
                </activeProfiles>
                <mirrors>
                    <mirror>
                        <id>nexus</id>
                        <url>http://localhost:8081/repository/maven-snapshots/</url>
                        <mirrorOf>*</mirrorOf>
                    </mirror>


                </mirrors>
            </settings>

        ```
   - cmd
        ```
        mvn deploy -DaltDeploymentRepository=nexus::default::http://localhost:8081/repository/maven-snapshots/ -Dusername=admin -Dpassword=admin -X
        ```
2. Jenkins push
    ```
        // TODO
    ```



