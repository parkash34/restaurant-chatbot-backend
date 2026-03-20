# Restaurant Chatbot Backend

A conversational AI chatbot backend for an Italian restaurant 
built with FastAPI and Groq AI.

## Features
- Multi-session conversation memory
- Restaurant-specific AI responses
- Input validation and error handling

## Technologies
- Python
- FastAPI
- Groq API (LLaMA 3.3 70B)
- Pydantic
- python-dotenv

## Setup
1. Clone the repository
2. Create virtual environment — python -m venv env
3. Install dependencies — pip install -r requirements.txt
4. Create .env file and add your GROQ API key
5. Run server — uvicorn main:app --reload

## API Endpoint
POST /restaurant-chat
{
    "session_id": "user_1",
    "message": "Do you have vegetarian pizza?"
}

## Environment Variables
API_KEY=your_groq_api_key