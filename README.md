# Vision-Stream: SQS Service Testing Mini Project

## Overview

This project is designed to help test and simulate an AWS SQS-based architecture, similar to what is used in production environments. 

The goal is to send messages from a UI to a Lambda function via SQS, and receive response payloads back to the UI. SQS is chosen for its ability to target specific queues, unlike SNS which broadcasts to multiple topics.

## Features

- Simulate sending messages to an SQS queue
- Mock Lambda function to process messages
- Return response payloads to the UI
- Python-based implementation

## Architecture

1. **UI**: Sends messages to SQS
2. **SQS Queue**: Receives and stores messages
3. **Lambda Function (Mocked)**: Processes messages from SQS and returns responses
4. **UI**: Displays response payloads

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://github.com/charliermarsh/uv) for dependency management
- AWS credentials (if testing with real SQS)

### Installation

```bash
uv venv .venv
uv sync
```

### Running the Project

```bash
make dev
```

## Configuration

- SQS queue details can be set in environment variables or a config file.
- For local testing, AWS resources can be mocked using libraries like `moto`.

## Usage

- Start the service
- Use the UI or CLI to send a message
- Observe the response payload

## Contributing

Pull requests are welcome. For major changes, please open an issue first.

## License

MIT
