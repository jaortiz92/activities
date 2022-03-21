from fastapi import HTTPException, status


def register_not_found(register):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{register} does not exist"
    )


def register_without_cr_and_db():
    raise HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail="The register doesn't use a activity with CR and other with DB"
    )


def register_with_transactions(register, id):
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"The {register} with ID {id} has transactions active"
    )
