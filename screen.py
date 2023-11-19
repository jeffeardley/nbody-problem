import pygame
import sys
import body
import time
import random
import math


SIMULATION_SPEED = 10
SCALE_FACTOR = .1 # smaller means more zoomed out
SOLAR_MASS = 1000000
EARTH_MASS = SOLAR_MASS * .0000003
AU = 100
sun       = body.Body(SOLAR_MASS, [0, 0], [0, 0], color=(255, 255, 255), name='Sun')
mercury   = body.Body(EARTH_MASS / 18, [0, AU // 4], [0, 0], color=(255, 0, 0), orbit={'type': 'elyptical', 'mass': SOLAR_MASS, 'radius': AU // 4})
venus     = body.Body(EARTH_MASS, [0, AU // 2], [0, 0], color=(255, 255, 0), orbit={'type': 'elyptical', 'mass': SOLAR_MASS, 'radius': AU // 2})
earth     = body.Body(EARTH_MASS, [0, AU], [0, 0], color=(0, 180, 255), orbit={'type': 'elyptical', 'mass': SOLAR_MASS, 'radius': AU})
moon      = body.Body(EARTH_MASS / 3, [0, AU + (AU * .01)], [0, 0], color=(255, 255, 255), orbit={'type': 'circular', 'mass': earth.mass, 'radius': AU * .01 })
moon.update_velocity(earth.velocity)
mars      = body.Body(EARTH_MASS * (2/3), [0, 2 * AU], [0, 0], color=(255, 0, 0), orbit={'type': 'elyptical', 'mass': SOLAR_MASS, 'radius': 2 * AU})
jupiter   = body.Body(SOLAR_MASS / 1000, [0, 8 * AU], [0, 0], color=(150, 111, 51), orbit={'type': 'elyptical', 'mass': SOLAR_MASS, 'radius': 8 * AU})
saturn    = body.Body(SOLAR_MASS / 3000, [0, 16 * AU], [0, 0], color=(255, 255, 0), orbit={'type': 'elyptical', 'mass': SOLAR_MASS, 'radius': 16 * AU})
black_hole = body.Body(100 * SOLAR_MASS, [-10 * AU, -10 * AU], [AU, (1/2) * AU], color=(150,150,150), name='Black Hole')
bodies = [sun, mercury, venus, earth, mars, jupiter, saturn]
# bodies = []
# for i in range(10):
#   b_mass = random.uniform(99, 100)
#   b_vel = [0, 0]
#   # b_mass = random.uniform(.1, 10)
#   b_pos = [random.uniform(-5,5), random.uniform(-5,5)]
#   b_vel = [random.uniform(-5,5), random.uniform(-5,5)]
#   bodies.append(body.Body(b_mass, b_pos, b_vel, color=(255, 255, 255)))

  

pygame.init()

# Set the screen dimensions
screen_width, screen_height = 1500, 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Gravity Simulator")

# Define a color for your point
point_color = (255, 255, 255)  # Red in RGB format

running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with a black background

    # Draw the point at the specified coordinates
    for n in range(int((10 * SIMULATION_SPEED) // 1)):
      body_deltas = []
      for body in bodies:
        body_delta = body.step_simulation(bodies, .001)
        body_deltas.append(body_delta)
      for i in range(len(body_deltas)):
        bodies[i].update_position(body_deltas[i])
    
    for body in bodies:
      mass = ((( 3/4 ) * body.mass) ** (1/3))
      mass = (mass // 1) 
      if mass < 1:
        mass = 1
      if body.name == 'Sun':
         mass = ((AU // 4) * SCALE_FACTOR) * (1/2)
      if body.name == 'Black Hole':
        mass = ((AU // 4) * SCALE_FACTOR) * (1/2)



      # mass = 2
      # if body.get_x() > (screen_width / SCALE_FACTOR):
      #   body.set_x(0)
      # elif body.get_x() < 0:
      #   body.set_x(screen_width)

      # if body.get_y() > (screen_height / SCALE_FACTOR):
      #   body.set_y(0)
      # elif body.get_y() < 0:
      #   body.set_y(screen_height)
      point_pos = [body.get_x() * SCALE_FACTOR, body.get_y() * SCALE_FACTOR]
      point_pos[0], point_pos[1] = point_pos[0] + (screen_width / 2), point_pos[1] + (screen_height / 2)
    
      pygame.draw.circle(screen, body.color, point_pos, mass)


    pygame.display.flip()
    time.sleep(.01)

pygame.quit()
sys.exit()