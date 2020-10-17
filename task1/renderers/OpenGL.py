from OpenGL.GLU import *
import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr
from PIL import load_texture
from classes.ObjLoader import ObjLoader


def init():
    global xrot, yrot, ambient, greencolor, treecolor, lightpos
    xrot = .0
    yrot = .0
    ambient = (1., 1., 1., 1)
    greencolor = (.2, .8, .0, .8)
    treecolor = (.9, .6, .3, .8)
    lightpos = (1., 1., 1.)
    glClearColor(.2, .2, .2, 1)
    gluOrtho2D(-1., 1., -1., 1.)
    glRotatef(-90, 1., .0, .0)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)


def specialkeys(key, x, y):
    global xrot, yrot
    if key == glfw.KEY_UP:
        xrot -= 2.
    if key == glfw.KEY_DOWN:
        xrot += 2.
    if key == glfw.KEY_LEFT:
        yrot -= 2.
    if key == glfw.KEY_RIGHT:
        yrot += 2.


def start(color__):
    vertex_src = """
    # version 330
    layout(location = 0) in vec3 a_position;
    layout(location = 1) in vec2 a_texture;
    layout(location = 2) in vec3 a_normal;
    uniform mat4 model;
    uniform mat4 projection;
    uniform mat4 view;
    out vec2 v_texture;
    void main()
    {
        gl_Position = projection * view * model * vec4(a_position, 1.0);
        v_texture = a_texture;
    }
    """

    fragment_src = """
    # version 330
    in vec2 v_texture;
    out vec4 out_color;
    uniform sampler2D s_texture;
    void main()
    {
        out_color = texture(s_texture, v_texture);
    }
    """

    def window_resize(window, width, height):
        glViewport(0, 0, width, height)
        projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

    if not glfw.init():
        raise Exception("glfw can not be initialized!")
    window = glfw.create_window(1280, 720, "My OpenGL window", None, None)
    if not window:
        glfw.terminate()
        raise Exception("glfw window can not be created!")
    glfw.set_window_pos(window, 400, 200)
    glfw.set_window_size_callback(window, window_resize)
    glfw.make_context_current(window)
    chibi_indices, chibi_buffer = ObjLoader.load_model("resources/traffic_color.obj")
    shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER),
                            compileShader(fragment_src, GL_FRAGMENT_SHADER))
    VAO = glGenVertexArrays(2)
    VBO = glGenBuffers(2)
    glBindVertexArray(VAO[0])
    glBindBuffer(GL_ARRAY_BUFFER, VBO[0])
    glBufferData(GL_ARRAY_BUFFER, chibi_buffer.nbytes, chibi_buffer, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, chibi_buffer.itemsize * 8, ctypes.c_void_p(0))
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, chibi_buffer.itemsize * 8, ctypes.c_void_p(12))
    glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, chibi_buffer.itemsize * 8, ctypes.c_void_p(20))
    glEnableVertexAttribArray(2)
    glBindVertexArray(VAO[1])
    glBindBuffer(GL_ARRAY_BUFFER, VBO[1])
    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)
    glEnableVertexAttribArray(2)
    textures = glGenTextures(2)
    load_texture("resources/TextureR.png", textures[0])
    glUseProgram(shader)
    glClearColor(0, 0.1, 0.1, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280 / 720, 0.1, 100)
    chibi_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, -10]))
    view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 8]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))
    model_loc = glGetUniformLocation(shader, "model")
    proj_loc = glGetUniformLocation(shader, "projection")
    view_loc = glGetUniformLocation(shader, "view")
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
    while not glfw.window_should_close(window):
        if color__.s == "r":
            load_texture("resources/TextureR.png", textures[0])
        elif color__.s == "y":
            load_texture("resources/TextureY.png", textures[0])
        else:
            load_texture("resources/TextureG.png", textures[0])
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time())
        model = pyrr.matrix44.multiply(rot_y, chibi_pos)
        glBindVertexArray(VAO[0])
        glBindTexture(GL_TEXTURE_2D, textures[0])
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
        glDrawArrays(GL_TRIANGLES, 0, len(chibi_indices))
        glDrawElements(GL_TRIANGLES, len(chibi_indices), GL_UNSIGNED_INT, None)
        rot_y = pyrr.Matrix44.from_y_rotation(-0.8 * glfw.get_time())
        glfw.swap_buffers(window)
    glfw.terminate()