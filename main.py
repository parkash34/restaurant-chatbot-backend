import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

class Message(BaseModel):
    session_id : str
    message : str

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY is not set in the env.")

app = FastAPI()
memory = {}


def ask_ai(chat_history):
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": "llama-3.3-70b-versatile",
                "temperature": 0.7,
                "max_tokens": 500,
                "messages": [
                    {"role": "system", "content": "You are a friendly assistant for an Italian restaurant. Only answer questions about the menu, reservations, and opening hours. If asked anything unrelated, politely say you can only help with restaurant related questions."},
                    *chat_history
                ]
            },
            timeout=10
        )
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return "Connection error. Please check your network."
    except requests.exceptions.HTTPError as e:
        return f"API error: {e.response.status_code}"
    except Exception as e:
        return f"Something went wrong: {str(e)}"
    


@app.post("/restaurant-chat")
def restaurant_chat(message: Message):
   
   if not message.session_id.strip():
       return {"error": "Session ID is missing."}
   if not message.message.strip():
       return {"error": "Please type a message before sending."}
   
   session_id = message.session_id
   user_message = message.message

   if session_id not in memory:
        memory[session_id] = []
    
   memory[session_id].append({"role": "user", "content": user_message})
   ai_reply = ask_ai(memory[session_id])

   memory[session_id].append({"role": "assistant", "content": ai_reply})
   return {"reply": ai_reply}