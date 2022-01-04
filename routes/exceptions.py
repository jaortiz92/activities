from fastapi import HTTPException, status


def not_found(string):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=string
    )


def activity_not_exist():
    not_found("activity_id does not exist")


def transaction_not_exist():
    not_found("transaction_id does not exist")


def account_not_exist():
    not_found("account_id does not exist")
