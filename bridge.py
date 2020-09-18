from simpleai.search import astar,SearchProblem
# class State(SearchProblem):

#     GOAL = [1,3,6,8,12]

#     def __init__(self,a : int,b : int,limit : int,finishSide : list,initSide : list):
#         self.a          = a
#         self.b          = b
#         self.limit      = limit
#         self.finishSide = finishSide
#         self.initSide   = initSide

#     def is_goal(self):
#         return self.finishSide == State.GOAL and self.limit >= 0

    

#     def copy(self) -> State:
#         return State(self.a,self.b,self.limit,self.finishSide,self.initSide)

#     def saveState(self) -> dict:
#         return {
#             "a"             : self.a,
#             "b"             : self.b,
#             "limit"         : self.limit,
#             "finishSide"    : self.finishSide,
#             "initSide"      : self.initSide,
#         }

#     @classmethod
#     def fromDict(cls,dic : dict) -> State:
#         return cls(dic["a"],dic["b"],dic["limit"],dic["finishSide"],dic["initSide"])

class Party:
    def __init__(self,bSide : list,aSide : list,cost : int,direction : bool):
        self.bSide     = bSide
        self.aSide     = aSide
        self.cost      = cost
        self.direction = direction

    def attr(self):
        return (self.bSide,self.aSide,self.cost,self.direction)

    def modify(self,addition):
        nCost = max(addition)
        if(addition[0] == addition[1]): # Just one traveler
            newASide = [0]
            newBSide = [0]
            if self.direction: # A -> B
                newBSide = self.bSide.copy()
                newBSide.append(addition[0])
                newASide = list(filter(lambda x: x != addition[0],self.aSide))
            else: # B -> A
                newBSide = list(filter(lambda x: x != addition[0],self.bSide))
                newASide = self.aSide.copy()
                newASide.append(addition[0])
            return Party(newBSide,newASide,self.cost - nCost,not self.direction)
        else:
            newASide = [0]
            newBSide = [0]
            if self.direction: # A -> B
                newBSide = self.bSide.copy()
                newBSide.extend(addition)
                newASide = list(filter(lambda x: x not in addition,self.aSide))
            else: # B -> A
                newBSide = list(filter(lambda x: x not in addition,self.bSide))
                newASide = self.aSide.copy()
                newASide.extend(addition)
            return Party(newBSide,newASide,self.cost - nCost,not self.direction)
        

GOAL = [1,3,6,8,12]

class TorchProblem(SearchProblem):

    def actions(self, state : Party):
        if(state.cost<1):
            return []
        else:
            if(state.direction): # A to B
                return [(x,y) for x in state.aSide for y in state.aSide]
            else: # B to A
                return [(x,y) for x in state.bSide for y in state.bSide]

    def result(self, state : Party, action : tuple):
        return state.modify(action)

    def is_goal(self, state : Party):
        temp = sorted(state.bSide)
        return temp == GOAL and state.cost>=0

    def heuristic(self, state : Party):
        return len(GOAL) - len(state.bSide)

problem = TorchProblem(initial_state=Party([],GOAL.copy(),30,True))
result = astar(problem)

for x in result.path():
    print((x[0],x[1].attr()))
