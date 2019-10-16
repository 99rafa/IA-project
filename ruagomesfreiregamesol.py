import math
import pickle
import time

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

  

  def search(self, init, limitexp = 2000, limitdepth = 20, tickets = [math.inf,math.inf,math.inf]):
    ##
    ## to implement
    ##


    return [[[],[30]],[[0],[56]]]

    
