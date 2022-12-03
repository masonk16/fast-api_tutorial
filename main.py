from uuid import UUID, uuid4
from fastapi import FastAPI
from typing import List
from models import Gender, Roles, User

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("bd7ef9e7-b56a-4cfa-9717-3a765c9c4189"), 
        first_name="Jamilla", 
        last_name="Ahmed",
        gender=Gender.female,
        role=[Roles.student]
        ),
    User(
        id=UUID("946d4dba-cb40-4453-b94d-572ffcebf800"), 
        first_name="Kudya", 
        last_name="Makumboarimumvura",
        middle_name="Usavi",
        gender=Gender.male,
        role=[Roles.admin, Roles.user]
        ),

]

@app.get("/")
def root():
    """Base route.
    Returns: a simple JSON response
    """
    return {"Hello": "Mason"}

@app.get("/api/v1/users")
def fetch_users():
    """Get users route.
    Returns: Full list of users in database.
    """
    return db

@app.post("/api/v1/users")
def create_user(user: User):
    db.append(user)
    return {"id": user.id}
