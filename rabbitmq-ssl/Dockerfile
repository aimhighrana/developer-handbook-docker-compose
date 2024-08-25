FROM rabbitmq:3.11

COPY rabbitmq.config /etc/rabbitmq/rabbitmq.config
COPY key.pem /home/cert/
COPY localhost.pem /home/cert/

RUN rabbitmq-plugins enable rabbitmq_management

# CMD /bin/bash rabbitmq-server