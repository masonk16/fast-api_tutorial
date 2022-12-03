from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from typing import List
from models import Gender, Roles, UpdateUser, User

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

@app.put("/api/v1/users/{user_id}")
def update_user(user_update: UpdateUser, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.role is not None:
                user.role = user_update.role  
            return
    raise HTTPException(
        status_code = 404,
        detail = f"User with id: {user_id} does not exist."
    )

@app.delete("/api/v1/users/{user_id}")
def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = f"User with id: {user_id} does not exist."
    )
