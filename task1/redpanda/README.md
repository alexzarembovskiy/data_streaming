# Investigation of kafka CLI tools - Redpanda part

### 1) How to launch docker compose with Redpanda:

- Using terminal, in folder ./task1/redpanda, execute *docker compose up -d* command.

### 2) Learn about the redpanda cli tools - tasks and corresponding commands:

1. Create a topic
- docker exec -it redpanda-0 rpk topic create chat-room
2. List of topics
- docker exec -it redpanda-0 rpk topic list
3. Send at least 10 simple text messages with the console producer
- docker exec -it redpanda-0 rpk topic produce chat-room
4. Receive the messages with the console consumer
- docker exec -it redpanda-0 rpk topic consume chat-room
5. Delete the topic
- docker exec -it redpanda-0 rpk topic delete chat-room

### 3) Screenshots

Can be viewed in this folder, ./task1/redpanda

### 4) Used resources 

- https://docs.redpanda.com/docs/get-started/quick-start/?num-brokers=three