3D Cube Prototype

This was a quick "One Day Build" challange. This took about 4 hours w/ coding & research.
The program starts with "main.py" & it displays a cube. The program start w/ rendering the vertexs, after a few seconds it changes to rendering the edges of the cube, followd by the faces.
Every thing is rendered by using the x & y cordinets and ignoring the z cordinets. This results is a simple easy render camera w/ a orthographic perspective (no perspective)
There is some hacked in backface culling by comparing the face normals with a camera vector & drawing the ones with a angle less then 90 degrees.
Also the lighting/shadows are done the same way by comparing the face normals with a light vector and adjusting the greyscale relitive to the angle.
The OBJ is also rotating slowly with some basic matrix math.

main.py
    This glues everything together & provides some minor logic (like switching the render mode as time goes on)

obj.py
    This provides an obj class with all the methods needed to "simulate" a object
    Also provides the cube class the holds all the hard coded data for the vertexs, edges, & faces

renderer.py
    This holds all the logic for taking a obj class (vertexs, edge & face modes) & rendering it to a pygame.screen
