
# YouTube Data Tracker Project

This project leverages Azure Event Hub to track and process YouTube data efficiently. The solution uses Azure resources such as Event Hub Producer and Consumer to simulate data flow, enabling real-time data tracking and processing.

## Features
- Event-driven architecture using Azure Event Hub.
- Simulates YouTube data flow using a Producer and Consumer setup.
- Built-in support for environment variables for secure credential management.
- Fully configured for local development and deployment.

---

## Prerequisites

### Tools & Dependencies
- **Python** (>= 3.12)
- **Azure CLI**
- **Virtual Environment (venv)**
- Python libraries:
  - `azure-eventhub`
  - `python-dotenv`

### Azure Resources
- **Resource Group**: `youtube-data-tracker-rg`
- **Event Hub Namespace**: `youtube-tracker-ns`
- **Event Hub Instance**: `youtube-events`
- **Consumer Group**: `$Default` (Basic tier limitation)

---

## Installation

### Step 1: Clone the Repository
```bash
# Clone the repository to your local machine
git clone <repository-url>
cd youtube-data-tracker-azure
```

### Step 2: Set Up Virtual Environment
```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Configuration

### Step 1: Create `.env` File
Create a `.env` file in the root directory and populate it with the following values:

```env
EVENTHUB_CONNECTION_STRING="Endpoint=sb://<YourNamespace>.servicebus.windows.net/;SharedAccessKeyName=<KeyName>;SharedAccessKey=<Key>"
EVENTHUB_NAME="youtube-events"
```

Replace the placeholders with your Azure Event Hub details:
- `<YourNamespace>`: The name of your Event Hub namespace.
- `<KeyName>`: The name of the shared access key.
- `<Key>`: The shared access key value.

---

## Usage

### Step 1: Start the Producer
The Producer sends events to the Event Hub.

```bash
# Run the producer script
python eventhub/producer.py
```

You should see the following output:
```plaintext
Connection String Loaded: <Your Connection String>
Event Hub Name Loaded: youtube-events
Events sent successfully!
```

### Step 2: Start the Consumer
The Consumer reads events from the Event Hub.

```bash
# Run the consumer script
python eventhub/consumer.py
```

---

## Limitations
- **Basic Tier Limitation**: Only the default consumer group (`$Default`) is supported. For additional consumer groups, upgrade to the Standard tier.
- **Partition Count**: Set to 1 for Basic tier. For scalability, use the Standard or Premium tier.

---

## Upgrading to Standard Tier

If you need multiple consumer groups or higher throughput, upgrade your namespace to the Standard tier:

```bash
az eventhubs namespace update \
    --resource-group youtube-data-tracker-rg \
    --name youtube-tracker-ns \
    --sku Standard
```

---

## Troubleshooting

### Error: "Basic Tier Limitation"
**Issue**: Attempting to create additional consumer groups in the Basic tier.
**Solution**: Upgrade to Standard tier.

### Error: "Connection String Not Found"
**Issue**: The `EVENTHUB_CONNECTION_STRING` is missing or invalid.
**Solution**:
1. Verify your `.env` file has the correct values.
2. Ensure the namespace and Event Hub names match your Azure setup.

---

## Architecture Overview

1. **Producer**:
   - Sends events to the Event Hub.
   - Simulates YouTube event data flow.

2. **Consumer**:
   - Reads events from the Event Hub.
   - Processes the received event data.

---

## Azure CLI Commands

### Create Resource Group
```bash
az group create --name youtube-data-tracker-rg --location eastus
```

### Create Event Hub Namespace
```bash
az eventhubs namespace create \
    --name youtube-tracker-ns \
    --resource-group youtube-data-tracker-rg \
    --location eastus \
    --sku Basic
```

### Create Event Hub Instance
```bash
az eventhubs eventhub create \
    --name youtube-events \
    --namespace-name youtube-tracker-ns \
    --resource-group youtube-data-tracker-rg \
    --message-retention 1 \
    --partition-count 1
```

---

## References
- [Azure Event Hub Documentation](https://learn.microsoft.com/en-us/azure/event-hubs/)
- [Azure CLI Reference](https://learn.microsoft.com/en-us/cli/azure/)

---

