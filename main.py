import argparse

from depense.service import (
    add_expense,
    list_expenses,
    delete_expense,
    summary
)


parser = argparse.ArgumentParser(
    description="Expense Tracker"
)


sub = parser.add_subparsers(
    dest="command"
)


# -------------------
# ADD
# -------------------

add = sub.add_parser("add")

add.add_argument(
    "--description",
    required=True
)

add.add_argument(
    "--amount",
    type=float,
    required=True
)


# -------------------
# LIST
# -------------------

sub.add_parser("list")


# -------------------
# DELETE
# -------------------

delete = sub.add_parser("delete")

delete.add_argument(
    "--id",
    type=int,
    required=True
)


# -------------------
# SUMMARY
# -------------------

summ = sub.add_parser("summary")

summ.add_argument(
    "--month",
    type=int,
    required=False
)


args = parser.parse_args()


# ======================
# Traitement commandes
# ======================


if args.command == "add":

    expense = add_expense(
        args.description,
        args.amount,
        "Other"
    )

    print(
        f"Expense added successfully (ID: {expense['id']})"
    )


elif args.command == "list":

    expenses = list_expenses()

    print(
        "ID Date Description Amount"
    )

    for e in expenses:

        print(
            e["id"],
            e["date"],
            e["description"],
            "$"+str(e["amount"])
        )


elif args.command == "delete":

    try:

        delete_expense(args.id)

        print(
            "Expense deleted successfully"
        )

    except ValueError as error:

        print(error)


elif args.command == "summary":

    total = summary(args.month)

    if args.month:

        print(
            f"Total expenses for month {args.month}: ${total}"
        )

    else:

        print(
            f"Total expenses: ${total}"
        )


else:

    parser.print_help()
