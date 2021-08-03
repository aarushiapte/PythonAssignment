#classes and oops
#Ques1

class Country:

    avg_population = 10000

    def __init__(self, country_name, country_code):
        self.country_name = country_name
        self.country_code = country_code

        if type(country_name) != str:
            raise ValueError("Country name should be a string")
        if type(country_code) != str:
            raise ValueError("Country code should be a string")
        if len(country_code) != 3:
            raise ValueError("Country code should be exactly 3 letters long")

    def country_short_form(self,country_name):
        self.country_name = country_name
        return self.country_name[:2].upper()

    @classmethod
    def is_densely_populated(cls, population):
        cls.population = population
        return population > cls.avg_population

    @staticmethod
    def world_avg_population(arr_country_population):
        return (sum(arr_country_population)/len(arr_country_population))

    @property
    def formatted_country_name(self):
        return self.country_name, '(', self.country_code, ')'

    @formatted_country_name.setter
    def formatted_country_name(self, name, code):
        self.country_name = name
        self.country_code = code

    @formatted_country_name.deleter
    def formatted_country_name(self):
        self.country_name = None
        self.country_code = None

count = Country("India", "IND")

print(count.country_short_form("India"))
print(count.is_densely_populated(20000))
print(count.world_avg_population([7000, 80000, 5500, 4000]))
count.country_name = "Australia"
count.country_code = "AUS"
print(count.country_name)


#Ques2
class Shapes:
    def __init__(self, area, sides):
        self.area = area
        self.sides = sides

    def get_area(self):
        return self.area

    def get_sides(self):
        return self.sides

class Triangles(Shapes):
    def __init__(self, area, sides, size):
        Shapes.__init__(self, area, sides)
        self.size = size

    def get_sides(self):
        return self.sides + 3

    def get_size(self):
        return self.size

class Quadrilaterals(Shapes):
    def __init__(self, area, sides, colour):
        Shapes.__init__(self, area, sides)
        self.colour = colour

    def get_sides(self):
        return self.sides + 4

    def get_colour(self):
        return self.colour

class derivedTriangle(Triangles):
    def __init__(self, area, sides, size, colour, shade):
        Triangles.__init__(self, area, sides, size)
        self.colour = colour
        self.shade = shade
        if area < 1:
            raise Exception("Area cannot be zero.")

    def get_size(self):
        self.size + 100

    def get_colour(self):
        return self.colour, " and ", self.shade

class derivedQuadrilaterals(Quadrilaterals):
    def __init__(self, area, sides, colour, shade, size):
        Quadrilaterals.__init__(self, area, sides, colour)
        self.size = size
        self.shade = shade
        if area < 1:
            raise Exception("Area cannot be zero.")

    def get_colour(self):
        return self.colour, " and ", self.shade

    def get_size(self):
        return self.size

objTri = derivedTriangle(100, 3,10, "Blue", "Light")
print(objTri.get_size())
print(objTri.get_area())
print(objTri.get_colour())
print((objTri.get_sides()))

objQuad = derivedQuadrilaterals(400, 4, "Green", "Lime", 30)
print(objQuad.get_colour())
print(objQuad.get_sides())
print(objQuad.get_size())
print(objQuad.get_area())




