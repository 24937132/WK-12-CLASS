
# ---------- Setup ----------
# Set canvas size (width, height) and initialize all elements
def setup():
    size(900, 600)   # Set window size to 900 pixels wide by 600 pixels tall
    smooth()         # Enable anti-aliasing for smoother graphics
    frameRate(60)    # Set animation to 60 frames per second
    init_bubbles(15) # Create 15 bubbles at start


# ---------- Global Color Variables ----------
ROCK_GRAY    = color(90, 95, 105)    #colour of rock
c1           = color(0, 150, 200)   # light blue (top)
c2           = color(0, 50, 100)    # dark blue (bottom)

# ---------- Global Data Lists ----------
bubbles      = []  # List to store all bubble data
fishes       = []  # List to store all fish data

# ---------- Main Draw Loop ----------
# This function runs continuously (about 60 times per second) to animate everything
# The order matters: background first, then sand, rocks, bubbles, and fish on top
def draw():
    drawBackground()    # 1) Water background gradient
    drawSand()          # 2) Sand on top of background
    drawRocks()         # 3) Rocks on top of sand
    drawSeaweed()       # 4) Seaweed plants
    drawCoral()         # 5) Coral decorations
    drawStarfish()      # 6) Starfish on rocks and sand
    draw_bubbles()      # 7) Animated bubbles
    drawFish()          # 8) Draw all moving fish


# ---------- Background ----------
# Water background ombre: Light blue at the top (shallower water), Dark blue at the bottom (deeper water)
# Achieved by drawing one thin horizontal line per row of pixels with color blended using lerpColor() from c1 to c2
def drawBackground():
    # Create a gradient from c1 → c2 by drawing many horizontal lines
    for y in range(height):
        amt = y / float(height)        # Goes from 0.0 at top → 1.0 at bottom
        c = lerpColor(c1, c2, amt)     # Blend between c1 and c2, the amt parameter is the amount to interpolate
        stroke(c)                      # Set the stroke (line color) to the blended color
        line(0, y, width, y)           # Draws multiple lines of the stroke to create ombre

# ---------- Sand ----------
def drawSand():
    fill(194, 178, 128)  # Sandy color
    rect(0, height - 100, width, 100)  # Area of the sand (bottom 100 pixels)

# ---------- Rocks ----------
# Draws a single rock using three layered shapes:
# 1) Soft shadow (darker ellipse below) for depth
# 2) Main rock body (grey ellipse)
# 3) Subtle highlight (light ellipse top-left) for a 3D, underwater sheen

def drawRocks():
    # Draws multiple rocks at different x-positions, heights, widths, and sizes
    drawRock(110, height - 85, 70, 35)
    drawRock(170, height - 82, 45, 25)
    drawRock(220, height - 78, 60, 30)
    drawRock(730, height - 80, 80, 38)
    drawRock(780, height - 84, 45, 22)

def drawRock(cx, cy, w, h):
    # cx = center x, cy = center y, w = width, h = height
    noStroke()
    fill(0, 0, 0, 40)                              # Shadow color (semi-transparent black)
    ellipse(cx, cy + h * 0.55, w * 0.9, h * 0.35)  # Shadow underneath the rock
    fill(ROCK_GRAY)                                # Main rock color
    ellipse(cx, cy, w, h)                          # Main rock body
    fill(255, 255, 255, 22)                        # Highlight color (semi-transparent white)
    ellipse(cx - w * 0.2, cy - h * 0.25, w * 0.35, h * 0.25)  # Highlight on top-left

#---------- Seaweed ----------
# Draws seaweed plants swaying gently at the bottom of the tank
def drawSeaweed():
    # Draw multiple seaweed plants at different positions
    drawOneSeaweed(80, height - 100, 60, color(34, 139, 34))   # Dark green seaweed
    drawOneSeaweed(280, height - 100, 70, color(50, 205, 50))  # Light green seaweed
    drawOneSeaweed(450, height - 100, 55, color(34, 139, 34))  # Dark green seaweed
    drawOneSeaweed(620, height - 100, 65, color(46, 125, 50))  # Medium green seaweed
    drawOneSeaweed(820, height - 100, 58, color(50, 205, 50))  # Light green seaweed

