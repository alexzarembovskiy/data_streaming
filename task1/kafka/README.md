# Investigation of kafka CLI tools - Kafka part

### 1) How to launch docker compose with Kafka:

- Using terminal, in folder ./task1/kafka, execute *docker compose up -d* command.

### 2) Learn about the kafka cli tools - tasks and corresponding commands:

1. Create a topic
- docker exec kafka-1 kafka-topics --bootstrap-server kafka-1:9092 --create --topic quickstart
2. List of topics
- docker exec kafka-1 kafka-topics --bootstrap-server kafka-1:9092 --list
3. Send at least 10 simple text messages with the console producer
- docker exec --interactive --tty kafka-1 kafka-console-producer --bootstrap-server kafka-1:9092 --topic quickstart
4. Receive the messages with the console consumer
- docker exec --interactive --tty kafka-1 kafka-console-consumer --bootstrap-server kafka-1:9092 --topic quickstart --from-beginning
5. Delete the topic
- docker exec kafka-1 kafka-topics --bootstrap-server kafka-1:9092 --delete --topic quickstart

### 3) Screenshots:

Can be viewed in this folder, ./task1/kafka

### 4) Used resources 

- https://developer.confluent.io/quickstart/kafka-docker/#:~:text=Apache%20Kafka%C2%AE%20Quick%20Start%201%201.%20Set%20up,...%207%207.%20Stop%20the%20Kafka%20broker%20
- https://www.baeldung.com/ops/kafka-docker-setup