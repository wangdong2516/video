from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get('/get_user')
async def get_users():
    return {"username": "fakecurrentuser"}
