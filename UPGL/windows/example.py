import pyglet

class ExampleWindow(pyglet.window.Window):
    def __init__(self):
        super(ExampleWindow, self).__init__(
            1280,
            800,
            caption='Initial caption',
        )

        self.label = pyglet.text.Label('Hello, world!')

    def on_draw(self):
        self.clear()
        self.label.draw()
