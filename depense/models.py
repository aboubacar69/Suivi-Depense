from datetime import date


def create_expense(
        id,
        description,
        amount,
        category="Other"
):

    return {

        "id": id,

        "description": description,

        "amount": amount,

        "date": str(date.today()),

        "category": category
    }
