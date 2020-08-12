# import openGL libs
import moderngl
import moderngl_window
from moderngl_window.scene.camera import OrbitCamera

# import own classes
from decorators import syntax_compatibility

# engine global variable
engine = None

# main window class
class Window(moderngl_window.WindowConfig):
    """Base class with built in 3D orbit camera support"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera = OrbitCamera(aspect_ratio=self.wnd.aspect_ratio)
        self.camera_enabled = True

    def key_event(self, key, action, modifiers):
        keys = self.wnd.keys

        if action == keys.ACTION_PRESS:
            if key == keys.C:
                self.camera_enabled = not self.camera_enabled
                self.wnd.mouse_exclusivity = self.camera_enabled
                self.wnd.cursor = not self.camera_enabled
            if key == keys.SPACE:
                self.timer.toggle_pause()

    def render(self, *args, **kwargs):
        # call loop on the global engine
        global engine
        engine.loop(*args, **kwargs)

    def mouse_position_event(self, x: int, y: int, dx, dy):
        if self.camera_enabled:
            self.camera.rot_state(dx, dy)

    def mouse_scroll_event(self, x_offset: float, y_offset: float):
        if self.camera_enabled:
            self.camera.zoom_state(y_offset)

    def resize(self, width: int, height: int):
        self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)

class Engine:

    camera_window = Window

    def __init__(self):
        pass

    def loop(self, time: float, frametime: float):
        """Main loop method."""
        

    def start(self):
        moderngl_window.run_window_config(self.camera_window)

# create engine and start it
engine = Engine()
engine.start()
