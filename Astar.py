import math

class Junction:

    def __init__(self,id,d,p = None, totalTransport = [0,0,0]):

        self.id = id
        self.parent = p
        self.d = d
        self.transport = [] 
        self.totalTransport = totalTransport #transporte até aquele ponto
        self.tickets = 0 #bilhetes ate este ponto
        self.sum = self.d + self.tickets #caminho ate ao ponto mais distancia ate goal


    def __eq__(self,other):
        if self.parent and other.parent:
            return self.id == other.id and self.parent.id == other.parent.id and self.transport == other.transport
        else:
             return self.id == other.id and self.transport == other.transport


def distance(x1,x2,y1,y2):
    return math.sqrt((x1-x2)**2 + (y1 - y2)**2)

def checkempty(size,list):
    for i in range(size):
        if list[i] != []:
            return False
    return True

def cleanExpList(exp_list, limit):
    for j,junc in enumerate(exp_list):
        if junc.tickets > limit:
            exp_list.pop(j)
    return exp_list


def getNewLim(ger_list):
    newLim = ger_list[0].tickets
    for i in ger_list:
        if i.tickets < newLim:
            newLim = i.tickets
    return newLim

        

def Astar(map,coords,start,goal,lim_exp,lim_depth, maxTickets, alreadyOccupied, correction, correctLen):

    #initialize
    pathsDone = len(alreadyOccupied)
    maxTaxiTickets = maxTickets[0]
    maxBusTickets = maxTickets[1]
    maxMetroTickets = maxTickets[2]



    dist = distance(coords[start-1 ][0],coords[goal-1][0],coords[start -1][1],coords[goal -1 ][1])


    start_junc = Junction(start,dist)


    end_junc = Junction(goal,0, math.inf)


    exp_list = []
    ger_list = []


    ger_list.append(start_junc)
    lim = start_junc.tickets
    while len(ger_list) > 0:

        #Atualiza o node a ser expandido para cada agente
        current_index = -1
        positionsOccupied = []
        if pathsDone > 0:
            for i in range(pathsDone):
                if lim + 1 < len(alreadyOccupied[i]) :
                    positionsOccupied.append(alreadyOccupied[i][lim+1][1][0])  # o [0] e apenas para me dar so o valor dentro da lista e nao os brackets
                  
        for j, node in enumerate(ger_list):
            if node.tickets == lim and node.id:
                current_junc = ger_list[0]
                current_index = j
                break
        for j, node in enumerate(ger_list):
            if node.d < current_junc.d and node.tickets == lim :
                current_junc = node
                current_index = j
        if current_index == -1:
            lim = getNewLim(ger_list)
            continue

        ger_list.pop(current_index)
        
        exp_list.append( current_junc)

        

        #Verifica se esta no goal
        
        if  current_junc.id == end_junc.id:
            if not correction or (correction and lim == correctLen -1 ): # -1 porque o lim começa em 0
                res = []
                current =  current_junc
                while current is not None:
                    res.append([current.transport,[current.id]])
                    current = current.parent
                return res[::-1] # Return reversed path
                

        adjacentJuncs =[]

        

        if correction and current_junc.tickets == correctLen:
            continue


        for newJunc in map[ current_junc.id ]:
            

            newJuncID = newJunc[1]
            newJuncTransport = newJunc[0]


            if newJuncID in positionsOccupied:
               continue

            
            if current_junc.parent and current_junc.parent.id == newJunc[1] and not correction: 
                continue

    
            if newJuncTransport == 0 and current_junc.totalTransport[0] >= maxTaxiTickets:
                continue
            elif newJuncTransport == 1 and current_junc.totalTransport[1] >= maxBusTickets:
                continue 
            elif  newJuncTransport == 2 and current_junc.totalTransport[2] >= maxMetroTickets:
                continue

            
            
            
            childTotalTransport = []
            childTotalTransport.append(current_junc.totalTransport[0])
            childTotalTransport.append(current_junc.totalTransport[1])
            childTotalTransport.append(current_junc.totalTransport[2])
            
            
            newJuncDist = distance(coords[newJuncID -1][0],coords[goal -1 ][0], coords[newJuncID -1 ][1], coords[goal -1 ][1])
            childJunc = Junction(newJuncID, newJuncDist, current_junc, childTotalTransport)

           
            
            childJunc.transport = [newJuncTransport]
            childTaxiTickets = childTotalTransport[0] +1
            childBusTickets = childTotalTransport[1] +1
            childMetroTickets = childTotalTransport[2] +1
            
            

            if newJuncTransport == 0:
                childJunc.totalTransport[0] = childTaxiTickets  
            elif newJuncTransport == 1:
                childJunc.totalTransport[1] = childBusTickets 
            elif newJuncTransport == 2:
                childJunc.totalTransport[2] = childMetroTickets

            
            adjacentJuncs.append(childJunc)
            

  
        for adjac in adjacentJuncs:
            

            if adjac in exp_list and not correction:
                continue
                
                
            
            adjac.tickets =  current_junc.tickets + 1
            adjac.sum = adjac.d + adjac.tickets


            # Add the child to the open list
            #tem que ser uma lista de um elemento por causa do formato do result
            ger_list.append(adjac)
        if len(ger_list) > 0:
            lim = getNewLim(ger_list)


    return []
       
        
            

        
