def setup():
    size(1600,1200)
def draw():
    if mousePressed:
        fill(0)
    else:
        fill(255,255,0)
    ellipse(mouseX,mouseY,25,25)
