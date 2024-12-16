from dotenv import load_dotenv
import os

load_dotenv(".env")

print("EVENTHUB_CONNECTION_STRING:", os.getenv("EVENTHUB_CONNECTION_STRING"))
print("EVENTHUB_NAME:", os.getenv("EVENTHUB_NAME"))
print("API_KEY:", os.getenv("API_KEY"))
