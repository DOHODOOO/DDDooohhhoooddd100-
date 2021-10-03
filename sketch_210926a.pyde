y=0
x=1000
z=700
def setup():
    size(1000,700)
    frameRate(50)
    strokeWeight(100)
def draw():
    global y,x,z
    background(random(0,255),random(0,255),random(0,255))
    point(y,y)
    y+=1
