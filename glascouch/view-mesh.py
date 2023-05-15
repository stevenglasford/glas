import pygmsh
import meshio

mesh = meshio.read("file.msh")
geom = pygmsh.built_in.Geometry()

# Define the nodes
nodes = []
for i in range(mesh.points.shape[0]):
    nodes.append(geom.add_point(mesh.points[i], mesh.point_data["gmsh:physical"][i]))

# Define the elements
element_type = list(mesh.cells.keys())[0] # assume only one element type in the mesh
elements = []
for i in range(mesh.cells[element_type].shape[0]):
    element_points = []
    for j in range(mesh.cells[element_type].shape[1]):
        node_index = mesh.cells[element_type][i][j]
        element_points.append(nodes[node_index])
    elements.append(geom.add_polygon(element_points, mesh.cell_data["gmsh:physical"][i]))

# Define the edges
edges = []
if "line" in mesh.cells:
    for i in range(mesh.cells["line"].shape[0]):
        edge_points = []
        for j in range(mesh.cells["line"].shape[1]):
            node_index = mesh.cells["line"][i][j]
            edge_points.append(nodes[node_index])
        edges.append(geom.add_line(edge_points))

# Define the faces
faces = []
if "quad" in mesh.cells:
    for i in range(mesh.cells["quad"].shape[0]):
        face_points = []
        for j in range(mesh.cells["quad"].shape[1]):
            node_index = mesh.cells["quad"][i][j]
            face_points.append(nodes[node_index])
        faces.append(geom.add_polygon(face_points))

# Generate the mesh
mesh = geom.generate_mesh()

num_nodes = len(nodes)
num_elements = len(elements)
num_edges = len(edges)
num_faces = len(faces)

