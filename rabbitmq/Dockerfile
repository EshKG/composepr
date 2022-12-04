FROM rabbitmq:3.9
EXPOSE 4369 5671 5672 25672
RUN rabbitmq-plugins enable --offline rabbitmq_management
CMD ["rabbitmq-server"]
