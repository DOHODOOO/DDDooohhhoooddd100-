def setup():
    size(1000,700)
    background(135,155,245)
    strokeWeight(10)
    fill(1,100,10)
    frameRate(10000)
def draw():
    fill(random(0,255),random(0,255),random(0,255))
    triangle(random(0,1000),random(0,700),random(0,1000),random(0,700),random(0,1000),random(0,700))
