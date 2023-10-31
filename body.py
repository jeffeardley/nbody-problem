import math

class Body:
  def __init__(self, mass, x_init, y_init, velocity_vector_init):
    self.x = x_init
    self.y = y_init
    self.mass = mass
    self.velocity = velocity_vector_init

  def get_distance(self, x1, x2, y1, y2):
    return math.sqrt(((x1 - x2)**2 + (y1 - y2)**2))

  def get_r(self, other):
    r = self.get_distance(self.x, other.x, self.y, other.y)
    return r
  
  def scalar_multiply(x, vector):
    for n in vector:
      n *= vector
  
  def add_vectors(self, vectors, dimensions):
    vector_sum = []
    for i in range(dimensions):
      vector_sum.append(0)

    for vector in vectors:
      for i in range(dimensions):
        vector_sum[i] += vector[i]
  
  def find_gravitational_force(self, other):
    r = self.get_r(self, other)
    Force = (self.mass * other.mass) / (r**2)
    unit_vector = self.find_unit_vector(other)
    Force_vector = self.scalar_multiply(Force, unit_vector)
    return Force_vector
  
  def find_unit_vector(self, other):
    vector = [other.x - self.x, other.y - self.y]
    len_vector = self.get_distance(vector[0], 0, vector[1], 0)
    unit_vector = []
    unit_vector.append(vector[1] / len_vector, vector[1] / len_vector)
    return unit_vector
  
  def find_acceleration(self, total_force_vector):
    a = self.scalar_multiply(total_force_vector, 1/self.mass)
    return a
  
