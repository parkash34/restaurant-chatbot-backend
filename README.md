# 🍕 Restaurant Chatbot Backend

A FastAPI backend that powers an AI chatbot for an Italian restaurant.
Built on top of Groq's LLaMA 3.3 70B model — it answers questions about the menu,
reservations, and opening hours. Nothing else.

Each conversation is tracked by a session ID, so the bot remembers context
across messages without needing a database.

---

## ⚡ Tech Stack

| | |
|---|---|
| **Framework** | FastAPI |
| **AI Model** | LLaMA 3.3 70B via Groq API |
| **Language** | Python |
| **Memory** | In-memory per session |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/parkash34/restaurant-chatbot-backend.git
cd restaurant-chatbot-backend
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment
```bash
cp .env.example .env
```
Then open `.env` and add your Groq API key:
```
API_KEY=your_groq_api_key_here
```

### 4. Run the server
```bash
uvicorn main:app --reload
```

Server runs at `http://localhost:8000`

---

## 📡 API Usage

### `POST /restaurant-chat`

**Request body:**
```json
{
  "session_id": "user_123",
  "message": "What are your opening hours?"
}
```

**Response:**
```json
{
  "reply": "We are open Monday to Sunday, 11am to 10pm!"
}
```

> Each `session_id` keeps its own chat history, so the bot stays in context across messages.

---

## 📁 Project Structure

```
restaurant-chatbot-backend/
├── main.py            # FastAPI app, routes, and AI logic
├── requirements.txt   # Python dependencies
├── .env               # Your API key (never commit this)
├── .env.example       # Template for environment variables
├── .gitignore         # Ignores .env and pycache
└── README.md
```

---

## 👤 Author

**Om Parkash** — [LinkedIn](https://www.linkedin.com/in/om-parkash34) · [GitHub](https://github.com/parkash34)