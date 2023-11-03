import pygame
import sys
import body
import time
import random

DT = .1
# b1 = body.Body(4, [50, 40], [0, 0])
# b2 = body.Body(4, [40, 50], [0, 0])
# b3 = body.Body(4, [40, 60], [0, 0])
# b4 = body.Body(4, [40, 80], [0, 0])
# bodies = [b1, b2, b3, b4]

bodies = []
for i in range(10):
  b_mass = 5
  b_vel = [0, 0]
  # b_mass = random.uniform(.1, 10)
  b_pos = [random.uniform(10,70), random.uniform(10,50)]
  # b_vel = [random.uniform(-1,1), random.uniform(-1,1)]
  bodies.append(body.Body(b_mass, b_pos, b_vel))

  

pygame.init()

# Set the screen dimensions
screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Point in Pygame")

# Define a color for your point
point_color = (255, 255, 255)  # Red in RGB format

# Define the point's coordinates
point_x, point_y = 400, 300  # Change these values to position the point

running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with a black background

    # Draw the point at the specified coordinates
    for n in range(int((DT * 1000) // 1)):
      body_deltas = []
      for body in bodies:
        body_delta = body.step_simulation(bodies, .001)
        body_deltas.append(body_delta)
      for i in range(len(body_deltas)):
        bodies[i].update_position(body_deltas[i])
    
    for body in bodies:
      if body.mass < 1:
        mass = 1
      elif body.mass > 10:
        mass = 10
      else:
        mass = body.mass // 1
      if body.get_x() > (screen_width / 10):
        body.set_x(0)
      elif body.get_x() < 0:
        body.set_x(screen_width)

      if body.get_y() > (screen_height / 10):
        body.set_y(0)
      elif body.get_y() < 0:
        body.set_y(screen_height)
    
      pygame.draw.circle(screen, point_color, (body.get_x() * 10, body.get_y() * 10), mass)


    pygame.display.flip()
    time.sleep(.01)

pygame.quit()
sys.exit()