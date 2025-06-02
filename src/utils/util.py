import math

def calculate_collision ( x_1,y_1,x_2,y_2 ):
    distance = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1 , 2))
    if distance < 27:
        return True
    else:
        return False