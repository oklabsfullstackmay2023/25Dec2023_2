#1. Function Defination is one time process
def myFavoruiteFruits(*fruits):  #formalarguments

    print(f'My Favoruite Fruits are')
    for fruit in fruits:
        print(fruit)

    pass

#2. Function calling/invoking is many time process
myFavoruiteFruits("Apple", "Banana", "Papaya", 'Kiwi', '''Watermelon''' )  #actualargument