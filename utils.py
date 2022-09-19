from matplotlib.patches import Polygon
from matplotlib import pyplot as plt

import numpy as np
import operator
import re

class DOLSystem:
    def __init__(self, axiom, rules):
        # http://algorithmicbotany.org/papers/abop/abop.pdf
        self.axiom = axiom
        self.rules = rules
        
        self.x     = 0
        self.y     = 0
        self.angle = 0 
        
    def __repr__(self):
        # https://stackoverflow.com/a/24055500
        axiom = re.sub(r'^(.{32}).*$', '\g<1>...', self.axiom)
        return f'[AXIOM] {axiom}\n[RULES] {self.rules}'
    
    def __call__(self, n=0):
        evolved = self
        for _ in range(n):
            evolved = DOLSystem.evolve(evolved.axiom, self.rules)
        return evolved
    
    def forward(self, distance):
        angle  = np.radians(self.angle)
        self.x = self.x + distance * np.cos(angle)
        self.y = self.y + distance * np.sin(angle)
        return self.x, self.y
    
    def left(self, angle):
        self.angle += angle
        return self.x, self.y
    
    def right(self, angle):
        self.angle -= angle
        return self.x, self.y
    
    def draw(self, angle=90, distance=5, edgecolor='w', facecolor='k', linestyle='-', linewidth=1, fname=None):
        commands  = {
            'F': ('forward' , distance),
            '-': ('right'   , angle   ),
            '+': ('left'    , angle   )
            }
        
        fig, ax = plt.subplots(facecolor=facecolor, clear=True)
        polygon = Polygon([ operator.methodcaller(*commands.get(c))(self) for c in self.axiom ], closed=True, fill=None, edgecolor=edgecolor, linestyle=linestyle, linewidth=linewidth)
        
        ax.scatter(self.x, self.y, c=facecolor) # polygon won't be shown otherwise ???
        
        ax.set_aspect('equal', 'box')
        ax.add_patch(polygon)
        ax.set_axis_off()
        
        fig.tight_layout()
        if fname is None: plt.show()
        else            : plt.savefig(fname)
        
    @staticmethod
    def evolve(axiom, rules):
        evolved = ''.join(rules.get(c, c) for c in axiom)
        return DOLSystem(evolved, rules)