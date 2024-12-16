import asyncio
import os
from dotenv import load_dotenv
from azure.eventhub.aio import EventHubConsumerClient

# Load environment variables
load_dotenv()

EVENTHUB_CONNECTION_STRING = os.getenv("EVENTHUB_CONNECTION_STRING")
EVENTHUB_NAME = os.getenv("EVENTHUB_NAME")
CONSUMER_GROUP = os.getenv("CONSUMER_GROUP", "$Default")

if not EVENTHUB_CONNECTION_STRING or not EVENTHUB_NAME:
    raise ValueError("Please ensure EVENTHUB_CONNECTION_STRING, EVENTHUB_NAME, and optionally CONSUMER_GROUP are set in the .env file")

async def on_event(partition_context, event):
    print(f"Partition ID: {partition_context.partition_id}")
    print(f"Event received: {event}")
    print(f"Event data: {event.body_as_str()}")
    await partition_context.update_checkpoint(event)


async def consume_events():
    print("Initializing consumer...")

    consumer = EventHubConsumerClient.from_connection_string(
        conn_str=EVENTHUB_CONNECTION_STRING,
        consumer_group=CONSUMER_GROUP,
        eventhub_name=EVENTHUB_NAME
    )
    
    async with consumer:
        print("Consumer connected. Listening for events...")
        await consumer.receive(
            on_event=on_event, 
            starting_position="-1",  # Read from the beginning
            consumer_timeout=60  # Wait for at least 60 seconds
        )


if __name__ == "__main__":
    print("EVENTHUB_CONNECTION_STRING:", EVENTHUB_CONNECTION_STRING)
    print("EVENTHUB_NAME:", EVENTHUB_NAME)
    print("CONSUMER_GROUP:", CONSUMER_GROUP)
    asyncio.run(consume_events())
