# Suivi-Depense

## Voici comment manipuler notre application 
$ python main.py add --description "Lunch" --amount 20
### Expense added successfully (ID: 1)

$ python main.py add --description "Dinner" --amount 10
### Expense added successfully (ID: 2)

$ python main.py list
### ID  Date       Description  Amount
#### 1   2024-08-06  Lunch        $20
###  2   2024-08-06  Dinner       $10

$ python main.py summary
### Total expenses: $30

$ python main.py delete --id 2
### Expense deleted successfully

$ python.main summary
### Total expenses: $20

$ python main.py summary --month 8
Total expenses for August: $20
