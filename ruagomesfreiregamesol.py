import math
import pickle
import time
from Astar import Astar
from Astar import distance



def updateTickets(tickets, solutionSet, index, mode):

    for step in solutionSet[index]:
      if step[0] == [0] and mode == 1:
        tickets[0] -= 1
      elif step[0] == [0] and mode == 2:
        tickets[0] += 1
      elif step[0] == [1] and mode == 1:
        tickets[1] -= 1
      elif step[0] == [1] and mode == 2:
        tickets[1] += 1
      elif step[0] == [2] and mode == 1:
        tickets[2] -= 1
      elif step[0] == [2] and mode == 2:
        tickets[2] += 1
    return tickets

def getOffset(solutionSet, missingLen, nextLongestPath):
  offset = []
  for step in solutionSet:
    if len(step) >= nextLongestPath+missingLen :
      offset.append(step[nextLongestPath-1:-1][0])

  return offset


def formatOutput(solutionSet):
  outputSolution = []

  for i in range(len(solutionSet[0])):
    outputSolution.append([])
    for k in range(2):
      outputSolution[i].append([])
  
  
  for i in range(len(solutionSet[0])):
    for j in range(len(solutionSet)):
      outputSolution[i][0] += solutionSet[j][i][0]
      outputSolution[i][1] += solutionSet[j][i][1]
  return outputSolution




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
  

    size = len(init)
    
    longestPath = 0

    solutionSet = []

    for i in range(size):
      solution = Astar(self.model, self.auxheur, init[i], self.goal[i], limitexp, limitdepth, tickets, solutionSet,False,0)
      if len(solution) > longestPath:
        longestPath = len(solution)
      solutionSet.append(solution)
      tickets = updateTickets(tickets, solutionSet, i, 1)


    nextLongestPath = 0

    incompletePath = None


    for l in range(size):
      alreadyDone = []
      for i in range(size):
        if len(solutionSet[i]) < longestPath and len(solutionSet[i]) > nextLongestPath:
          nextLongestPath = len(solutionSet[i])
          incompletePath = solutionSet[i]
          offsetIndex = i
      for j in solutionSet:
        if len(j) == longestPath:
          alreadyDone.append(j)
      if incompletePath:
        tickets =  updateTickets(tickets, solutionSet, offsetIndex,2)
        solutionSet.pop(offsetIndex)
        offsetPath = Astar(self.model, self.auxheur, init[offsetIndex], self.goal[offsetIndex], limitexp, limitdepth, tickets,alreadyDone ,True, longestPath)

        for k in range(size): 
          if [init[k]] == offsetPath[0][1]:  #para ter o id do start
            index = k
            break
        
        solutionSet = solutionSet[0:index] + [offsetPath] + solutionSet[index:]
        tickets = updateTickets(tickets, solutionSet, index, 1)

      nextLongestPath = 0
      incompletePath = None
      offsetPath = []
    outputSolution = formatOutput(solutionSet)

    return outputSolution

