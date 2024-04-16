FROM jboss/jbpm-server-full:latest
COPY business-central.war kie-server.war /opt/jboss/wildfly/standalone/deployments/
COPY standalone.xml /opt/jboss/wildfly/standalone/configuration/
COPY deployment-descriptor.xml /home/

## COPY the custom module into ... jboss wildfly module
COPY amqp-client-5.21.0.jar /opt/jboss/wildfly/modules/system/layers/base/com/rabbitmq/client/main/amqp-client-5.21.0.jar
COPY module.xml /opt/jboss/wildfly/modules/system/layers/base/com/rabbitmq/client/main/module.xml


MAINTAINER sandeep.rana(aimhigh.excel@gmail.com)
