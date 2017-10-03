import pygame

f=open("f.raw")
data=f.read()
f.close()

print "data length: ", len(data)

resolution = (640, 480)
assert len(data)==resolution[0]*resolution[1]*2

screen=pygame.display.set_mode(resolution)
for i in range(resolution[0]):
    for j in range(resolution[1]):
        pixel = data[(i+j*resolution[0])*2]
        screen.set_at((i,j),(ord(pixel), ord(pixel), ord(pixel)))
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
