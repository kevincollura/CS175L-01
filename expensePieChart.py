'''
Kevin Collura
CS-175L
Expense Pie Chart
'''



import matplotlib.pyplot as plt


def main():
    file_name = open('expenses.txt', 'r')
    expenses = file_name.readlines()
    file_name.close

    for x in range(len(expenses)):
        expenses[x] = expenses[x].rstrip('\n')

    sliceLabels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc.']

    plt.pie(expenses, labels = sliceLabels)

    plt.title('Monthly Expenses')

    plt.show()

main()
