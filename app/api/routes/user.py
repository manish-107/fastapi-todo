from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_all_users():
    return [{"name": "manish", "age": 30}, {"name": "anish", "age": 20}]