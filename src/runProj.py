import numpy as np
import matplotlib.pyplot as plt
import random 
import PSO

def runUAVSwarm(numParticles, numIterations, x, v, w, phi_p, phi_g, targetLocation):
    """
    Using PSO to do a search and rescue/find on a target location.
    Args:
        numParticles (int): how many particles per iteration
        numIterations (int): how many iterations do you want to run
        x (int): random value, negative and positive used in initializtion of particles
        v (int): random value, used as random initial velocities
        w (double): *must be between 0-1* self declared variables used in updating particle velocity
        phi_p (double): *must be between 0-1* self declared variables used in updating particle velocity
        phi_g (double): *must be between 0-1* self declared variables used in updating particle velocity
        targetLocation ([int, int]): must be in form np.array([int, int])
    """
    S = numParticles
    particles = []
    
    for s in range(S):
        x = np.random.uniform(-x, x, 2)
        v = np.random.uniform(-v, v, 2)
        particles.append(PSO.Particle(x, v, w, phi_p, phi_g, targetLocation))
    
    g = particles[0].x.copy()
    
    positionVals = []
    totalPoints = 0
    n = 0
    fig, ax = plt.subplots(figsize=(8,5))
    while n < numIterations:
        for particle in particles:
            particle.updateVelocity(g)
            particle.updatePosition()
            particle.updateValue(targetLocation)
            if particle.value < PSO.f(g, targetLocation):
                g = particle.x.copy()
                positionVals.append(g)
            ax.plot(particle.x[0], particle.x[1], 'o')
            totalPoints += 1
        n += 1
    print("The PSO flocked towards", positionVals[-1])
    print("The PSO started at", positionVals[0])
    print("The total amount of points generated")
    print(totalPoints)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Particle Swarm Optimization - Iterations')
    plt.show()
    
runUAVSwarm(10, 50, 50, 5, 0.8, 0.1, 0.1, np.array([-1, 1]))
        
