from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='47.108.164.71:9092')
producer.send('my-topic', b'Hello, Kafka!')
