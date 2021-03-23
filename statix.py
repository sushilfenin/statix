#!/usr/bin/python3 

class Statix():
    
    def mean(*args):
        sum = int()
        for i in range(len(args)):
            sum += args[i]
        mean = sum/len(args)
        print("MEAN: ", mean)

    def mean_deviation(*args):
        sum = int()
        for i in range(len(args)):
            sum += args[i]
        mean = sum/len(args)
        sum2 = int()
        for i in range(len(args)):
            sum2 += abs(args[i]-mean)
        mean_deviation = sum2/len(args)
        print("MEAN DEVIATION: ", mean_deviation)

    def median(*args):
        list = sorted(args)
        if len(list)%2 == 0:
            median = (list[round(len(list)/2)-1] + list[round(len(list)/2)])/2
            print("MEDIAN: ", median)
        else: 
            median = list[len(list)/2]
            print("MEDIAN: ", median)

    def variance(*args):
        square_sum = int()
        for i in range(len(args)):
            square_sum += args[i]**2
        variance = (len(args)*square_sum-(sum(args)**2))/len(args)**2
        print("VARIANCE: ", variance)

    def stadard_deviation(*args):
        square_sum = int()
        for i in range(len(args)):
            square_sum += args[i]**2
        std_deviation = ((len(args)*square_sum-(sum(args)**2))/len(args)**2)**(1/2)
        print("STANDARD DEVIATION: ", std_deviation)
        
if __name__ == '__main__':
    Statix.mean(4, 7, 8, 9, 10, 12, 13, 17)
    Statix.mean_deviation(4, 7, 8, 9, 10, 12, 13, 17)
    Statix.median(13, 17, 16, 14, 11, 13, 10, 16, 11, 18, 12, 17)
    Statix.variance(6, 7, 10, 12, 13, 4, 8, 12)
    Statix.stadard_deviation(6, 7, 10, 12, 13, 4, 8, 12)
