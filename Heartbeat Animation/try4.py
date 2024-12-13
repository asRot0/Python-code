import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random  # Import random module for random selection of markers


# Function to define the heart shape
def heart_shape(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y


# Generate particle positions around the heart
def generate_particles(n_particles):
    angles = np.random.uniform(0, 2 * np.pi, n_particles)
    radii = np.random.uniform(0.5, 1.5, n_particles)
    x = radii * 16 * np.sin(angles) ** 3
    y = radii * (13 * np.cos(angles) - 5 * np.cos(2 * angles) - 2 * np.cos(3 * angles) - np.cos(4 * angles))
    return x, y


# Generate triangle particle positions around the heart with random markers
def generate_triangle_particles(n_particles):
    angles = np.random.uniform(0, 2 * np.pi, n_particles)
    radii = np.random.uniform(0.5, 1.5, n_particles)
    x = radii * 16 * np.sin(angles) ** 3
    y = radii * (13 * np.cos(angles) - 5 * np.cos(2 * angles) - 2 * np.cos(3 * angles) - np.cos(4 * angles))

    # Randomly assign marker types to each particle
    markers = ['^', '<', '>', 'v']  # Available marker types
    marker_choices = [random.choice(markers) for _ in
                      range(n_particles)]  # Randomly select marker type for each particle
    return x, y, marker_choices


# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.axis('off')

# Initial plots
heart_line, = ax.plot([], [], color='pink', lw=2)
glow_lines = [ax.plot([], [], color='pink', lw=1, alpha=0.2)[0] for _ in range(5)]
particles, = ax.plot([], [], 'o', color='pink', alpha=0.6, markersize=2)
triangles = []  # List to hold the triangle markers

# Time array for heart shape
t = np.linspace(0, 2 * np.pi, 1000)

# Particle positions
n_particles = 60
particle_x, particle_y = generate_particles(n_particles)

# Triangle particles
n_triangle_particles = 20
triangle_x, triangle_y, triangle_markers = generate_triangle_particles(n_triangle_particles)

# Create individual plot objects for each triangle marker
for i in range(n_triangle_particles):
    triangle, = ax.plot([], [], marker=triangle_markers[i], color='pink', alpha=0.5, markersize=5)
    triangles.append(triangle)


# Animation function
def update(frame):
    scale = 1 + 0.1 * np.sin(frame / 10)  # Pulsating effect
    x, y = heart_shape(t)
    heart_line.set_data(scale * x, scale * y)

    # Update glow effect
    for i, glow in enumerate(glow_lines):
        glow_scale = scale * (1 + i * 0.05)
        glow.set_data(glow_scale * x, glow_scale * y)

    # Update circular particle positions
    particle_offset = 0.2 * np.sin(frame / 5)
    particles.set_data(particle_x + particle_offset, particle_y + particle_offset)

    # Update triangular particle positions with random markers
    triangle_offset = 0.2 * np.cos(frame / 5)
    for i in range(n_triangle_particles):
        triangles[i].set_data(triangle_x[i] + triangle_offset, triangle_y[i] + triangle_offset)

    return [heart_line, *glow_lines, particles, *triangles]


# Create the animation
anim = FuncAnimation(fig, update, frames=range(200), interval=50, blit=True)

# Display the animation
plt.show()
