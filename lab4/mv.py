import glm
import numpy
import pygame
import random
from OpenGL.GL import *
from OpenGL.GL.shaders import *


pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)

#dT = pygame.time.Clock()





# vertex_shader = """
# #version 460
# layout (location = 0) in vec3 a_position;
# layout (location = 1) in vec3 a_color;
# 
# uniform mat4 m;
# 
# out vec3 v_color;
# 
# float pulse(float val, float dst){
#     return floor(mod(val * dst, 1.0)+0.5);
# }
# 
# void main()
# {
#     vec3 dir = vec3(0, 1, 0);
# 
#     const float d = 5.0;
# 
#     float brightness = pulse(a_position.x, d) + pulse(a_position.y, d);
# 
#     vec3 color = mod(brightness, 2.0) > 0.5? vec3(0.0, 0.0, 0.0) : vec3(1.0, 1.0, 0.0);
# 
#     float diffuse = 0.5 + dot(dir, normalize(a_position));
#     //gl_FragColor = vec4(color * diffuse, 1.0f);
# 
#     gl_Position = m * vec4(a_position.x, a_position.y, a_position.z, 1.0f);
#     v_color = color * diffuse;
# 
# }
# 
# """


### vertex_shader = """
### #version 460
### layout (location = 0) in vec3 a_position;
### layout (location = 1) in vec3 a_color;
### # 
### uniform mat4 m;
### # 
### out vec3 v_color;
### # 
### float pulse(float val, float dst){
###     return floor(mod(val * dst, 1.0)+0.5);
### }
### 
### void main()
### {
###     vec3 dir = vec3(0, 1, 0);
### 
###     vec3 b_position = a_position;
### 
###     vec3 b_color = a_color;
### 
###     
### 
###     b_color = vec3(a_color.x , pulse(b_position.y, 10.0), a_color.z);
### 
###     gl_Position = m * vec4(a_position.x, a_position.y, a_position.z, 1.0f); 
###     v_color = b_color;
### }
### 
### """

vertex_shader = """
#version 460
layout (location = 0) in vec3 a_position;
layout (location = 1) in vec3 a_color;

uniform mat4 m;

out vec3 v_color;
out vec3 v_position;

void main()
{
    gl_Position = m * vec4(a_position.x, a_position.y, a_position.z, 1.0f);
    v_color = a_color;
    v_position = a_position;
}
"""


fragment_shader = """ 
#version 460

layout (location = 0) out vec4 outColor;

uniform vec3 c_alpha;

in vec3 v_color;
in vec3 v_position;



void main()
{
    //outColor = vec4(v_color.xyz , 1.0f);
    outColor = vec4(c_alpha , 1.0f);
}

"""

fragment_shader_2 = """ 
#version 460

layout (location = 0) out vec4 outColor;

uniform vec3 c_alpha;

in vec3 v_color;
in vec3 v_position;

float pulse(float val, float dst){
    return floor(mod(val * dst, 1.0)+0.5);
}

void main()
{
    //outColor = vec4(v_color.xyz , 1.0f);
    //outColor = vec4(c_alpha , 1.0f);
    vec3 b_position = v_position;
    //vec3 b_color = v_color;

    //b_color = vec3(v_color.x , pulse(b_position.y, 5.0), v_color.z);

    //outColor = vec4(b_color , 1.0f);
    outColor = vec4(c_alpha.x , pulse(v_position.y, 5.0), c_alpha.z , 1.0f);
}

"""

##### precision highp float;
##### varying vec3 fNormal;
##### uniform float time;
##### 
##### void main()
##### {
#####   float theta = time*20.0;
#####   
#####   vec3 dir1 = vec3(cos(theta),0,sin(theta)); 
#####   vec3 dir2 = vec3(sin(theta),0,cos(theta));
#####   
#####   float diffuse1 = pow(dot(fNormal,dir1),2.0);
#####   float diffuse2 = pow(dot(fNormal,dir2),2.0);
#####   
#####   vec3 col1 = diffuse1 * vec3(1,0,0);
#####   vec3 col2 = diffuse2 * vec3(0,0,1);
#####   
#####   gl_FragColor = vec4(col1 + col2, 1.0);
##### }


