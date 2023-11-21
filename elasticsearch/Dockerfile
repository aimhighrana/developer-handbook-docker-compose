FROM docker.elastic.co/elasticsearch/elasticsearch:7.10.2

RUN mkdir /usr/share/elasticsearch/config/ssl
COPY ca.cert /usr/share/elasticsearch/config/ssl/
COPY key.key /usr/share/elasticsearch/config/ssl/
COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
RUN sh /usr/share/elasticsearch/bin/elasticsearch-users useradd admin1 -p Welcome@123 -r kibana_dashboard_only_user,apm_system,watcher_admin,logstash_system,rollup_user,kibana_user,beats_admin,remote_monitoring_agent,rollup_admin,data_frame_transforms_admin,snapshot_user,monitoring_user,enrich_user,kibana_admin,logstash_admin,machine_learning_user,data_frame_transforms_user,machine_learning_admin,watcher_user,apm_user,beats_system,reporting_user,transform_user,kibana_system,transform_admin,transport_client,remote_monitoring_collector,superuser,ingest_admin

MAINTAINER sandeep.rana(aimhigh.excel@gmail.com)