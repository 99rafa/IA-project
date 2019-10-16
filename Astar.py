import math

class Junction:
    
    def __init__(sefl,id,d,transitions,p,n):

        self.id = id
        self.parent = []    
        self.d = d
        self.transitions = transitions
        self.transport = []
        self.p = []
        self.f1 = [] #bilhetes usados ate este ponto
        self.f2 = [] #caminho ate ao ponto mais distancia ate goal

        for i in range(n):
            self.parent.append(None)
            self.p.append(p[i])
            self.f1.append(0)
            self.f2.append(0)

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
    start_junc = []
    end_junc = []
    dist = []
    oridist = []
    for i in  range(len(start)):
        dist.append([])
        oridist.append
        for j in range(len(goal)):
            dist[i].append(distance(coords[start[i] + 1][0],coords[start[i][1],coords[goal[j] + 1][0],coords[goal[j] + 1][1]]))


    for i in range(len(start)):
        start_junc.append(Junction(start[i],dist[i],coords[start[i] + 1][1]),map[start[i]],0))

    
    for i in goal:
        end_junc.append(Junction(goal[i],0,map[goal],0))


    exp_list = []
    ger_list = []
    for i in range(len(start)):


    for i in range(len(start)):
        ger_list.append([start_junc[i]])
        exp_list.append([])

    
    size = len(ger_list)
    while not checkempty(size,ger_list):
    


        #Atualiza o node a ser expandido para cada agente
        current_nodes = []
        current_indexs = []
        for i in range(size):
            current_nodes.append(ger_list[i][0])
            current_indexs.append(0)
            for j, node in enumerate(ger_list[i]):
                if node.f1[i] < current_nodes[i].f1[i]
                    current_nodes[i] = node
                    current_indexs[i] = j

            ger_list[i].pop(current_indexs[i])
            exp_list[i].append(current_nodes[i])

        #Verifica se tao todos no goal
        check = 0
        for i in range(size):
            if( current_nodes[i] == end_junc[i])
                check += 1
            
        if (check == size):
            #perfect
            

            res = []    
            for i in range(current_nodes[0]):
                res.append([])

            for i in range(size):
                current = current_nodes[i]
                j = 0
                while current is not None:
                    res[j].append(current.id[i])
                    current = current.parent[i]
                    j+=1
            
            return res[::-1] # Return reversed path


            pass
            
        



        



    
    


    

