# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    from collections import defaultdict
    from util import Stack
    initial_node=problem.getStartState()
    
    current_node=defaultdict(list)
    current_node[initial_node].append("No parent")
    current_node[initial_node].append("No direction")
    stack=Stack()
    stack.push(current_node)
    current_node=stack.pop()
    direction_list={}
    Child=current_node.keys()
    Parent=current_node.values()[0]
    visited_list={}
    while (problem.isGoalState(Child[0]) is not True):
            
        if(Child[0] in visited_list.keys()):
            
            current_node=stack.pop()
            Child=current_node.keys()
            Parent=current_node.values()[0]
            
        else:
            visited_list[Child[0]]=Parent[0]
            direction_list[Child[0]]=Parent[1]
            Successor_node=problem.getSuccessors(Child[0])
            for index in range(len(Successor_node)):
                temp_dict=defaultdict(list)
                temp_dict[Successor_node[index][0]].append(Child[0])
                temp_dict[Successor_node[index][0]].append(Successor_node[index][1])
                #print"The temp dict values are",temp_dict
                
                stack.push(temp_dict)
                
            #print " The heap of queue is",priority_queue.heap
            current_node=stack.pop()
            #print "The current node is",current_node
            Child=current_node.keys()
            Parent=current_node.values()[0]
    
    visited_list[Child[0]]= Parent[0]
    direction_list[Child[0]]=Parent[1]
    backtracking =[]
    path = Child[0]
    backtracking.append(direction_list[path])
    path = visited_list[path]
    print "The path is",path
    while (path!= problem.getStartState()):
        backtracking.append(direction_list[path])
        path = visited_list[path]
    backtracking.reverse()

    return backtracking
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    from collections import defaultdict
    from util import Queue
    initial_node=problem.getStartState()
    
    current_node=defaultdict(list)
    current_node[initial_node].append("No parent")
    current_node[initial_node].append("No direction")
    queue=Queue()
    queue.push(current_node)
    current_node=queue.pop()
    direction_list={}
    Child=current_node.keys()
    Parent=current_node.values()[0]
    visited_list={}
    while (problem.isGoalState(Child[0]) is not True):
            
        if(Child[0] in visited_list.keys()):
            
            current_node=queue.pop()
            Child=current_node.keys()
            Parent=current_node.values()[0]
            
        else:
            visited_list[Child[0]]=Parent[0]
            direction_list[Child[0]]=Parent[1]
            Successor_node=problem.getSuccessors(Child[0])
            for index in range(len(Successor_node)):
                temp_dict=defaultdict(list)
                temp_dict[Successor_node[index][0]].append(Child[0])
                temp_dict[Successor_node[index][0]].append(Successor_node[index][1])
                queue.push(temp_dict)

            current_node=queue.pop()
            Child=current_node.keys()
            Parent=current_node.values()[0]
    
    visited_list[Child[0]]= Parent[0]
    direction_list[Child[0]]=Parent[1]
    backtracking =[]
    path = Child[0]
    backtracking.append(direction_list[path])
    path = visited_list[path]
    print "The path is",path
    while (path!= problem.getStartState()):
        backtracking.append(direction_list[path])
        path = visited_list[path]
    backtracking.reverse()

    return backtracking
    


    util.raiseNotDefined()

def uniformCostSearch(problem):
    from collections import defaultdict
    from util import PriorityQueue
    initial_node=problem.getStartState()
    
    current_node=defaultdict(list)
    current_node[initial_node].append("No parent")
    current_node[initial_node].append("No direction")
    priority_queue=PriorityQueue()
    priority_queue.push(current_node,0)
    cost_list={}
    cost_list[initial_node]=0
    current_node=priority_queue.pop()
    direction_list={}
    Child=current_node.keys()
    Parent=current_node.values()[0]
    visited_list={}
    while (problem.isGoalState(Child[0]) is not True):
            
        if(Child[0] in visited_list.keys()):
            
            current_node=priority_queue.pop()
            Child=current_node.keys()
            Parent=current_node.values()[0]
                                   
        else:
            visited_list[Child[0]]=Parent[0]
            direction_list[Child[0]]=Parent[1]
            Successor_node=problem.getSuccessors(Child[0])
            for index in range(len(Successor_node)):
                temp_dict=defaultdict(list)
                temp_dict[Successor_node[index][0]].append(Child[0])
                temp_dict[Successor_node[index][0]].append(Successor_node[index][1])
                cost_list[Successor_node[index][0]]= cost_list[Child[0]]+Successor_node[index][2]
                priority_queue.push(temp_dict, cost_list[Successor_node[index][0]])
            current_node=priority_queue.pop()
            Child=current_node.keys()
            Parent=current_node.values()[0]
    
    visited_list[Child[0]]= Parent[0]
    direction_list[Child[0]]=Parent[1]
    backtracking =[]
    path = Child[0]
    backtracking.append(direction_list[path])
    path = visited_list[path]
    print "The path is",path
    while (path!= problem.getStartState()):
        backtracking.append(direction_list[path])
        path = visited_list[path]
    backtracking.reverse()
    return backtracking  
    util.raiseNotDefined()




def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  
    
    from collections import defaultdict
    from util import PriorityQueue
    
    initial_node=problem.getStartState()
    
    current_node=defaultdict(list)
    current_node[initial_node].append("No parent")
    current_node[initial_node].append("No direction")
    priority_queue=PriorityQueue()
    cost_array={}
    #priority_queue.push(current_node,0)
    cost_list={}
    cost_list[initial_node]=0
    cost_array[initial_node]=heuristic(initial_node,problem)
    
    direction_list={}
    Child=current_node.keys()
    Parent=current_node.values()[0]
    visited_list={}
          
    
    while (problem.isGoalState(Child[0]) is not True):
            
        if(Child[0] in visited_list.keys()):
            current_node=priority_queue.pop()
            Child=current_node.keys()
            Parent=current_node.values()[0]
        else:
            visited_list[Child[0]]=Parent[0]
            direction_list[Child[0]]=Parent[1]
            Successor_node=problem.getSuccessors(Child[0])
            for index in range(len(Successor_node)):
                temp_dict=defaultdict(list)
                
                temp_dict[Successor_node[index][0]].append(Child[0])
                temp_dict[Successor_node[index][0]].append(Successor_node[index][1])
                cost_list[Successor_node[index][0]]= cost_list[Child[0]]+Successor_node[index][2] 
                cost_array[Successor_node[index][0]]=cost_list[Successor_node[index][0]]+heuristic(Successor_node[index][0],problem)
                priority_queue.push(temp_dict, cost_array[Successor_node[index][0]])
                  
            current_node=priority_queue.pop()
            Child=current_node.keys()
            Parent=current_node.values()[0]
    
    visited_list[Child[0]]= Parent[0]
    direction_list[Child[0]]=Parent[1]
    backtracking =[]
    path = Child[0]
    backtracking.append(direction_list[path])
    path = visited_list[path]
    while (path!= problem.getStartState()):
        backtracking.append(direction_list[path])
        path = visited_list[path]
    backtracking.reverse()
    return backtracking
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
