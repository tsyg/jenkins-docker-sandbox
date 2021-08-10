import json

import uvicorn
from fastapi import FastAPI

app = FastAPI()
DATA_DIR = "data"

# endpoints


@app.get("/users")
def users():
    return {
        "success": True,
        "data": get_users()
    }


@app.get("/users/{user_id}")
def user(user_id):
    return {
        "success": True,
        "data": get_user_by_id(user_id)
    }


# some concrete logic

def get_users():
    with open(f"{DATA_DIR}/users.json") as f:
        return json.load(f)


def get_user_by_id(user_id):
    with open(f"{DATA_DIR}/user{user_id}.json") as f:
        return json.load(f)


# run app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
