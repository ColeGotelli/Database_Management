from faker import Faker
import csv

faker = Faker()


def writeToCSV():
    with open(fileName, 'w') as csvfile:
        fieldnames = ['first_name', 'last_name', 'age', 'city', 'state', 'zip']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(int(numTuples)):
            writer.writerow(
                {
                'first_name': faker.first_name(),
                'last_name': faker.last_name(),
                'age': faker.random_int(min=18, max=75),
                'city': faker.city(),
                'state': faker.state(),
                'zip': faker.zipcode()
                }
            )

if __name__ =='__main__':

    fileName = raw_input('Enter the name of the file you wish to create (No need to include .csv): ')
    fileName = '../' + fileName + '.csv'
    numTuples = raw_input('Enter the number of tuples you would like: ')
    writeToCSV()
