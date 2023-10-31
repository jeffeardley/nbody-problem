import math

class Body:
  def __init__(self, mass, position_init, velocity_vector_init):
    self.position = position_init
    self.mass = mass
    self.velocity = velocity_vector_init

  def get_distance(self, x1, x2, y1, y2):
    return math.sqrt(((x1 - x2)**2 + (y1 - y2)**2))

  def get_x(self):
    return self.position[0]
  
  def get_y(self):
    return self.position[1]
  
  def get_position(self):
    return self.position
  
  def get_velocity(self):
    return self.velocity

  def get_r(self, other):
    r = self.get_distance(self.get_x(), other.get_x(), self.get_y(), other.get_y())
    return r
  
  def scalar_multiply(self, x, vector):
    if vector != None:
      for i in range(len(vector)):
        vector[i] *= x
    return vector
  
  def add_vectors(self, vectors, dimensions):
    vector_sum = []
    for i in range(dimensions):
      vector_sum.append(0)

    for vector in vectors:
      for i in range(dimensions):
        vector_sum[i] += vector[i]
    return vector_sum
  
  def find_gravitational_force(self, other):
    r = self.get_r(other)
    if r != 0:
      Force = (self.mass * other.mass) / (r**2)
      unit_vector = self.find_unit_vector(other)
      Force_vector = self.scalar_multiply(Force, unit_vector)
      return Force_vector
  
  def find_unit_vector(self, other):
    vector = [other.get_x() - self.get_x(), other.get_y() - self.get_y()]
    len_of_vector = self.get_distance(vector[0], 0, vector[1], 0)
    unit_vector = self.scalar_multiply(1/len_of_vector, vector)
    return unit_vector
  
  def find_acceleration(self, total_force_vector):
    a = self.scalar_multiply(1/self.mass, total_force_vector)
    return a
  
  def velocity_delta(self, acceleration_vector, time):
    delta = self.scalar_multiply(time, acceleration_vector)
    return delta
  
  def distance_delta(self, velocity_vector, time):
    delta = self.scalar_multiply(time, velocity_vector)
    return delta
  
  def update_velocity(self, velocity_delta):
    self.velocity[0] += velocity_delta[0]
    self.velocity[1] += velocity_delta[1]
  
  def update_position(self, position_delta_vector):
    self.position[0] += position_delta_vector[0]
    self.position[1] += position_delta_vector[1]

  def step_simulation(self, all_bodies, time):
    force_vectors = []
    for body in all_bodies:
      if body == self:
        continue
      force_vectors.append(self.find_gravitational_force(body))
    total_force_vector = self.add_vectors(force_vectors, 2)
    acceleration = self.find_acceleration(total_force_vector)
    v_delta = self.velocity_delta(acceleration, time)
    self.update_velocity(v_delta)
    self.update_position([self.velocity[0] * time, self.velocity[1] * time])
    return self.get_position(), self.get_velocity()

    
b1 = Body(1, [0, 0], [0, 0])
b2 = Body(1, [1, 1], [0, 0])

for i in range(1000):
  for n in range(100):
    b1.step_simulation([b1, b2], .001)
    b2.step_simulation([b1, b2], .001)
  print(b1.get_distance(b1.get_x(), b2.get_x(), b1.get_y(), b2.get_x()))
# bodies = [b1, b2]
# i = 0
# time_step = 1

# while True:
#   if i % 5 == 0:
#     for body in bodies:
#       print(body.get_position, body.get_velocity)
#   for body in bodies:
#     body.step_simulation(bodies, 1)
#   i += 1

