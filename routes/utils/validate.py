from .exceptions import (
    register_not_found, register_without_cr_and_db
)


def if_error_redirect_transaction(response):
    if response == "category":
        register_not_found("Category")
    if response == "description":
        register_not_found("Description")
    if response == "kind":
        register_not_found("Kind")
    if response == "origin":
        register_not_found("Origin")
    if response == "destiny":
        register_not_found("Destiny")


def if_error_redirect_activity(response):
    if response == "transaction":
        register_not_found("Transaction")
    if response == "account":
        register_not_found("Account")


def validate_cr_and_db(activity_one, activity_two):
    if activity_one["nature"] == activity_two["nature"]:
        register_without_of_cr_and_db()
