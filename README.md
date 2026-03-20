# 🍕 Restaurant Chatbot Backend

A lightweight AI-powered chatbot backend for an Italian restaurant — built with FastAPI and Groq's LLaMA 3.3 model. Handles menu questions, reservations, and opening hours with per-session memory.

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
pip install fastapi python-dotenv requests uvicorn
```

### 3. Set up environment
Create a `.env` file in the root:
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

> Each `session_id` maintains its own conversation history, so the bot remembers context across messages in the same session.

---

## 📁 Project Structure

```
restaurant-chatbot-backend/
├── main.py        # FastAPI app, routes, and AI logic
├── .env           # API key (never commit this)
└── .gitignore     # Make sure .env is listed here
```

---

## ⚠️ Important

Make sure your `.gitignore` includes:
```
.env
__pycache__/
```

Never push your API key to GitHub.

---

## 👤 Author

**Om Parkash** — [LinkedIn](https://www.linkedin.com/in/om-parkash-a93a87275) · [GitHub](https://github.com/parkash34)