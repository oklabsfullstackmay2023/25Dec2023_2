#1. Function Defination is one time process
def myFavouriteCars(*cars):

    print(f'My Favorurite Car are')
    for car in cars:
        print(car)

    pass

#2. Function calling/invoking is many time process
myFavouriteCars('Alcazar', ' Endeavour', "Alturas G4", '''ScorpioN''')  #actualargument
