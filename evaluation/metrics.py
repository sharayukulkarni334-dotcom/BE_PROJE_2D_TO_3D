import trimesh

def evaluate_mesh(mesh_path):
    mesh = trimesh.load(mesh_path)

    metrics = {
        "num_vertices": len(mesh.vertices),
        "num_faces": len(mesh.faces),
        "watertight": mesh.is_watertight
    }

    return metrics
