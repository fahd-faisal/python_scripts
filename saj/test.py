import pyglet

window = pyglet.window.Window()
image = '/home/fahd/Desktop/saj/saj_1.jpg'

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

pyglet.app.run()
