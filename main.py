import pickle


class PlayerCar:
    def __init__(self, carNumber, carName, carColor, carSpeed):
        self.number = carNumber
        self.name = carName
        self.color = carColor
        self.speed = carSpeed

    def display(self):
        print('The Car Specification')
        print('Car Number: {}\nCar Name: {}\nCar Color : {}\nCar Speed: {}'.format(self.number, self.name, self.color,
                                                                                   self.speed))


def serialization(car):
    with open('playerCar.txt', 'wb') as file:
        pickle.dump(car, file)
        print('Serialization completed')
        return


def deserialization(fileName):
    with open(fileName, 'rb') as file:
        carObject = pickle.load(file)
        print('Deserialization completed\n')
        carObject.display()
        return


def process():
    print('Please type number 1 or 2\n')
    print('1. Serialization \n2. Deserializaton\n ')
    choose = input(' ')
    if choose == '1':
        carNumber = input('Car Num? ')
        carName = input('Car Name? ')
        carColor = input('Car Color? ')
        carSpeed = input('Car speed? ')

        car1 = PlayerCar(carNumber, carName, carColor, carSpeed)
        car1.display()

        serialization(car1)
    elif choose == '2':
        openFile = input('Deserialize what file?')
        deserialization(openFile)

if __name__ == "__main__":
    process()