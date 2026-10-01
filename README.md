# Hayavo Meet Python SDK

Official Python SDK for **Hayavo Meet**.

Hayavo Meet provides APIs for building real-time communication applications including video conferencing, audio calling, real-time messaging, screen sharing, room management, participant management, and collaboration features.

The Python SDK provides a simple interface for integrating Hayavo Meet into your backend applications.

---

## Installation

Install the latest version from PyPI:

```bash
pip install hayavo-meet
```

Upgrade to the latest version:

```bash
pip install --upgrade hayavo-meet
```

---

## Requirements

* Python 3.9+
* Hayavo Meet API Key
* Hayavo Meet Application credentials:

  * App ID
  * App Secret
  * App Platform
  * App Identifier

### Supported Platforms

| Platform  | Identifier            |
| --------- | --------------------- |
| `web`     | Domain name           |
| `android` | Android package name  |
| `ios`     | iOS bundle identifier |

Python 3.11+ is recommended for production applications.

---

## Getting Started

### 1. Create a Hayavo Meet Application

Create an application from your Hayavo Meet dashboard.

You will receive:

* API Key
* App ID
* App Secret
* App Platform
* App Identifier

Keep your API Key and App Secret secure.

---

### 2. Initialize the Client

```python
from hayavo_meet import HayavoClient

client = HayavoClient(
    api_key="hayavo_meet_live_xxxxxxxxx",
    app_id="your_app_id",
    app_secret="your_app_secret",
    app_platform="web",
    app_identifier="client.example.com",
)
```

---

## Quick Start

### Create a Room

```python
room = client.rooms.create(
    room_name="my-room",
    max_participants=5,
)

print(room)
```

### Generate a Host Token

```python
token = client.rooms.generate_host_token(
    "my-room",
)

print(token)
```

### Generate a Guest Token

```python
token = client.rooms.generate_guest_token(
    "my-room",
    "app_id",
)

print(token)
```

The generated token can then be provided to your client application to authorize the participant to join the room.

---

# Authentication

Hayavo Meet API requests use your application credentials.

| Credential     | Description                                             |
| -------------- | ------------------------------------------------------- |
| API Key        | Authenticates your Hayavo Meet account                  |
| App ID         | Identifies your application                             |
| App Secret     | Application secret used for request authentication      |
| App Platform   | Application platform such as `web`, `android`, or `ios` |
| App Identifier | Platform-specific application identifier                |

## Security

**Never expose your API Key or App Secret in frontend or client-side applications.**

Store sensitive credentials on your backend server or in a secure secrets manager.

For example:

```text
Browser / Mobile App
        |
        | Your backend API
        v
Your Backend
        |
        | Hayavo Meet SDK
        v
Hayavo Meet API
```

Your frontend should not contain:

```text
API Key
App Secret
```

---

# Features

The Hayavo Meet Python SDK is designed to provide access to real-time communication functionality including:

* 🎥 Video calling
* 🎙️ Audio calling
* 🖥️ Screen sharing
* 🏠 Room management
* 📞 Call management
* 💬 Real-time communication
* 💬 Real-time chat
* 😀 Emoji and reactions
* 🖼️ Image sharing
* 📎 File and attachment sharing
* 👥 Participant management
* 🔐 Secure authentication
* 🛠️ Administrative APIs
* ⏱️ Context and timeout support
* 📦 Typed request and response models
* 🚀 Backend-friendly Python integration

> Availability of individual features depends on the installed SDK version and the APIs enabled for your Hayavo Meet application.

---

# Room Management

## Create a Room

```python
room = client.rooms.create(
    room_name="hm_default_meet_room",
    max_participants=5,
)

print(room)
```

You can use the returned room information to manage the session and generate participant authorization tokens.

---

## Generate a Host Token

```python
token = client.rooms.generate_host_token(
    "hm_default_meet_room",
)

print(token)
```

A host token authorizes a participant to join the specified room with host permissions.

---

## Generate a Guest Token

```python
token = client.rooms.generate_guest_token(
    "hm_default_meet_room",
    "app_id",
)

print(token)
```

Guest tokens can be used to authorize participants joining an existing room as guests.

---

# RTC Configuration

Hayavo Meet provides RTC connection information through the SDK client.

```python
print(client.rtc)
```

For example, after creating a room:

```python
room = client.rooms.create(
    room_name="hm_default_meet_room",
    max_participants=5,
)

print(client.rtc)
```

