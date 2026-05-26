# Star Wars Mini API Project

This is a beginner Python project that contains a small Flask API server and a Python client.

The API runs locally and provides Star Wars character data in JSON format. The client sends a request to the local API, receives the JSON response, and prints selected character information.

This project was created to practice APIs, HTTP requests, JSON, and basic client-server communication.

## Project Structure

    star_wars_api_project/
    │
    ├── server/
    │   ├── api_server.py
    │   └── requirements.txt
    │
    └── client/
        └── star_wars_api_fetcher.py



## Features

- Creates a local API using Flask
- Provides character data in JSON format
- Uses a Python client to request data from the API
- Reads JSON responses
- Handles request errors
- Allows the user to choose how many characters to display
- Prints character names and species

## Skills Practiced

- Python functions
- Flask basics
- REST API basics
- HTTP requests
- JSON data
- Error handling
- Loops
- User input
- Client-server communication

## Requirements

This project uses:

Flask
requests

## How to Run

First, start the API server:

python server/api_server.py

The server will run locally at:

http://127.0.0.1:5000

In a second terminal, run the client:

python client/star_wars_api_fetcher.py

## Example

How many Star Wars characters do you want? 5

Characters:
- Luke Skywalker (Human)
- Darth Vader (Human)
- Leia Organa (Human)
- Obi-Wan Kenobi (Human)
- Yoda (Unknown)
