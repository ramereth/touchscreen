from core.models import ScreenAnimation

class Slide(ScreenAnimation):
    template = "screen_animations/slide.js"
    
    
class Fade(ScreenAnimation):
    template = "screen_animations/fade.js"