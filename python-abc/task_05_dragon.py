"""
This is module docstring
"""
#!/usr/bin/env python3

class SwimMixin: 
    """
    This is a class docstring
    """

    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """"""

    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """"""

    def roar(self):
        print("The dragon roars!")
