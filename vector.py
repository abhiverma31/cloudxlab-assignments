import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self, new_vector):
        return Vector(self.x + new_vector.x, self.y + new_vector.y)
    def multiply(self, x):
        return Vector(self.x * x, self.y * x)
    def dist(self, position):
        return math.sqrt((self.x - position.x) ** 2 + 
                         (self.y - position.y) ** 2)
    def turn(self, theta):# counterclock wise
        #speed = math.sqrt(self.x ** 2 + self.y ** 2)
        speed = self.dist(Vector(0,0)) # origin and point of reference
        #cos_theta = math.cos(math.radians(theta))
        cos_theta1 = self.x / speed # theta1 is the angle of the initial position
        sin_theta1 = self.y / speed
        cosine_new_angle = cos_theta1 * math.cos(math.radians(theta)) - sin_theta1 * math.sin(math.radians(theta))
        sin_new_angle = sin_theta1 * math.cos(math.radians(theta)) + cos_theta1 * math.sin(math.radians(theta))
        return Vector(speed * cosine_new_angle, speed * sin_new_angle)
    
    
position = Vector(3, 4)
move = Vector(-2,3)
new_position = position.add(move)

new_position.dist(position)

wind1 = Vector(10,0)
move_wind1 = wind1.multiply(2)
new_position = new_position.add(move_wind1)

print(new_position.x,new_position.y)

wind2 = Vector(5,3)
move_wind2 = wind2.multiply(2)

new_position = new_position.add(move_wind2)
print(new_position.x,new_position.y)

pos = Vector(3,4)
print(pos.turn(30))