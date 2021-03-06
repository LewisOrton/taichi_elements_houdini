import bpy

from .. import base


def get_pos_value(socket):
    node = socket.node
    pos = node.inputs['Position']
    pos_key = '{0}.{1}'.format(node.name, pos.name)
    scn.elements_sockets[pos_key] = pos.get_value()


def get_vel_value(socket):
    node = socket.node
    vel = node.inputs['Velocity']
    vel_key = '{0}.{1}'.format(node.name, vel.name)
    scn.elements_sockets[vel_key] = vel.get_value()


def get_ang_value(socket):
    node = socket.node
    ang = node.inputs['Angular Velocity']
    ang_key = '{0}.{1}'.format(node.name, ang.name)
    scn.elements_sockets[ang_key] = ang.get_value()


def get_life_value(socket):
    node = socket.node
    life = node.inputs['Lifetime']
    life_key = '{0}.{1}'.format(node.name, life.name)
    scn.elements_sockets[life_key] = life.get_value()


class ElementsParticlesSystemNode(base.BaseNode):
    bl_idname = 'elements_particles_system_node'
    bl_label = 'Particles System'

    category = base.OUTPUT
    # particle system object name
    obj_name: bpy.props.StringProperty()

    get_value = {
        'Position': get_pos_value,
        'Velocity': get_vel_value,
        'Angular Velocity': get_ang_value,
        'Lifetime': get_life_value,
        'Size': get_pos_value
    }

    def init(self, context):
        self.width = 180.0

        # particle position
        pos = self.inputs.new('elements_vector_socket', 'Position')
        pos.text = 'Position'
        pos.hide_value = True

        # particle velocity
        vel = self.inputs.new('elements_vector_socket', 'Velocity')
        vel.text = 'Velocity'
        vel.hide_value = True

        # particle angular velocity
        ang_vel = self.inputs.new('elements_vector_socket', 'Angular Velocity')
        ang_vel.text = 'Angular Velocity'
        ang_vel.hide_value = True

        # particle lifetime
        lifetime = self.inputs.new('elements_float_socket', 'Lifetime')
        lifetime.text = 'Lifetime'
        lifetime.hide_value = True

        # particle size
        size = self.inputs.new('elements_float_socket', 'Size')
        size.text = 'Size'
        size.hide_value = True

    def draw_buttons(self, context, layout):
        layout.prop_search(self, 'obj_name', bpy.data, 'objects', text='')
