#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals

""" Various standard shapes demonstrates different ways of setting draw details
either prior to or while drawing.
The demo also shows setting a semitransparent background and using the String
and Ttffont classes (see /usr/share/fonts/truetype/ for other fonts)
"""
import demo

from pi3d import Display
from pi3d.Keyboard import Keyboard
from pi3d.Texture import Texture
from pi3d.context.Light import Light
from pi3d.Camera import Camera
from pi3d.Shader import Shader

from pi3d.shape.Cone import Cone
from pi3d.shape.Cylinder import Cylinder
from pi3d.shape.Extrude import Extrude
from pi3d.shape.Helix import Helix
from pi3d.shape.Lathe import Lathe
from pi3d.shape.Sphere import Sphere
from pi3d.shape.TCone import TCone
from pi3d.shape.Torus import Torus
from pi3d.shape.Tube import Tube
from pi3d.shape.Plane import Plane

from pi3d.util.String import String
from pi3d.util.Ttffont import Ttffont
from pi3d.util.Screenshot import screenshot

# Setup display and initialise pi3d

#DISPLAY = Display.create(w=1840, h=1130)
DISPLAY = Display.create()
DISPLAY.set_background(0.2, 0.0, 0.1, 0.3)      # r,g,b,alpha
#setup camera, light, shader
camera = Camera((0, 0, 5), (0, 0, -2), (1, 1000, 1.6, 1.2))
light = Light((5, 5, 1))
shader = Shader("shaders/uv_reflect")
flatsh = Shader("shaders/uv_flat")

# Load textures
patimg = Texture("textures/PATRN.PNG")
coffimg = Texture("textures/COFFEE.PNG")
shapebump = Texture("textures/floor_nm.jpg")
shapeshine = Texture("textures/stars.jpg")

#Create inbuilt shapes
mysphere = Sphere(camera, light, 1, 24, 24, 0.0,"sphere",-4, 2, 5)
mytcone = TCone(camera, light, 0.8,0.6,1,24,"TCone", -2, 2, 5)
myhelix = Helix(camera, light, 0.4, 0.1, 12, 24, 1.5, 3.0, "helix", 0, 2, 5)
mytube = Tube(camera, light, 0.4, 0.1, 1.5, 24, "tube",2, 2, 7, 30, 0, 0)
myextrude = Extrude(camera, light, ((-0.5, 0.5), (0.5,0.7), (0.9,0.2), (0.2,0.05), (1.0,0.0), (0.5,-0.7), (-0.5, -0.5)), 0.5,"Extrude", 4, 2, 5)
myextrude.buf[0].set_draw_details(shader, [coffimg, shapebump, shapeshine], 4.0, 0.2)
myextrude.buf[1].set_draw_details(shader, [patimg, shapebump, shapeshine], 4.0, 0.2)
myextrude.buf[2].set_draw_details(shader, [shapeshine, shapebump, shapeshine], 4.0, 0.2)

mycone = Cone(camera, light, 1,2,24,"Cone", -4, -1, 5)
mycylinder = Cylinder(camera, light, 0.7,1.5,24,"Cyli", -2, -1, 5)
myhemisphere = Sphere(camera, light, 1, 24, 24, 0.5, "hsphere", 0, -1, 5)
mytorus = Torus(camera, light, 1,0.3,12,24,"Torus", 2, -1, 5)
# NB Lathe needs to start at the top otherwise normals are calculated in reverse, also inside surfaces need to be defined otherwise normals are wrong
mylathe = Lathe(camera, light, ((0,1),(0.6,1.2),(0.8,1.4),(1.09,1.7), (1.1,1.7),(0.9, 1.4),(0.7,1.2),(0.08,1),(0.08,0.21),(0.1,0.2),(1,0.05),(1,0),(0,0)), 24,"Cup",4,-1, 5, 0,0,0, 0.8, 0.8, 0.8)

myPlane = Plane(camera, light, 4, 4,"plane")
myPlane.translate(0, 0, 10)

arialFont = Ttffont("fonts/FreeMonoBoldOblique.ttf", "#dd00aa")   #load ttf font and set the font colour to 'raspberry'
mystring = String(font=arialFont, string="Now the Raspberry Pi really does rock")
mystring.set_shader(flatsh)


# Fetch key presses
mykeys = Keyboard()
angl = 0.0
# Display scene
while 1:
  DISPLAY.clear()
  camera.reset()

  mysphere.draw(shader, [patimg])
  mysphere.rotateIncY( 0.5 )

  myhemisphere.draw(shader, [coffimg])
  myhemisphere.rotateIncY( .5 )

  myhelix.draw(shader, [patimg])
  myhelix.rotateIncY(3)
  myhelix.rotateIncZ(1)

  mytube.draw(shader, [coffimg, shapebump, shapeshine], 4.0, 0.1)
  mytube.rotateIncY(3)
  mytube.rotateIncZ(2)

  # Extrude has different textures for each Buffer so has to use
  # set_draw_details() rather than having arguments passed to draw()
  myextrude.draw()
  myextrude.rotateIncY(-2)
  myextrude.rotateIncX(0.37)

  mycone.draw(shader, [coffimg])
  mycone.rotateIncY(-2)
  mycone.rotateIncZ(1)

  mycylinder.draw(shader, [patimg, shapebump, shapeshine], 4.0, 0.1)
  mycylinder.rotateIncY(2)
  mycylinder.rotateIncZ(1)

  mytcone.draw(shader, [coffimg])
  mytcone.rotateIncY(2)
  mytcone.rotateIncZ(-1)

  mytorus.draw(shader, [patimg, shapebump, shapeshine], 4.0, 0.6)
  mytorus.rotateIncY(3)
  mytorus.rotateIncZ(1)

  mylathe.draw(shader, [patimg])
  mylathe.rotateIncY(2)
  mylathe.rotateIncZ(1)

  myPlane.draw(shader, [coffimg])
  myPlane.rotateIncX(9)

  mystring.draw()
  mystring.rotateIncZ(0.5)

  k = mykeys.read()
  if k >-1:
    if k==112: screenshot("shapesPic.jpg")
    elif k==27:
      mykeys.close()
      DISPLAY.destroy()
      break

  DISPLAY.swapBuffers()
