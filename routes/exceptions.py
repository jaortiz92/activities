from fastapi import HTTPException, status


def register_not_found(register):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{register} does not exist"
    )