# Draws a single seaweed plant with gentle swaying motion
def drawOneSeaweed(x, y, tall, seaweed_color):
    # x = x position, y = starting y position (bottom), tall = height of seaweed
    # Sway amount changes over time using sin() function
    sway = sin(frameCount * 0.02) * 8  # Gentle side-to-side movement
    
    fill(seaweed_color)
    noStroke()
    
    # Draw seaweed as a series of overlapping ellipses going upward
    for i in range(5):
        offset = sway * (i / 5.0)  # Top sways more than bottom
        ellipse(x + offset, y - (tall / 5.0) * i, 12, tall / 4.0)

# ---------- Coral ----------
# Draws coral decorations on the sand
def drawCoral():
    # Draw multiple coral pieces at different positions
    drawOneCoral(350, height - 90, 30, color(255, 127, 80))   # Orange coral
    drawOneCoral(500, height - 85, 25, color(255, 105, 180))  # Pink coral
    drawOneCoral(680, height - 88, 28, color(255, 127, 80))   # Orange coral

# Draws a single coral decoration
def drawOneCoral(x, y, size, coral_color):
    # x = x position, y = y position, size = size of coral
    fill(coral_color)
    noStroke()
    
    # Draw coral as multiple circles branching upward
    ellipse(x, y, size * 0.8, size * 0.8)  # Base
    ellipse(x - size * 0.3, y - size * 0.4, size * 0.6, size * 0.6)  # Left branch
    ellipse(x + size * 0.3, y - size * 0.4, size * 0.6, size * 0.6)  # Right branch
    ellipse(x, y - size * 0.7, size * 0.5, size * 0.5)  # Top

# ---------- Starfish ----------
# Draws starfish on rocks and sand
def drawStarfish():
    # Draw multiple starfish at different positions
    drawOneStarfish(140, height - 70, 15, color(255, 140, 0))  # Orange starfish on rock
    drawOneStarfish(240, height - 65, 12, color(255, 99, 71))  # Red starfish
    drawOneStarfish(760, height - 68, 14, color(255, 140, 0))  # Orange starfish on rock

# Draws a single starfish
def drawOneStarfish(x, y, size, star_color):
    # x = x position, y = y position, size = size of starfish
    fill(star_color)
    noStroke()
    
    # Draw starfish as a center circle with 5 small arms
    ellipse(x, y, size, size)  # Center body
    
    # Draw 5 arms around the center
    for i in range(5):
        angle = TWO_PI / 5 * i  # Divide circle into 5 equal parts
        arm_x = x + cos(angle) * size * 0.8  # Position of arm
        arm_y = y + sin(angle) * size * 0.8
        ellipse(arm_x, arm_y, size * 0.6, size * 0.4)  # Small oval arm
        
        
# ---------- Bubbles ----------
# Create n bubbles. If from_sand=True, spawn near the sand line
def init_bubbles(n=15, from_sand=True):
    global bubbles
    bubbles = []
    for _ in range(n):
        x = random(width)  # Random x position across the tank
        if from_sand:
            y = random(height - 100, height)  # Bubbles rise from the sand area near the bottom
        else:
            y = random(height)                # Bubbles can start anywhere in the tank
        r = random(8, 20)                     # Random bubble size (radius)
        bubbles.append(Bubble(x, y, r))       # Add new bubble to the list

def draw_bubbles():
    # Loop through every bubble in the list
    for b in bubbles:
        b.update()   # Moves the bubble upward
        b.display()  # Draw the bubble

