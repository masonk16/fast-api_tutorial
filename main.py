from uuid import uuid4
from fastapi import FastAPI
from typing import List
from models import Gender, Roles, User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Jamilla", 
        last_name="Ahmed",
        gender=Gender.female,
        role=[Roles.student]
        ),
    User(
        id=uuid4(), 
        first_name="Kudya", 
        last_name="Makumboarimumvura",
        middle_name="Usavi",
        gender=Gender.male,
        role=[Roles.admin, Roles.user]
        ),

]

@app.get("/")
def root():
    return {"Hello": "Mason"}

@app.get("/api/v1/users")
def fetch_users():
    return db
