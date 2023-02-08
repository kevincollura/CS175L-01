'''
Kevin Collura
Professor Eckert
CS-175L
Restaurants
'''

anotherSearch='yes'
while anotherSearch== 'yes':

    vegetarian=False
    vegan=False
    glutenFree=False

    response1=input('Is anyone in your party a vegetarian? ')
    response1lower=response1.lower()
    if response1=='yes':
        vegetarian=True

    response2=input('Is anyone in your party a vegan?')
    response2lower=response2.lower()
    if response2=='yes':
        vegan=True

    response3=input('Is anyone in your party gluten free? ')
    response3lower=response3.lower()
    if response3=='yes':
        glutenFree=True

    print('Here are your restaurant choices:')

    if not vegetarian and not vegan and glutenFree:
        print("Joe's Gourmet Burger")

    elif not vegan and not glutenFree:
        print("Mama's Fine Italian")

    elif not vegan:
        print("Main Street Pizza")

    print("Corner Cafe")
    print("Chef's Kitchen")

    anotherSearch=input("Enter 'yes' if you would like to do another search (enter 'no' to end):")

