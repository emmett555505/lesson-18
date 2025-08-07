import random #importing module
import time

def getRandomDate(startDate, endDate): #defining function
    randomGenorator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate,dateFormat))

    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenorator * (endTime - startTime)
    randomDate = time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
#display result
print("random date = ",getRandomDate("1/1/2016", "12/12/2018"))