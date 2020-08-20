from dot import Dot


class Dots:
    """A collection of dots."""
    def __init__(self, WIDTH, HEIGHT,
                 LEFT_VERT, RIGHT_VERT,
                 TOP_HORIZ, BOTTOM_HORIZ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TH = TOP_HORIZ
        self.BH = BOTTOM_HORIZ
        self.LV = LEFT_VERT
        self.RV = RIGHT_VERT
        self.SPACING = 75
        self.EAT_DIST = 50
        self.LEFT = "LEFT"
        self.RIGHT = "RIGHT"
        self.TOP = "TOP"
        self.BOTTOM = "BOTTOM"
        # Initialize four rows of dots, based on spacing and width of the maze
        self.top_row = [Dot(self.SPACING * i, self.TH)
                        for i in range(self.WIDTH//self.SPACING + 1)]
        self.bottom_row = [Dot(self.SPACING * i, self.BH)
                           for i in range(self.WIDTH//self.SPACING + 1)]
        self.left_col = [Dot(self.LV, self.SPACING * i)
                         for i in range(self.HEIGHT//self.SPACING + 1)]
        self.right_col = [Dot(self.RV, self.SPACING * i)
                          for i in range(self.HEIGHT//self.SPACING + 1)]

    def display(self):
        """Calls each dot's display method"""
        for i in range(0, len(self.top_row)):
            self.top_row[i].display()
        for i in range(0, len(self.bottom_row)):
            self.bottom_row[i].display()
        for i in range(0, len(self.left_col)):
            self.left_col[i].display()
        for i in range(0, len(self.right_col)):
            self.right_col[i].display()

    # PROBLEM 3: implement dot eating
    # BEGIN CODE CHANGES
    def eat(self, position, coordinate):  # You might want/need to pass arguments here.
        if position == self.LEFT:
            for i in self.left_col:
                if (abs(i.y - coordinate) <= self.EAT_DIST or
                    abs(i.y - coordinate) > self.HEIGHT):
                    self.left_col.remove(i)
        if position == self.RIGHT:
            for i in self.right_col:
                if (abs(i.y - coordinate) <= self.EAT_DIST or
                    abs(i.y - coordinate) > self.HEIGHT):
                    self.right_col.remove(i)
        if position == self.TOP:
            for i in self.top_row:
                if (abs(i.x - coordinate) <= self.EAT_DIST or
                    abs(i.x - coordinate) > self.WIDTH):
                    self.top_row.remove(i)
        if position == self.BOTTOM:
            for i in self.bottom_row:
                if (abs(i.x - coordinate) <= self.EAT_DIST or
                    abs(i.x - coordinate) > self.WIDTH):
                    self.bottom_row.remove(i)
    # END CODE CHANGES

    def dots_left(self):
        """Returns the number of remaing dots in the collection"""
        return (len(self.top_row) +
                len(self.bottom_row) +
                len(self.left_col) +
                len(self.right_col))
