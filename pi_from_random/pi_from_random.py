import random

"""random_pi(data_count) derives π using the function random().

random.random() generates random float uniformly in the semi-open range [0.0, 1.0).
random_pi takes in an integer as how many random 2D data points to generate.
The 2D points should be within a 1X1 grid, inside the gird, if destance from the point 
to 0.0 is less than 1, then it's within the area of a quadrant. Since the points are
random, they should have the same likehood to land within the area of the quadrant
or outside to their area proportion.
area of the cirle / area of the square = data points in the cirle(data_in_circle) / data points in the square (data_in_square)
                v(πr ^ 2) / ((2r) ^ 2) = data_in_circle / data_in_square
                                 π / 4 = data_in_circle / data_in_square
                                     π = 4 * data_in_circle / data_in_square

    Typical usage example:

    foo = random_pi(100)
"""

def random_pi(data_count):
    data_in_circle = 0
    data_in_square = 0
    
    for data in range(data_count):
        random_x = random.random() # x coordinate of the data point
        random_y = random.random() # y coordinate of the data point

        #check if the data point is within the quadrant
        if (random_x ** 2 + random_y ** 2) < 1: # missing square root the random_x ** 2 + random_y ** 2 to get distance but this algo logic is the same and simplifed
            data_in_circle += 1 # count all data points within the circle
        else:
            data_in_square += 1 # only count the ones outside of the quadrant
            
    data_in_square += data_in_circle # count all the data points
    
    return 4 * data_in_circle / data_in_square
