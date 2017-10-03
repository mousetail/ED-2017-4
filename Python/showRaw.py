import pygame

f=open("f.raw", "rb" )
data=f.read()
f.close()


resolution = (640, 480)

print "data length: ", len(data), "expected:",resolution[0]*resolution[1]*2

assert len(data)>=resolution[0]*resolution[1]*2, (len(data), resolution[0]*resolution[1]*2)

screen=pygame.display.set_mode(resolution)
for i in range(resolution[0]):
    for j in range(resolution[1]):
        pixel = data[(i+j*resolution[0])*2], data[(i+j*resolution[0])*2 + 1]
        screen.set_at((i,j),(ord(pixel[0]), ord(pixel[1]), ord(pixel[0])))
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
