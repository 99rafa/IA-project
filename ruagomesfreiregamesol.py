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
    
    self.goal = goal
    self.model = model
    self.auxheur = auxheur  

  def fixOffset(self,size,init, solutionSet, longestPath, limitexp, limitdepth, tickets) :

    incompletePath = None

    fixedOffset = True

    for i in range(len(solutionSet)):
      if len(solutionSet[i]) != longestPath:
        fixedOffset = False
        break


    while not fixedOffset and size > 1:
      alreadyDone = []

      for i in range(len(solutionSet)):
        if len(solutionSet[i]) < longestPath :
          incompletePath = solutionSet[i]
          offsetIndex = i

      for j in solutionSet:
        if len(j) == longestPath:
          alreadyDone.append(j)

      if incompletePath:
        tickets =  updateTickets(tickets, solutionSet, offsetIndex,2)
        offsetPath = Astar(self.model, self.auxheur, init[offsetIndex], self.goal[offsetIndex], limitexp, limitdepth, tickets,alreadyDone ,True, longestPath)


        if offsetPath == []:  #quer dizer que nao existe um path naquele numero de steps
          longestPath += 1
          continue
        solutionSet.pop(offsetIndex)

        for k in range(size): 
          if [init[k]] == offsetPath[0][1]:  #para ter o id do start
            index = k
            break
        
        solutionSet = solutionSet[0:index] + [offsetPath] + solutionSet[index:]
        tickets = updateTickets(tickets, solutionSet, index, 1)
        fixedOffset = True

        for path in solutionSet:
          if len(path) != longestPath:
            fixedOffset = False
            break        

      incompletePath = None
      offsetPath = []
    return solutionSet


  def arrangePursuitOder(self,init):

    shortestPath = math.inf

    for i in range(len(init)):
        for j in range(len(self.goal)):
          currentDist = distance(self.auxheur[init[i]-1][0], self.auxheur[self.goal[j]-1][0], self.auxheur[init[i]-1][1], self.auxheur[self.goal[j]-1][1])
          if currentDist < shortestPath:
            shortestPath = currentDist
            shortestThief = j
        auxGoal = self.goal[shortestThief]
        self.goal[shortestThief] = self.goal[i]
        self.goal[i] = auxGoal
        shortestPath = math.inf
       

  
  

  def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf], anyorder=False):
  

    size = len(init)
    
    longestPath = 0

    solutionSet = []

    if anyorder:
      self.arrangePursuitOder(init)          


    for i in range(size):
      solution = Astar(self.model, self.auxheur, init[i], self.goal[i], limitexp, limitdepth, tickets, solutionSet,False,0)
      if len(solution) > longestPath:
        longestPath = len(solution)
      solutionSet.append(solution)
      tickets = updateTickets(tickets, solutionSet, i, 1)
      print(solution)


    solutionSet = self.fixOffset(size, init,solutionSet,longestPath,limitexp, limitdepth, tickets)

    outputSolution = formatOutput(solutionSet)

    return outputSolution

