#Imports
import numpy
import math

#Classes
class Obj():
    pos = 0,0,0 #x,y,z
    center = 0,0,0
    color = 255, 255, 255
    vertexs = numpy.array([])
    edges = numpy.array([])
    faces = numpy.array([])
    normals = []

    def __init__(self):
        self.center = numpy.mean(self.vertexs, axis = 0)
        self.build_normals()

    def build_normals(self):
        self.normals = []
        for face in self.faces:
            p1, p2, p3 = self.vertexs[face[0]], self.vertexs[face[1]], self.vertexs[face[2]]
            v1, v2 = p2 - p1, p3 - p1
            normal = numpy.cross(v1, v2)
            normal = normal / numpy.linalg.norm(normal)
            self.normals.append(normal)

    def rotate(self,x_angle, y_angle, z_angle):
        x_mat = numpy.array([
                                [math.cos(x_angle), 0, math.sin(x_angle)],
                                [0, 1, 0],
                                [-math.sin(x_angle), 0, math.cos(x_angle)]
                            ])
        y_mat = numpy.array([
                                [1, 0, 0],
                                [0, math.cos(y_angle), -math.sin(y_angle)],
                                [0, math.sin(y_angle), math.cos(y_angle)]
                            ])
        z_mat = numpy.array([
                                [math.cos(z_angle), -math.sin(z_angle), 0],
                                [math.sin(z_angle), math.cos(z_angle), 0],
                                [0, 0, 1]
                            ])
        self.vertexs = numpy.dot(self.vertexs, x_mat)
        self.vertexs = numpy.dot(self.vertexs, y_mat)
        self.vertexs = numpy.dot(self.vertexs, z_mat)
        self.build_normals()

class Cube(Obj):
    # 400 unit cube centered on 0,0,0
    vertexs = numpy.array([#x,y,z
        [-200,-200,-200], [-200,200,-200], [200,-200,-200], [200,200,-200],#back face
        [-200,-200,200], [-200,200,200], [200,-200,200], [200,200,200]#front face
    ])
    edges = numpy.array([
                            [5,7], [7,6], [6,4], [4,5], #Front Face
                            [7,3], [3,2], [2,6], #Right Face
                            [3,1], [1,0], [0,2], #Back Face
                            [1,5], [4,0], #Left Face
                        ])
    faces = numpy.array([
                            [7,5,4,6], [0,1,3,2], #Front & Back
                            [7,6,2,3], [0,4,5,1], #Right & Left
                            [3,1,5,7], [0,2,6,4], #Top & Bottom
                        ])
