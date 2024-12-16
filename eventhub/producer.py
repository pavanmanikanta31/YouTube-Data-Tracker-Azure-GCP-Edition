import asyncio
import os
from dotenv import load_dotenv
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

# Load environment variables
load_dotenv()

EVENTHUB_CONNECTION_STRING = os.getenv("EVENTHUB_CONNECTION_STRING")
EVENTHUB_NAME = os.getenv("EVENTHUB_NAME")

if not EVENTHUB_CONNECTION_STRING or not EVENTHUB_NAME:
    raise ValueError("Please ensure EVENTHUB_CONNECTION_STRING and EVENTHUB_NAME are set in the .env file")

async def send_events():
    producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENTHUB_CONNECTION_STRING,
        eventhub_name=EVENTHUB_NAME
    )
    async with producer:
        event_data_batch = await producer.create_batch()
        event_data_batch.add(EventData("First event"))
        event_data_batch.add(EventData("Second event"))
        event_data_batch.add(EventData("Third event"))
        
        print("Sending events...")
        await producer.send_batch(event_data_batch)
        print("Events sent successfully!")

if __name__ == "__main__":
    print("EVENTHUB_CONNECTION_STRING:", EVENTHUB_CONNECTION_STRING)
    print("EVENTHUB_NAME:", EVENTHUB_NAME)
    print("CONSUMER_GROUP:", CONSUMER_GROUP)
    asyncio.run(send_events())