fragment_shader_3 = """
layout (location = 0) out vec4 outColor;

uniform vec3 c_alpha;

in vec3 v_color;
in vec3 v_position;

float pulse(float val, float dst){
    return floor(mod(val * dst, 1.0)+0.5);
}

void main()
{
    //outColor = vec4(v_color.xyz , 1.0f);
    //outColor = vec4(c_alpha , 1.0f);
    //vec3 b_position = v_position;
    //vec3 b_color = v_color;

    //b_color = vec3(v_color.x , pulse(b_position.y, 5.0), v_color.z);

    //outColor = vec4(b_color , 1.0f);
    vec4 o = vec4(pulse(v_position.x, 5.0) , pulse(v_position.y, 5.0), c_alpha.z , 1.0f);
    if (o.x == 1.0 && o.y == 1.0){
        o = vec4(0.0, 0.0, 0.0, 1.0);
    }
    outColor = o;

}


"""




compiled_vertex_shader = compileShader(vertex_shader, GL_VERTEX_SHADER)
compiled_fragment_shader = compileShader(fragment_shader, GL_FRAGMENT_SHADER)
shader = compileProgram(compiled_vertex_shader, compiled_fragment_shader)

compiled_fragment_shader_2 = compileShader(fragment_shader_2, GL_FRAGMENT_SHADER)
shader_2 = compileProgram(compiled_vertex_shader, compiled_fragment_shader_2)

compiled_fragment_shader_3 = compileShader(fragment_shader_3, GL_FRAGMENT_SHADER)
shader_3 = compileProgram(compiled_vertex_shader, compiled_fragment_shader_3)

#glUseProgram(shader)


vertex_data = numpy.array([
    -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
    0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
    0.0, 0.5, 0.0 , 0.0, 0.0, 1.0
], dtype=numpy.float32)

vertex_buffer_object = glGenBuffers(1)

glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)

glBufferData(GL_ARRAY_BUFFER, # tipo de datos
    vertex_data.nbytes, # tamaño de los datos
    vertex_data, # datos
    GL_STATIC_DRAW # tipo de uso
)

vertex_array_object = glGenVertexArrays(1)

glBindVertexArray(vertex_array_object)

# posicion
glVertexAttribPointer(
    0, # atributo
    3, # tamaño
    GL_FLOAT, # tipo de datos
    GL_FALSE, # normalizado
    6 * 4, # stride
    ctypes.c_void_p(0) # offset
)

glEnableVertexAttribArray(0)



#color
glVertexAttribPointer(
    1, # atributo
    3, # tamaño
    GL_FLOAT, # tipo de datos
    GL_FALSE, # normalizado
    6 * 4, # stride
    ctypes.c_void_p(12) # offset
)

glEnableVertexAttribArray(1)


def calcMatrix_Y(a):
    i = glm.mat4(1.0)
    translate = glm.translate(i, glm.vec3(0.0, 0.0, 0.0))
    rotate = glm.rotate(i, glm.radians(a), glm.vec3(0.0, 1.0, 0.0))
    scale = glm.scale(i, glm.vec3(1.0, 1.0, 1.0))

    model = translate * rotate * scale

    view = glm.lookAt(glm.vec3(0.0, 0.0, 5.0), glm.vec3(0.0, 0.0, 0.0), glm.vec3(0.0, 1.0, 0.0))

    #projection = glm.ortho(0.0, 800.0, 0.0, 600.0, 0.1, 100.0)
    projection = glm.perspective(glm.radians(45.0), WIDTH / HEIGHT, 0.1, 1000.0)
    print(projection)

    m  = projection * view * model

    glUniformMatrix4fv(glGetUniformLocation(shader, "m"), 1, GL_FALSE, glm.value_ptr(m))

def calcMatrix_X(a):
    i = glm.mat4(1.0)
    translate = glm.translate(i, glm.vec3(0.0, 0.0, 0.0))
    rotate = glm.rotate(i, glm.radians(a), glm.vec3(1.0, 0.0, 0.0))
    scale = glm.scale(i, glm.vec3(1.0, 1.0, 1.0))

    model = translate * rotate * scale

    view = glm.lookAt(glm.vec3(0.0, 0.0, 5.0), glm.vec3(0.0, 0.0, 0.0), glm.vec3(0.0, 1.0, 0.0))

    #projection = glm.ortho(0.0, 800.0, 0.0, 600.0, 0.1, 100.0)
    projection = glm.perspective(glm.radians(45.0), WIDTH / HEIGHT, 0.1, 1000.0)

    m  = projection * view * model

    glUniformMatrix4fv(glGetUniformLocation(shader, "m"), 1, GL_FALSE, glm.value_ptr(m))

