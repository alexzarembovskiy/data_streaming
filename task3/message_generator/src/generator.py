import sys
from confluent_kafka import Producer
import socket
import pandas as pd
import concurrent.futures
from urllib.parse import urlparse

def send(producer, message):
    producer.produce('domains', value=message)
    producer.flush()


def main():
    dev = pd.read_json("./src/History-Hoard.json")

    url_list = list(dev["URL"])

    domains = [urlparse(i).netloc.split(".")[-1] for i in url_list]
    try:
        conf = {
            'bootstrap.servers': "kafka-1:9092",
            'client.id': socket.gethostname()
        }

        producer = Producer(conf)

        messages = domains

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:

            futures = []
            for msg in messages:
                futures.append(executor.submit(send, producer=producer, message=msg))
            for future in concurrent.futures.as_completed(futures):
                future.result()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
