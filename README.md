# AI Telegram Bot

AI-powered Telegram bot built with **Python**, **Aiogram 3**, and **Google Gemini API**. The bot supports context-aware conversations, image analysis, and asynchronous message processing.


## Overview

This project demonstrates the integration of Google's Gemini large language model into a Telegram bot using the Aiogram framework.

The bot is capable of:

* Generating AI responses to text messages
* Analyzing images sent by users
* Maintaining conversation history
* Handling multiple users asynchronously
* Securing sensitive configuration with environment variables


## Features

* Google Gemini API integration
* Context-aware conversations
* Image recognition and analysis
* Fully asynchronous architecture
* Environment variable configuration
* Modular project structure
* Easy to extend with new functionality


## Tech Stack

* Python 3
* Aiogram 3
* Google Gemini API
* asyncio
* python-dotenv


## Installation

Clone the repository:

```bash
git clone https://github.com/umani0/AIBot.git
cd AIBot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
TG_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run the application:

```bash
python AIBot.py
```


## Usage

1. Start the bot in Telegram.
2. Send a text message to receive an AI-generated response.
3. Upload an image for AI analysis.
4. Continue the conversation while preserving context.

## Implemented Functionality

* Telegram Bot API integration
* Google Gemini API integration
* Context-aware conversations
* Image analysis
* Asynchronous request handling
* Environment-based configuration
* Modular project architecture


## Project Goals

This project was created to gain practical experience with:

* AI application development
* Telegram bot development
* REST API integration
* Asynchronous programming in Python
* Working with Large Language Models (LLMs)
* Building scalable Python applications
