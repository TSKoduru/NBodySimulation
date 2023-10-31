import numpy as np
import pygame as pg
import time

# Objective: Create a simulation of a 2D N-body system using pygame and numpy
# NOTE: This should be easily scalable to more bodies.

# Define some constants
G = 6.67408e-11 # m^3 kg^-1 s^-2
AU = (149.6e6 * 1000) # m

# Define some parameters
N = 1 # number of bodies
dt = 0.001 # time step
t = 0 # current time
softening = 0.01 # softening parameter
planetDensity = 5514 # kg/m^3 (Density of Earth, which we'll use to approximate the density of all planets)

# One pixel represents 1000 km

class Body:
    def __init__(self, mass, x, y, z, vx, vy, vz, color = None):
        self.mass = mass
        volume = self.mass / planetDensity # Calculate the volume of the planet
        self.radius = (3 * volume / (4 * np.pi))**(1/3) # Calculate the radius of the planet (Assuming it's a sphere)
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        # Random self color
        if not color: self.color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
        else: self.color = color

    def update(self, ax, ay):
        # if acceleration is suspiciously high, set it to 0
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.z += self.vz * dt
    
    def draw(self, screen):
        # First draw a white circle as a border with a slightly bigger radius
        pg.draw.circle(screen, (200, 200, 200), (int(self.x), int(self.y)), self.radius/1000 + 1)
        pg.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius/1000) # Use the density of Earth to calculate the radius of the planet
        if(len(positions[self][-1500:]) > 2):
            pg.draw.lines(screen, self.color, False, positions[self][-1500:], 2)

    def __str__(self):
        return "Mass: " + str(self.mass) + "\nPosition: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")\nVelocity: (" + str(self.vx) + ", " + str(self.vy) + ", " + str(self.vz) + "), Radius: " + str(self.radius)
    
    def intersecting(self, other):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2) <= self.radius + other.radius
    
def initBodies():
    bodies = [] # Keep track of all the bodies
    positions = dict() # Keep track of the paths they take to draw a trail later
    
    if N == 1:
        planet = Body(np.random.uniform(1e10, 2e16), np.random.uniform(20000, 200000), np.random.uniform(20000, 200000), 0, np.random.uniform(-1e2, 1e2), np.random.uniform(-1e2, 1e2), 0)
        bodies.append(planet)
        positions[planet] = []
        return bodies, positions
    
    for i in range(N):
        planet = Body(np.random.uniform(1e10, 2e16), np.random.uniform(0, 2000), np.random.uniform(0, 2000), 0, np.random.uniform(-1e2, 1e2), np.random.uniform(-1e2, 1e2), 0)
        bodies.append(planet)
        positions[planet] = []
    return bodies, positions

def getAcc( pos, mass, G, softening ):
	"""
    Calculate the acceleration on each particle due to Newton's Law 
	pos  is an N x 3 matrix of positions
	mass is an N x 1 vector of masses
	G is Newton's Gravitational constant
	softening is the softening length
	a is N x 3 matrix of accelerations
	"""
	# positions r = [x,y,z] for all particles
	x = pos[:,0:1]
	y = pos[:,1:2]
	z = pos[:,2:3]

	# matrix that stores all pairwise particle separations: r_j - r_i
	dx = x.T - x
	dy = y.T - y
	dz = z.T - z

	# matrix that stores 1/r^3 for all particle pairwise particle separations 
	inv_r3 = (dx**2 + dy**2 + dz**2 + softening**2)
	inv_r3[inv_r3>0] = inv_r3[inv_r3>0]**(-1.5)

	ax = G * (dx * inv_r3) @ mass
	ay = G * (dy * inv_r3) @ mass
	az = G * (dz * inv_r3) @ mass
	
	a = np.column_stack((ax,ay,az))
	return a

def addBody(body):
    # Add body to simulation
    global positionsStack, velocitiesStack, massStack, accelerationStack, N
    bodies.append(body)
    positions[body] = []
    positionsStack = np.vstack((positionsStack, np.array([body.x, body.y, body.z])))
    velocitiesStack = np.vstack((velocitiesStack, np.array([body.vx, body.vy, body.vz])))
    massStack = np.append(massStack, body.mass)
    accelerationStack = getAcc(positionsStack, massStack, G, softening)
    N += 1

