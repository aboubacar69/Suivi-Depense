from depense.storage import (
    load_expenses,
    save_expenses
)

from depense.models import create_expense


# Liste des dépenses
def list_expenses():

    return load_expenses()


# Ajout d'une dépense
def add_expense(description, amount, category):

    expenses = load_expenses()

    if amount <= 0:
        raise ValueError(
            "Amount must be positive"
        )

    new_id = len(expenses) + 1

    expense = create_expense(
        new_id,
        description,
        amount,
        category
    )

    expenses.append(expense)

    save_expenses(expenses)

    return expense


# Supprimer une dépense
def delete_expense(expense_id):

    expenses = load_expenses()

    new_list = [
        e for e in expenses
        if e["id"] != expense_id
    ]

    if len(new_list) == len(expenses):

        raise ValueError(
            "Expense not found"
        )

    save_expenses(new_list)

# Résumé total


def summary(month=None):

    expenses = load_expenses()

    if month:

        expenses = [
            e for e in expenses
            if int(e["date"].split("-")[1]) == month
        ]

    total = sum(
        e["amount"]
        for e in expenses
    )

    return total
