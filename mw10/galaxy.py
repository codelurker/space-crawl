#!/usr/bin/env python

import random
import math
import body
import station
import star

class Galaxy:
    """Class to handle keeping up with galaxy elements, including random
    initialization of a galaxy"""
    def __init__(self, position, name='Milky Way 10'):
        """Initialize a galaxy"""
        self.width = 30
        self.height = 30
        self.position = position
        self.name = name
        self.symbol = 'o'
        self.bodies = [station.Station(self.generate_position(),
            self.name + ' Station')]
        for index in range(random.randint(5, 10)):
            self.bodies.append(body.Body(self.generate_position(), str(index)))
        self.star = star.Star(self.get_random_location())

    def __repr__(self):
        """String representation of the galazy"""
        return 'galaxy ' + self.name + ' contains ' + self.star.__repr__()

    def generate_position(self):
        """Get a random position in the galaxy"""
        x = random.randint(-self.width/2, self.width/2)
        y = random.randint(-self.height/2, self.height/2)
        return x, y

    def get_random_location(self):
        """Get a random location tuple"""
        return (random.randint(0, self.width-1),
                random.randint(0, self.height-1))

    def get_current_view(self):
        """Returns a string representing the location of items in the
        galaxy"""
        horizontal_border = '|' + '-'*(self.width+2) + '|'
        current_view = horizontal_border + '\n'
        for row in range(self.height):
            current_view += '|'
            if self.star.get_location()[1] == row:
                current_view += ' '*(self.star.get_location()[0])
                current_view += '*'
                current_view += ' '*(self.width+1-self.star.get_location()[0])
            else:
                current_view += ' '*(self.width+2)
            current_view += '|\n'
        current_view += horizontal_border
        current_view += '\n' + str(self.star.get_location())
        return current_view

    def get_name(self):
        """Return the galaxy name"""
        return self.name

    def set_symbol(self, symbol):
        """Set the galaxy's map symbol"""
        self.symbol = symbol

    def get_station_position(self):
        """Get the station position, where the player is located after a
        launch"""
        return self.bodies[0].position
    
    def get_bodies_in_view(self, position, radius=10):
        """Get a list of bodies in view of the position"""
        bodies_in_view = []
        for b in self.bodies:
            if self.distance(position, b.position) <= radius:
                bodies_in_view.append(body.Body(
                    self.relative_position(position, b.position),
                    b.name, b.symbol))
        bodies_in_view.append(body.Body((0, 0), 'Player', '^'))
        return bodies_in_view

    def distance(self, user, body):
        """Get the distance between the user and body"""
        relative_position = self.relative_position(user, body)
        return math.sqrt(relative_position[0]**2 + relative_position[1]**2)

    def relative_position(self, user, body):
        """Calculate the position of the body relative to the user"""
        return body[0]-user[0], body[1]-user[1]
