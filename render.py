#Imports
import numpy
import pygame
from obj import Obj

#Classes
class Renderer():
    normal = numpy.array([0,0,1])
    light = numpy.array([0.5,-0.5,0.5])

    def __init__(self, obj, screen, offset):
        self.obj = obj
        self.screen = screen
        self.offset = offset

    def get_angle(self,n1,n2):
        mag1 = numpy.linalg.norm(n1)
        mag2 = numpy.linalg.norm(n2)
        angle = numpy.dot(n1, n2) / (mag1 * mag2)
        angle = numpy.degrees(angle)
        angle  = 90 - angle
        return angle

    #Render methods
    def draw_vertexs(self):
        for x,y,z in self.obj.vertexs:
            x += self.offset
            y += self.offset
            pygame.draw.circle(self.screen, self.obj.color, (x,y), 5, 5)

    def draw_edges(self):
        for start, stop in self.obj.edges:
            sx,sy,sz = self.obj.vertexs[start]
            xs,ys,zs = self.obj.vertexs[stop]
            sx += self.offset
            sy += self.offset
            xs += self.offset
            ys += self.offset
            pygame.draw.line(self.screen, self.obj.color, (sx,sy), (xs, ys), 5)

    def draw_faces(self):
        for i,(l,t,r,b) in enumerate(self.obj.faces):
            n2  = self.obj.normals[i]
            angle = self.get_angle(self.normal, n2)
            #print(f"Render:{i}")
            if (90 > angle):
                lx,ly,lz = self.obj.vertexs[l]
                tx,ty,tz = self.obj.vertexs[t]
                rx,ry,rz = self.obj.vertexs[r]
                bx,by,bz = self.obj.vertexs[b]

                lx += self.offset
                ly += self.offset
                tx += self.offset
                ty += self.offset
                rx += self.offset
                ry += self.offset
                bx += self.offset
                by += self.offset

                angle = abs(self.get_angle(self.light, self.obj.normals[i])*2)
                if (255 < angle):
                    angle = 255
                color = self.obj.color[0] - angle, self.obj.color[1] - angle, self.obj.color[2] - angle

                pygame.draw.polygon(self.screen, color, [(lx,ly),(tx,ty),(rx,ry),(bx,by)])