Your client application can use the RTC configuration when establishing the real-time communication connection.

---

# Error Handling

The SDK provides structured exceptions for handling API errors.

```python
from hayavo_meet import HayavoClient
from hayavo_meet.exceptions import HayavoMeetError

client = HayavoClient(
    api_key="hayavo_meet_live_xxxxxxxxx",
    app_id="your_app_id",
    app_secret="your_app_secret",
    app_platform="web",
    app_identifier="client.example.com",
)

try:
    room = client.rooms.create(
        room_name="hayavo-meet-room",
    )

    print(room)

except HayavoMeetError as exc:
    print(f"Hayavo Meet error: {exc}")
```

You can use exception handling to handle situations such as:

* Authentication failures
* Invalid credentials
* Invalid requests
* Room errors
* API errors
* Authorization failures
* Network/API communication errors

---

# Environment Variables

For production applications, avoid hard-coding credentials in your source code.

Set your credentials as environment variables:

```bash
export HAYAVO_API_KEY="hayavo_meet_live_xxxxxxxxx"
export HAYAVO_APP_ID="your_app_id"
export HAYAVO_APP_SECRET="your_app_secret"
export HAYAVO_APP_PLATFORM="web"
export HAYAVO_APP_IDENTIFIER="client.example.com"
```

Then initialize the SDK:

```python
import os

from hayavo_meet import HayavoClient

client = HayavoClient(
    api_key=os.environ["HAYAVO_API_KEY"],
    app_id=os.environ["HAYAVO_APP_ID"],
    app_secret=os.environ["HAYAVO_APP_SECRET"],
    app_platform=os.environ["HAYAVO_APP_PLATFORM"],
    app_identifier=os.environ["HAYAVO_APP_IDENTIFIER"],
)
```

For larger production deployments, consider using a secrets manager instead of plain environment configuration.

---

# Production Example

A simple backend integration can look like this:

```python
import os

from hayavo_meet import HayavoClient
from hayavo_meet.exceptions import HayavoMeetError


client = HayavoClient(
    api_key=os.environ["HAYAVO_API_KEY"],
    app_id=os.environ["HAYAVO_APP_ID"],
    app_secret=os.environ["HAYAVO_APP_SECRET"],
    app_platform=os.environ["HAYAVO_APP_PLATFORM"],
    app_identifier=os.environ["HAYAVO_APP_IDENTIFIER"],
)


try:
    room = client.rooms.create(
        room_name="customer-support-room",
        max_participants=5,
    )

    host_token = client.rooms.generate_host_token(
        "customer-support-room",
    )

    guest_token = client.rooms.generate_guest_token(
        "customer-support-room",
        "app_id",
    )

    print("Room:", room)
    print("Host token:", host_token)
    print("Guest token:", guest_token)

except HayavoMeetError as exc:
    print(f"Hayavo Meet error: {exc}")
```

---

# SDK Design

The SDK is organized around the Hayavo Meet client:

```text
HayavoClient
│
├── rooms
│   ├── create()
│   ├── generate_host_token()
│   └── generate_guest_token()
│
├── rtc
│
└── ...
```

This design allows additional Hayavo Meet services to be added without changing the main client interface.

---

# API Reference

Full API documentation is available at:

[Hayavo Meet Documentation](https://docs.meet.hayavo.com?utm_source=chatgpt.com)

The documentation contains detailed information about:

* Authentication
* Rooms
* Tokens
* RTC
* RTM
* Calls
* Participants
* API responses
* Exceptions
* Configuration
* Examples

---

# Repository

Source code and issue tracking are available on GitHub:

[Hayavo Meet Python SDK on GitHub](https://github.com/hayavo/hayavo-meet-python?utm_source=chatgpt.com)

---

# Reporting Issues

If you discover a bug, have a question, or want to request a feature, open an issue in the GitHub repository:

[Report an issue](https://github.com/hayavo/hayavo-meet-python/issues?utm_source=chatgpt.com)

When reporting a bug, include:

* SDK version
* Python version
* Operating system
* Minimal reproducible example
* Error message
* Relevant logs

Do not include API Keys, App Secrets, passwords, tokens, or other sensitive credentials.

---

# License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

## Hayavo Meet

Build real-time communication into your applications with **Hayavo Meet**.

**Video • Audio • Real-time Communication • Rooms • Collaboration**
