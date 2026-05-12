# 🌐 Full Stack Portfolio + Admin Panel (FastAPI + MongoDB + HTML)

This project is a **Full Stack Portfolio Web Application** built using **FastAPI (Python)** for the backend and **pure HTML/CSS/JS** for the frontend. It includes both a **public-facing landing page** and a simple **admin panel** to manage content and view form submissions.

---

## 📌 Features

### Public Landing Page
- ✅ View Projects
- ✅ View Clients
- ✅ Contact Form
- ✅ Newsletter Subscription

### Admin Panel
- 🛠 Add new Projects
- 🛠 Add new Clients
- 🛠 View Contact Submissions
- 🛠 View Newsletter Subscribers

### Backend API
- RESTful endpoints for all major operations
- Data stored in **MongoDB Atlas** or a self-hosted MongoDB instance

---

## 🛠️ Tech Stack

| Layer     | Technology                    |
|-----------|-------------------------------|
| Frontend  | HTML, CSS, JavaScript         |
| Backend   | Python FastAPI, CORS middleware |
| Database  | MongoDB Atlas or MongoDB      |
| HTTP API  | JSON-based RESTful Endpoints  |
| Tools     | Uvicorn, Docker, Postman      |

---

## ⚙️ Environment Variables

Create a local `.env` file from `.env.example` and set:

- `MONGO_URI` - MongoDB connection string
- `CORS_ORIGINS` - Comma-separated allowed browser origins
- `PORT` - Runtime port for local or containerized execution

## 📁 Folder Structure

- `main.py` - FastAPI application and API routes
- `index.html` - Frontend and admin panel UI
- `Dockerfile` - Production container build
- `.env.example` - Deployment and local environment template

---

## ▶️ How to Run the Project Locally

### 🔧 Prerequisites

- Python 3.12+
- pip
- MongoDB Atlas cluster or local MongoDB
- Docker, if you want to build and run the production image locally

---

### 🔌 Step-by-Step Instructions

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/fullstack-portfolio.git
cd fullstack-portfolio

#### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3️⃣ Configure Environment

Copy `.env.example` to `.env` and update the MongoDB connection string if needed.

#### 4️⃣ Run Locally

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

#### 5️⃣ Build the Production Container

```bash
docker build -t portfolio-app .
docker run -p 8000:8000 --env-file .env portfolio-app
```

## 🚀 Deployment Notes

- The app listens on the `PORT` environment variable, which makes it ready for container platforms.
- Set `MONGO_URI` to your production MongoDB instance before deploying.
- Open `/health` for a simple readiness check.


