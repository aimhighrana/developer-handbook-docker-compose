### Apache livy srever with master and worker node 

#### How can i submit the job 
```
curl --location 'http://localhost:8998/batches' \
--header 'Content-Type: application/json' \
--data '{
    "file": "/target/mdo-datascope-spark-2024.01.03.01-SNAPSHOT.jar",
    "className": "io.prospecta.elastic.DataScopeSparkLoader",
    "jars": [
        "/target/mdo-datascope-spark-2024.01.03.01-SNAPSHOT.jar"
    ],
    "conf": {
        "spark.executorEnv.dms_store": "azure",
        "spark.driverEnv.dms_store": "azure"
    }
}'
```