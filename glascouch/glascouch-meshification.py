import stl
import gmsh
import os
import math

gmsh.initialize()

# import the couch STL file into python
def createGeometryAndMesh():
    gmsh.clear()
    path = os.path.dirname(os.path.abspath(__file__))
    gmsh.merge(os.path.join(path, os.pardir, 'couch.stl'))

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate()

gmsh.write("GFG.msh")

if 'close' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()