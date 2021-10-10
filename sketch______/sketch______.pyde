x=30
def setup():
    size(500,500)
    frameRate(100000000000000000000000000000000000000000000000000000000000000000)
def draw():
    global x
    translate(250,250)
    x=x-random(30,40)
    
    push()
    rotate(radians(x))
    fill(255,120,90)
    triangle(-10,-10,35,-50,0,-20)
    pop()

    push()
    rotate(radians(x))
    fill(90,255,120)
    triangle(-10,-10,35,-50,0,-20)
    pop()

    push()
    rotate(radians(x))
    fill(120,90,255)
    triangle(-10,-10,35,-50,0,-20)
    ellipse(0,0,30,30)
    pop()