class Bubble:
    # Defines a single bubble object with position, size, speed, and movement
    def __init__(self, x, y, r):
        # Position and size of bubble
        self.x = x  # X position
        self.y = y  # Y position
        self.r = r  # Radius (size)
        self.speed = random(0.6, 1.6)  # How fast this bubble rises
        self.phase = random(TWO_PI)  # For gentle side drift

    def update(self):
        # Moves the bubbles upward and adds gentle side to side drift
        self.y -= self.speed  # Move up
        self.x += sin(frameCount * 0.03 + self.phase) * 0.4  # Drift sideways
        # Reset bubbles to the bottom once it reaches the top
        if self.y < -self.r:
            self.y = height  # Reset to bottom
            self.x = random(width)  # New random x position

    def display(self):
        # Draws the bubbles to be transparent with white outline
        noFill()  # Outer bubble outline (no fill)
        stroke(255, 200)  # White stroke with transparency
        ellipse(self.x, self.y, self.r, self.r)  # Draw bubble circle

        noStroke()  # Adds a smaller white highlight to create dimension
        fill(255, 255, 255, 120)  # Semi-transparent white
        ellipse(self.x - self.r*0.25, self.y - self.r*0.25, self.r*0.45, self.r*0.45)  # Draw highlight on upper-left of bubble

# ---------- Fish ----------
def drawFish():
 # Draw preset (built-in) fish that always swim across the screen.
    # frameCount increases automatically each frame, so multiplying it by
    # a small number (like 0.9 or 1.2) makes each fish move at a different speed.
    # The % width wraps them back to the left side when they reach the right edge.
    drawOneFish((150 + frameCount * 0.9)  % width, 200, 40, color(255, 182, 193))
    drawOneFish((400 + frameCount * 0.8)  % width, 150, 45, color(200, 162, 200))
    drawOneFish((650 + frameCount * 0.9)  % width, 220, 38, color(173, 216, 230))
    drawOneFish((300 + frameCount * 1.0)  % width, 350, 42, color(255, 182, 193))
    drawOneFish((550 + frameCount * 1.2)  % width, 300, 40, color(173, 216, 230))
    drawOneFish((750 + frameCount * 1.15) % width, 180, 43, color(200, 162, 200))
    drawOneFish((200 + frameCount * 0.95) % width, 420, 39, color(173, 216, 230))
    drawOneFish((500 + frameCount * 0.98) % width, 450, 41, color(255, 182, 193))

   # Draw all user-added fish.
    # Each fish in the list 'fishes' has a dictionary with its own position, color, size, and speed.
    for f in fishes:
        # Move the fish to the right by its speed each frame
        f["x"] = (f["x"] + f["speed"]) % width  # % width wraps around the screen
        # Draw the fish at its new position
        drawOneFish(f["x"], f["y"], f["size"], f["col"])

# ---------- Draw One Fish ----------
def drawOneFish(x, y, size, fish_color):
    # Draw the fish body
    fill(fish_color)
    noStroke()
    ellipse(x, y, size, size * 0.6)  # Main oval body (wider than tall)

    # Draw the tail as a triangle behind the body
    triangle(x - size*0.5, y,
             x - size*0.7, y - size*0.25,
             x - size*0.7, y + size*0.25)

    # Draw a small black eye near the front of the fish
    fill(0)
    ellipse(x + size*0.2, y - size*0.1, size*0.15, size*0.15)

# ---------- Add Fish ----------
def addFish():
    # Create a new fish with random position, size, color, and speed.
    # Each fish is stored as a dictionary (a set of labeled data).
    f = {
        "x": random(width),                           # random horizontal start position
        "y": random(120, height - 140),               # random vertical position (avoid sand)
        "size": random(34, 52),                       # random size between 34 and 52 pixels
        "col": color(random(150,255), random(140,220), random(150,255)),  # random color
        "speed": random(0.8, 1.6)                     # random swimming speed
    }
    # Add this new fish to the global list
    fishes.append(f)

# ---------- Key Control ----------
def keyPressed():
    # This function runs whenever any key is pressed.
    # If the spacebar (' ') is pressed, it will add a new fish.
    if key == ' ':
        addFish()
