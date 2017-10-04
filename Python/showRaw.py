import pygame

f=open("f.raw", "rb" )
data=f.read()
f.close()

def coord(pos, offset=0):
    return (pos[0]+pos[1]*resolution[0])*2 + offset

def getColor(pos, offset):
    if (0 <= coord(pos,offset)+2 < len(data)):
        pixel = data[coord(pos,offset)], data[coord(pos,offset) + 1], data[coord(pos,offset)+1]
        return(ord(pixel[0]), ord(pixel[0]), ord(pixel[0]))
    else:
        return(255,0,255)

def draw(screen, resolution, offset):
    for i in range(resolution[0]):
         for j in range(resolution[1]):
             screen.fill(getColor((i,j),offset),(i,j,1,1))

resolution = (640, 480)
offset = len(data) - (resolution[0] * resolution[1] *2)

print "data length: ", len(data), "expected:",coord((resolution[0]-1,resolution[1]-1))+2

assert len(data)>=coord((resolution[0]-1,resolution[1]-1))+2, (len(data),
                                coord(resolution[0]-1,resolution[1])+2)

screen=pygame.display.set_mode((resolution[0],resolution[1]+50))
pygame.init()
font = pygame.font.SysFont("Areal", 45)
pygame.display.flip()

running = True

draw(screen, resolution, offset)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            #screen = pygame.display.set_mode((event.w, event.h),
            #                                  pygame.RESIZABLE)
            resolution = event.w, event.h
            draw(screen, resolution, offset)
            pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                offset-=100
            elif event.key == pygame.K_RIGHT:
                offset+=100
            elif event.key == pygame.K_UP:
                offset -= 10
            elif event.key == pygame.K_DOWN:
                offset += 10
            elif event.key == pygame.K_a:
                offset += 1
            elif event.key == pygame.K_d:
                offset -= 1
            draw(screen, resolution, offset)
            pygame.display.flip()
        elif event.type == pygame.MOUSEMOTION:
            screen.fill((255,200,200),(0,resolution[1],resolution[0],50))
            screen.blit(font.render(str(event.pos)+": "+str(coord(event.pos,offset)),1,(0,50,50)),(0,resolution[1]))
            screen.fill(getColor(event.pos, offset), (resolution[0]-100, resolution[1], 50, 50))
            screen.fill(getColor(event.pos, offset+1), (resolution[0]-50, resolution[1], 50, 50))
            pygame.display.flip()
pygame.quit()
