class Colors:
    DARK_GREY=(26,31,40)
    GREEN=(47,230,23)
    RED=(255,0,0)
    ORANGE=(226,116,17)
    YELLOW=(234,234,4)
    PURPLE=(166,0,247)
    CYAN=(21,204,209)
    BLUE=(0,0,255)
    WHITE=(255,255,255)
    DARKBLUE=(44,44,127)
    LIGHTBLUE=(59,85,162)
    @classmethod
    def get_cell_colors(cls):
        return [cls.DARK_GREY,cls.GREEN,cls.RED,cls.ORANGE,cls.YELLOW,cls.PURPLE,cls.CYAN,cls.BLUE]