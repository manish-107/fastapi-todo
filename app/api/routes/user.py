from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def getAllUsers():
    return [{"name":"manish","age":30},{"name":"anish","age":20}]