def calc_Matrix(x, y, z):
    i = glm.mat4(1.0)
    translate = glm.translate(i, glm.vec3(0.0, 0.0, 0.0))
    rotate = glm.rotate(i, glm.radians(x), glm.vec3(1.0, 0.0, 0.0))
    rotate = glm.rotate(rotate, glm.radians(y), glm.vec3(0.0, 1.0, 0.0))
    scale = glm.scale(i, glm.vec3(1.0, 1.0, 1.0))

    model = translate * rotate * scale

    view = glm.lookAt(glm.vec3(0.0, 0.0, 5.0 + z), glm.vec3(0.0, 0.0, 0.0), glm.vec3(0.0, 1.0, 0.0))

    #projection = glm.ortho(0.0, 800.0, 0.0, 600.0, 0.1, 100.0)
    projection = glm.perspective(glm.radians(45.0), WIDTH / HEIGHT, 0.1, 1000.0)

    m  = projection * view * model

    glUniformMatrix4fv(glGetUniformLocation(shader, "m"), 1, GL_FALSE, glm.value_ptr(m))





glViewport(0, 0, WIDTH, HEIGHT)
running = True
glClearColor(0.1, 0.1, 0.1, 1.0)

c4, c5, c6 = 0.0, 0.0, 0.0

r_y = 0
r_x = 0
z = 0
color_op = 0
shader_op = 0
while running:
    press = pygame.key.get_pressed()
    glClear(GL_COLOR_BUFFER_BIT)

    s = shader
    
    if shader_op == 0:
        s = shader
    elif shader_op == 1:
        #print("shader 2")
        s = shader_2
    elif shader_op == 2:
        s = shader_3
    
    
    glUseProgram(s)

    c_alpha = None
    if color_op == 0:
        c_alpha = glm.vec3(1.0, 0.0, 0.0)
        #print("rojo")
    elif color_op == 1:
        c = random.random()
        c2 = random.random()
        c3 = random.random()
        c_alpha = glm.vec3(c, c2, c3)
    
    elif color_op == 2:
        c_alpha = glm.vec3(c4, c5, c6)
        if c_alpha == glm.vec3(0.0, 0.0, 0.0):
            c4 = 1.0
            c5 = 1.0
            c6 = 1.0
        elif c_alpha == glm.vec3(1.0, 1.0, 1.0):
            c4 = 0.0
            c5 = 0.0
            c6 = 0.0

    #c_location = glGetUniformLocation(
    #    shader, 
    #    "c_alpha"
    #
    
    glUniform3fv(glGetUniformLocation(s, "c_alpha"), 1, glm.value_ptr(c_alpha))
    ##print(glGetError())
    #glUniform3f(glGetUniformLocation(shader, "c_alpha"), c_alpha.x, c_alpha.y, c_alpha.z)

    

    if press[pygame.K_d]:
        r_y += 1
    if press[pygame.K_a]:
        r_y -= 1
    if press[pygame.K_w]:
        r_x += 1
    if press[pygame.K_s]:
        r_x -= 1

    if press[pygame.K_UP]:
        z += 0.05
    if press[pygame.K_DOWN]:
        z -= 0.05
    
    

    if press[pygame.K_t]:
        if shader_op > 2:
            shader_op = 0
        else:
            shader_op += 1
        

    if press[pygame.K_c]:
        color_op += 1
        if color_op > 2:
            color_op = 0


    pygame.time.delay(5)

    calc_Matrix(r_x, r_y, z)
    #calcMatrix_Y(r_y)
    #calcMatrix_X(r_x)


    pygame.time.wait(5)

    glDrawArrays(GL_TRIANGLES, 0, 3)

    #x = random.randint(0, WIDTH)
    #y = random.randint(0, HEIGHT)
    #screen.set_at((x, y), (255, 255, 255))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False