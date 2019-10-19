import math
import pickle
import time
from Astar import Astar


class Agent:
  def __init__(self,initpos,tickets):
    self.initpos = initpos
    self.tickets = tickets

class SearchProblem:

  def __init__(self, goal, model, auxheur = []):
    ##
    ## to implement
    ## 
    self.goal = goal
    self.model = model
    self.auxheur = auxheur  


  

  def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
    ##
    ## to implement
    ##

    size = len(init)

    for i in range(size):
      solution = Astar(self.model, self.auxheur, init[i], self.goal[i], limitexp, limitdepth)


    return solution

    
