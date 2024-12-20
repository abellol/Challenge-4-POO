import math

class Point:
  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y

class Line:
  def __init__(self, start: Point, end: Point):
    self.start = start
    self.end = end

  def compute_length(self):
    dx = self.start.x - self.end.x
    dy = self.start.y - self.end.y
    return ((dx**2 + dy**2)**0.5)
  
  def compute_slope(self):
    dx = abs(self.start.x - self.end.x)
    dy = abs(self.start.y - self.end.y)
    return(f"The slope of the line with the x axis is {math.degrees(math.atan2(dy, dx))}°")

  def compute_horizontal_cross(self):
    point1 = self.start.y
    point2 = self.end.y
    return(f"Cross with x axis: {point1 * point2 < 0}")  
    
  def compute_vertical_cross(self):
    point1 = self.start.x
    point2 = self.end.x
    return(f"cross with y axis: {point1 * point2 < 0}")
  
  def dicretize_line(self, size):
    points = []
    scalex = 0
    scaley = 0
    dx = (self.end.x - self.start.x) / (size)
    dy = (self.end.y - self.start.y) / (size)
    for i in range(size):
      scalex += dx
      scaley += dy
      points.append((self.end.x - scalex, self.end.y - scaley))
    return points

class Shape:
  def __init__(self):
    pass

  def compute_area(self):
    ...
  
  def compute_perimeter(self):
    ...

class Rectangle(Shape):
  def __init__(self, width1: Line, height1: Line, width2: Line, height2: Line):
    super().__init__()
    self.width1 = width1
    self.height1 = height1
    self.width2 = width2
    self.height2 = height2

  def compute_area(self):
    return self.width1.compute_length() * self.height1.compute_length()
  
  def compute_perimeter(self):
    return (2 * self.height1.compute_length()) + (2 * self.width1.compute_length())
  
class Square(Shape):
  def __init__(self, width1: Line, height1: Line, width2: Line, height2: Line):
    super().__init__()
    self.width1 = width1
    self.height1 = height1
    self.width2 = width2
    self.height2 = height2
  
  def compute_area(self):
    return self.width1.compute_length() ** 2 
  
  def compute_perimeter(self):
    return 4 * self.width1.compute_length()
  

if __name__ == "__main__":

  #* RECTANGLE
  # First Line
  start1 = Point(0,0)
  end1 = Point(0,5)
  line1 = Line(start1, end1)

  # Second line
  start2 = Point(0,0)
  end2 = Point(4,0)
  line2 = Line(start2, end2)

  # Third line
  start3 = Point(4,0)
  end3 = Point(4,5)
  line3 = Line(start3, end3)

  # fourth line
  start4 = Point(0,5)
  end4 = Point(4,5)
  line4 = Line(start4, end4)

  rectangle1 = Rectangle(line1, line2, line3, line4)
  print(rectangle1.compute_area())
  print(rectangle1.compute_perimeter())  
  
  
  #* SQUARE
  # First Line
  start1 = Point(0,0)
  end1 = Point(0,5)
  line1 = Line(start1, end1)

  # Second line
  start2 = Point(0,0)
  end2 = Point(5,0)
  line2 = Line(start2, end2)

  # Third line
  start3 = Point(5,0)
  end3 = Point(5,5)
  line3 = Line(start3, end3)

  # fourth line
  start4 = Point(0,5)
  end4 = Point(5,5)
  line4 = Line(start4, end4)

  square1 = Square(line1, line2, line3, line4)
  print(square1.compute_area())
  print(square1.compute_perimeter())

