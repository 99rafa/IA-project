import math

class Junction:

    def __init__(self,id,d,p = None):

        self.id = id
        self.parent = p
        self.d = d
        self.transport = []
        self.tickets = 0 #bilhetes usados ate este ponto
        self.sum = 0 #caminho ate ao ponto mais distancia ate goal


    def __eq__(self,other):
        return self.id == other.id

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1 - y2)**2)

def checkempty(size,list):
    for i in range(size):
        if list[i] != []:
            return False
    return True

def Astar(map,coords,start,goal,lim_exp,lim_depth):

    #initialize

    dist = distance(coords[start-1 ][0],coords[start-1][1],coords[goal -1][0],coords[goal -1 ][1])


    start_junc = Junction(start,dist)


    end_junc = Junction(goal,0)


    exp_list = []
    ger_list = []


    ger_list.append(start_junc)


    while len(ger_list) > 0:

       
        #Atualiza o node a ser expandido para cada agente
        current_node = ger_list[0]
        current_index = 0
        for j, node in enumerate(ger_list):

            if node.sum < current_node.sum :

                current_node = node
                current_index = j

        ger_list.pop(current_index)
        exp_list.append(current_node)

  
        #Verifica se esta no goal
        
        if current_node == end_junc:
            #perfect


            res = []
            current = current_node
            while current is not None:
                res.append([current.transport,[current.id]])
                current = current.parent

            print(res)
            return res[::-1] # Return reversed path

        adjacentJuncs =[]


        for newJunc in map[current_node.id ]:
            
            
            newJuncID = newJunc[1]
            newJuncDist = distance(coords[newJuncID -1][0],coords[newJuncID -1 ][1], coords[goal -1 ][0],coords[goal -1 ][1])
            childJunc = Junction(newJuncID, newJuncDist,current_node)

            newJuncTransport = newJunc[0]
            adjacentJuncs.append([newJuncTransport,childJunc])
       
       #adjac[0] -> meio de transporte para essa junction
       #adjac[1] -> estrutura da junction
  
        for adjac in adjacentJuncs:

            for exp_junc in exp_list:
                if adjac[1] == exp_junc:
                    continue

            adjac[1].tickets = current_node.tickets + 1
            adjac[1].sum = adjac[1].d + adjac[1].tickets

            # Child is already in the open list

            for junc in ger_list:
                if junc == adjac[1] and adjac[1].tickets > junc.tickets:
                    continue

            # Add the child to the open list
            adjac[1].transport = [adjac[0]]  #tem que ser uma lista de um elemento por causa do formato do result
            ger_list.append(adjac[1])

          

