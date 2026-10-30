# Jozi Buddy — a voice AI agent

A real-time voice agent you can actually talk to, built with Strands Bidi Agents and Amazon Nova Sonic.

## What it does

Jozi Buddy listens through your microphone and talks back through your speakers. It is a friendly, Johannesburg-based companion that chats casually and shares tips about the city. Audio flows both ways at once, so you can interrupt it mid-sentence.

## How it works

- **Strands Bidi Agents** (`BidiAgent`) run the bidirectional conversation loop.
- **Amazon Nova Sonic** (`BedrockNovaSonicModel`) handles speech-to-speech on Amazon Bedrock in `us-east-1`.
- **`AudioIO`** reads the microphone and plays the agent's voice, with echo cancellation turned on.

## Prerequisites

- Python 3.12 (Nova Sonic support in Strands requires 3.12+)
- A microphone and speakers (headphones are nicer)
- An AWS account with Amazon Nova Sonic model access enabled in Bedrock (`us-east-1`)
- AWS credentials configured locally (`aws configure`)
- PortAudio, needed by PyAudio. On macOS: `brew install portaudio`

## Setup

```bash
git clone https://github.com/Kutloano-Yende/jozi-voice-buddy.git
cd jozi-voice-buddy
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
aws configure
```

Then enable **Amazon Nova Sonic** in the Bedrock console under **Model access** (region `us-east-1`).

## Run it

```bash
python voice_agent.py
```

Say "Hi". Press **Ctrl+C** to end the chat.

## Run the tests

```bash
pip install pytest
pytest
```

The tests build the agent offline. They do not call AWS or open the microphone.

## Make it your own

Edit `SYSTEM_PROMPT` in [`voice_agent.py`](voice_agent.py) to change the agent's personality. Keep replies short, since this is a voice conversation. To change the voice, pass a different `voice=` argument to `BedrockNovaSonicModel` (for example `voice="tiffany"`).
