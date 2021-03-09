import bpy

UNIT = 1

# Defines a component, the most basic and abstract piece of a 3D building.
class Component:
    BASE_SIZE = [1,1,1]

    def __init__(self, location=[0,0,0], rotation=[0,0,0], scale=[1,1,1], chirality=[False,False,False]):
        self.location = location
        self.rotation = rotation
        self.scale = scale
        self.chirality = chirality

    def size(self):
        return [
            self.BASE_SIZE[0] * self.scale[0],
            self.BASE_SIZE[1] * self.scale[1],
            self.BASE_SIZE[2] * self.scale[2]
        ]

    # set the location of the component so its bottom is at z=0 (or given ground level).
    def rest_on_ground(self, ground_level=0):
        self.location[2] = ground_level + self.size()[2] / 4
        return self

    def build(self):
        print("HELLO WORLD! I AM A " + type(self).__name__)
        print("MY BASE SIZE IS: " + str(self.BASE_SIZE))
        print("MY SCALE IS: " + str(self.scale))
        print("MY SIZE IS: " + str(self.size()))
        return self

    def construct_cube(self):
        bpy.ops.mesh.primitive_cube_add(
            size=UNIT,
            enter_editmode=False,
            align='WORLD',
            location=self.location,
            scale=self.size()
        )
