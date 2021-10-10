x=30
def setup():
    size(1000,1000)
    frameRate(5)
    fill(255,140,90)
def draw():
    global x
    translate(500,500)
    rotate(radians(x))
    triangle(-10,-10,10,-10,0,-20)
    ellipse(0,0,30,30)
    x=x+30
