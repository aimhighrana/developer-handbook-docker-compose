## Getting started 

### Download own custom modified war files 
```
Download business-central.war from https://drive.google.com/file/d/1R4d_p6hglz0Ipf_7dQOlm_Y7Sme-OYfg/view?usp=drive_link and place inside current folder
Download kie-server.war from https://drive.google.com/file/d/1Fg38JEponlNUZOIIOrFQMLCAcnd5RoBK/view?usp=drive_link 
```
### Build own image on top of  `jboss/jbpm-server-full:latest`
```
1. Copy the own customized .war files into /opt/jboss/wildfly/standalone/deployments/ 
2. Copy the deployment-descriptor.xml into /home
```
The above .war having 2 importer event listener class 
```
// To handle all process events 
org.jbpm.listeners.CustomProcessEventListener

// Tp handle all task events 
org.jbpm.listeners.CustomTaskEventListener
```

### Build and run to compose docker
```
docker-compose build
docker-compose up
```

### Testing check the logs of this compose 
```
[0m[0m10:26:39,719 INFO [stdout] (default task-11) -----------------TaskEvent listener --------:: taskEvent - {"id":66,"version":1,"priority":0,"name":"Task","subject":"","description":"","names":[{"id":69,"language":"en-UK","text":"Task"}],"subjects":[{"id":70,"language":"en-UK","text":""}],"descriptions":[{"id":68,"language":"en-UK","text":""}],"peopleAssignments":{"taskInitiator":null,"potentialOwners":[{"id":"jack"}],"excludedOwners":[],"taskStakeholders":[],"businessAdministrators":[{"id":"Administrator"},{"id":"process-admin"}],"recipients":[]},"delegation":{"delegates":[],"allowed":null},"taskData":{"status":"Exited","previousStatus":"Reserved","actualOwner":{"id":"jack"},"createdBy":null,"createdOn":1699006496407,"activationTime":1699006496407,"expirationTime":null,"skipable":false,"workItemId":66,"processInstanceId":66,"documentAccessType":"Inline","documentType":"java.util.HashMap","documentContentId":66,"outputAccessType":null,"outputType":null,"outputContentId":-1,"faultName":null,"faultAccessType":null,"faultType":null,"faultContentId":-1,"parentId":-1,"processId":"managebook.order","deploymentId":"managebook_1.0.0-SNAPSHOT","processSessionId":1,"comments":[],"attachments":[],"taskInputVariables":null,"taskOutputVariables":null},"deadlines":{"startDeadlines":[],"endDeadlines":[]},"subTaskStrategy":"NoAction","taskType":null,"formName":"Task","archived":false}
```
#### :) WOW ITS WORKING