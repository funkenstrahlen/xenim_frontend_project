
from .example import Example as ExampleDefault

''' This class adds the settings which are not supposed to land in the version
    control.
'''


class Example(ExampleDefault):
    EXAMPLE_SECRET = "5K62rQSnc2"
