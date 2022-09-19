from matplotlib.patches import Polygon
from matplotlib import pyplot as plt
from collections import deque
import numpy as np
import operator
import re

class DOLSystem:
    def __init__(self, axiom, rules):
        # http://algorithmicbotany.org/papers/abop/abop.pdf
        self.axiom = axiom
        self.rules = rules
        
        self.x, self.y = 0, 0
        self.angle     = 0 
        
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
        angle   = np.radians(self.angle)
        self.x += distance * np.cos(angle)
        self.y += distance * np.sin(angle)
    
    def left(self, angle):
        self.angle += angle
    
    def right(self, angle):
        self.angle -= angle
    
    def draw(self, angle=90, distance=5, color='w', facecolor='k', linestyle='-', linewidth=1, fname=None):
        commands  = {
            'F': ('forward' , distance),
            '-': ('right'   , angle   ),
            '+': ('left'    , angle   )
            }
        
        xs, ys    = deque([ self.x ]), deque([ self.y ])        
        for c in self.axiom:
            func, args = commands.get(c)
            getattr(self, func)(args)
            if func == 'forward':
                xs.append(self.x)
                ys.append(self.y)                
        xs.appendleft(self.x)
        ys.appendleft(self.y)
        
        fig, ax   = plt.subplots(facecolor=facecolor, clear=True)
        ax.set_aspect('equal', 'box')
        ax.set_axis_off()
        ax.plot(xs, ys, color=color, linestyle='-', linewidth=1)
        
        fig.tight_layout()
        if fname is None: plt.show()
        else            : plt.savefig(fname)
        
    @staticmethod
    def evolve(axiom, rules):
        evolved = ''.join(rules.get(c, c) for c in axiom)
        return DOLSystem(evolved, rules)

