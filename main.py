from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from pymongo import MongoClient
import os
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


# ------------------ App Setup ------------------
app = FastAPI(title="Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ MongoDB ------------------
MONGO_URI = "mongodb://localhost:27017"

client = MongoClient(MONGO_URI)
db = client["portfolio"]

projects_col = db["projects"]
clients_col = db["clients"]
contacts_col = db["contacts"]
newsletter_col = db["newsletter"]

# ------------------ Schemas ------------------
class Project(BaseModel):
    name: str
    description: str

class Client(BaseModel):
    name: str

class Contact(BaseModel):
    name: str
    email: EmailStr
    message: str

class Newsletter(BaseModel):
    email: EmailStr

# ------------------ Projects ------------------
@app.get("/api/projects")
def get_projects():
    return list(projects_col.find({}, {"_id": 0}))

@app.post("/api/projects", status_code=201)
def add_project(project: Project):
    projects_col.insert_one(project.dict())
    return {"message": "Project added"}

# ------------------ Clients ------------------
@app.get("/api/clients")
def get_clients():
    return list(clients_col.find({}, {"_id": 0}))

@app.post("/api/clients", status_code=201)
def add_client(client: Client):
    clients_col.insert_one(client.dict())
    return {"message": "Client added"}

# ------------------ Contact ------------------
@app.post("/api/contact", status_code=201)
def save_contact(contact: Contact):
    contacts_col.insert_one(contact.dict())
    return {"message": "Contact saved"}

@app.get("/api/contacts")
def get_contacts():
    return list(contacts_col.find({}, {"_id": 0}))

# ------------------ Newsletter ------------------
@app.post("/api/newsletter", status_code=201)
def subscribe(newsletter: Newsletter):
    newsletter_col.insert_one(newsletter.dict())
    return {"message": "Subscribed"}

@app.get("/api/newsletter")
def get_subscribers():
    return list(newsletter_col.find({}, {"_id": 0}))

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