def removeBody(body, positionsStack, velocitiesStack, massStack, accelerationStack, N):
    # Add body to simulation
    bodies.remove(body)
    positions.pop(body)

    positionsStack = np.vstack((positionsStack, np.array([body.x, body.y, body.z])))
    velocitiesStack = np.vstack((velocitiesStack, np.array([body.vx, body.vy, body.vz])))
    massStack = np.append(massStack, body.mass)
    accelerationStack = getAcc(positionsStack, massStack, G, softening)
    N -= 1

    return positionsStack, velocitiesStack, massStack, accelerationStack, N

def KCK(velocitiesStack, positionsStack, accelerationStack, massStack, dt):    # Update bodies with the step kick step kick method
    # (1/2) kick
    velocitiesStack += accelerationStack * dt/2.0
    
    # drift
    positionsStack += velocitiesStack * dt
    
    # update accelerations
    accelerationStack = getAcc( positionsStack, massStack, G, softening )
    
    # (1/2) kick
    velocitiesStack += accelerationStack * dt/2.0

    return velocitiesStack, positionsStack, accelerationStack

# Initialize bodies
bodies, positions = initBodies()

# Creating stacks of all the positions, velocities, and masses of the bodies for vectorized calculations
positionsStack = np.array([np.array([body.x, body.y, body.z]) for body in bodies])
velocitiesStack = np.array([np.array([body.vx, body.vy, body.vz]) for body in bodies])
massStack = np.array([body.mass for body in bodies])
accelerationStack = getAcc(positionsStack, massStack, G, softening)

sun = Body(1e19, 500, 500, 0, 0, 0, 0, (255, 255, 0))
addBody(sun)

# Initialize pygame
pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption("N-body simulation")
pg.font.init()

# Main loop
running = True
drawArrow = False
paused = False

while running:
    if paused: dt = 0
    else: dt = 0.001
    # Handle events
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            # On space, toggle the pause
            if event.key == pg.K_SPACE:
                paused = not paused

            # If r is hit, reset the simulation 
            if event.key == pg.K_r:
                N = 1
                bodies, positions = initBodies()
                positionsStack = np.array([np.array([body.x, body.y, body.z]) for body in bodies])
                velocitiesStack = np.array([np.array([body.vx, body.vy, body.vz]) for body in bodies])
                massStack = np.array([body.mass for body in bodies])
                accelerationStack = getAcc(positionsStack, massStack, G, softening)
                t = 0
                addBody(sun)


        if event.type == pg.MOUSEBUTTONDOWN:
            drawArrow = True
            startPos = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONUP:
            drawArrow = False
            mousePos = pg.mouse.get_pos()
            newBody = Body(np.random.uniform(1e10, 2e16), startPos[0], startPos[1], 0, mousePos[0] - startPos[0], mousePos[1] - startPos[1], 0)
            addBody(newBody)


    velocitiesStack, positionsStack, accelerationStack = KCK(velocitiesStack, positionsStack, accelerationStack, massStack, dt)        

    # update time
    t += dt

    # Update bodies
    for i in range(N):
        bodies[i].update(accelerationStack[i, 0], accelerationStack[i, 1])
        positions[bodies[i]].append((bodies[i].x, bodies[i].y))
                
    # Draw bodies
    screen.fill((0, 0, 0))
    for i in range(N):
        bodies[i].draw(screen)

    # Update time
    t += dt

    font = pg.font.SysFont('Calibri', 30)
    text = font.render(str(N - 1) + " bodies", False, (255, 255, 255))
    screen.blit(text, (50, 50))

    if drawArrow:
        # Draw an arror between the starting position and the current mouse position
        mousePos = pg.mouse.get_pos()
        pg.draw.line(screen, (255, 255, 255), startPos, mousePos, 3)

    pg.display.flip()


# Quit pygame
pg.quit()
