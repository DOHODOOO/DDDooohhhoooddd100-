x=0
y=0
#чтобы вращать фигуру вокруг центра нам нужно 1.с помощью транслэит сместить начало координат в центре будущей фигуры 
#2нарисовать в начале координат в новой системе
#3rotate-поворот системы координат
def setup():
    size(1000,1000,)#rotate(radians(30))
    frameRate(100000000000000000)
    background(255,155,235)
def draw():
    global x,y
    stroke(0)
    translate(500,500)#1
    rotate(radians(x))#2
    ellipse(0,0,30,50)
    fill(random(0,255),random(0,255),random(0,255))
    rect(100,50,30,30)
    stroke(random(0,255),random(0,255),random(0,255))
    line(0,0,100,50)
    x=x+1
    stroke(0)
    ellipse(0,0,30,50)
    fill(random(0,255),random(0,255),random(0,255))
    rect(100,50,30,30)
    stroke(random(0,255),random(0,255),random(0,255))
    line(0,0,100,50)
    y=y-1
