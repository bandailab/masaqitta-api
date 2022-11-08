from fastapi import APIRouter

router = APIRouter()

# User
@router.get("/users", tags=["users"])
async def list_users():
    pass

@router.get("/users/{user_id}", tags=["users"])
async def get_user():
    pass

@router.post("/users", tags=["users"])
async def create_user():
    pass

@router.put("/users/{user_id}", tags=["users"])
async def update_user():
    pass

@router.delete("/users/{user_id}", tags=["users"])
async def delete_user():
    pass
