import bpy

# Creates a simple floor.
def floor():
    print("FLOOR")
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(0,0,0))
    pl = bpy.context.object
    pl.name = 'ground'
    pl.scale = (10,10,0.1)
    bpy.ops.rigidbody.object_add(type='PASSIVE')

# Clears out all objects in the file.
def remove_all(type=None):
    print("REMOVE ALL")
    if type:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type=type)
        bpy.ops.object.delete()
    else:
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
