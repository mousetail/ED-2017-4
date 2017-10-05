import pygame
import md5

f=open("test.raw", "rb" )
data=f.read()
f.close()

print "Hash: ","".join("{:2x}".format(ord(i)) for i in md5.new(data).digest())

def coord(pos, offset=0):
    return (pos[0]+pos[1]*resolution[0])*2 + offset

def getColor(pos, offset):
    if (0 <= coord(pos,offset)+2 < len(data)):
        x = (pos[0]//2) * 2
        try:
            pixel = [ord(data[coord((x,pos[1]),offset)+i]) for i in range(4)]
        except IndexError:
            return (255,0,255)
        color = YUVtoRGB422(pixel)
        return(color[pos[0]%2])
    else:
        return(255,0,255)

def YUVtoRGB422(color):
    y1=color[0]
    v=color[1]
    y2=color[2]
    u=color[3]
    return tuple(YUVtoRgb444(y1, u, v)),tuple(YUVtoRgb444(y2, u, v))
def YUVtoRgb444(y, u, v):
    r = 1.164*(y - 16) + 1.596*(u-128)
    g = 1.164*(y - 16) - 0.813*(v-128) - 0.391*(u-128)
    b = 1.164*(y - 16) + 1.596*(v-128)
    return ([max(0,min(int(i*0.8), 255)) for i in (r,g,b)])
    
def draw(screen, resolution, offset):
    for i in range(resolution[0]):
         for j in range(resolution[1]):
             screen.fill(getColor((i,j),offset),(i*2,j*2,2,2))

resolution = (640, 480)
offset = len(data) - (resolution[0] * resolution[1] *2)

print "data length: ", len(data), "expected:",coord((resolution[0]-1,resolution[1]-1))+2

assert len(data)>=coord((resolution[0]-1,resolution[1]-1))+2, (len(data),
                                coord((resolution[0]-1,resolution[1]))+2)

screen=pygame.display.set_mode((resolution[0]*2,resolution[1]*2+50))
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
            elif event.key == pygame.K_r:
                offset = 0
            elif event.key == pygame.K_t:
                offset = len(data) - (resolution[0] * resolution[1] * 2)
            draw(screen, resolution, offset)
            pygame.display.flip()
        elif event.type == pygame.MOUSEMOTION:
            screen.fill((255,200,200),(0,resolution[1]*2,resolution[0]*2,50))
            pos = coord([event.pos[i]//2 for i in range(2)],offset)
            if (0 < pos < len(data)):
                screen.blit(font.render(str(event.pos)+": "+hex(pos)+
                                    "("+",".join(str(ord(data[pos+i])) for i in range(4))+")",
                                    1,(0,50,50)),(0,resolution[1]*2))
            screen.fill(getColor([event.pos[i]//2 for i in range(2)], offset),
                        (resolution[0]*2-100, resolution[1]*2, 50, 50))
            screen.fill(getColor([event.pos[i]//2 for i in range(2)], offset+1),
                        (resolution[0]*2-50, resolution[1]*2, 50, 50))
            screen.fill(getColor([event.pos[i]//2 for i in range(2)], offset+2),
                        (resolution[0]*2-150, resolution[1]*2, 50, 50)) 
            pygame.display.flip()
pygame.quit()
