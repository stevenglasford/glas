import stl
import gmsh
import os
import math
import sys

gmsh.initialize(sys.argv)

# import the couch STL file into python
def createGeometryAndMesh():
    gmsh.clear()
    path = os.path.dirname(os.path.abspath(__file__))
    gmsh.merge(os.path.join('couch.stl'))

createGeometryAndMesh()

gmsh.model.geo.synchronize()

#Set the resolution of the mesh
# gmsh.model.mesh.field.add("Threshold", 2)
# gmsh.model.mesh.field.setNumber(2, "SizeMin", .07 / 30)
# gmsh.model.mesh.field.setNumber(2, "SizeMax", .07)
# gmsh.model.mesh.field.setNumber(2, "DistMin", .15)
# gmsh.model.mesh.field.setNumber(2, "DistMax", .5)
gmsh.option.setNumber("Mesh.MeshSizeMin", 7)
gmsh.option.setNumber("Mesh.MeshSizeMax", 7)


gmsh.model.mesh.generate()

gmsh.write("couch.msh")

gmsh.finalize()