from utils import DOLSystem

DOLSystem(axiom='F-F-F-F', rules={ 'F':'FF-F-F-F-F-F+F' })(n=4).draw(fname='images/a.png')
DOLSystem(axiom='F-F-F-F', rules={ 'F':'FF-F-F-F-FF'    })(n=4).draw(fname='images/b.png')
DOLSystem(axiom='F-F-F-F', rules={ 'F':'FF-F+F-F-FF'    })(n=3).draw(fname='images/c.png')
DOLSystem(axiom='F-F-F-F', rules={ 'F':'FF-F--F-F'      })(n=4).draw(fname='images/d.png')
DOLSystem(axiom='F-F-F-F', rules={ 'F':'F-FF--F-F'      })(n=5).draw(fname='images/e.png')
DOLSystem(axiom='F-F-F-F', rules={ 'F':'F-F+F-F-F'      })(n=4).draw(fname='images/f.png')