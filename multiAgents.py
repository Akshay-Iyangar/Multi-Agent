# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions, AgentState
import random, util
from game import Grid
from game import Directions
from game import Actions
from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()
        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        #print "Successor game state",successorGameState.
        newPos = successorGameState.getPacmanPosition()
        #print "Pacman position",newPos
        newFood = successorGameState.getFood()
        ghost_pos = successorGameState.getGhostPositions()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        food_cord=newFood.asList()
        #print sorted(food_cord)
        food_count = len(food_cord)
        dictionary={}
        distance = [0]*food_count
        distance_between_pacman_ghost=manhattanDistance(ghost_pos[0], newPos)
        #print food_count
        if(distance_between_pacman_ghost>1):
            for i in range(food_count):
                for j in range(2):
                    distance[i]=(distance[i]+abs((food_cord[i][j] - newPos[j])) )   
                dictionary[food_cord[i]]=distance[i]  
            if(bool(dictionary)==True):  
                nearest_food_state=min(dictionary, key=dictionary.get)
                nearest_food_distance1 = sum(distance)
                nearest_food_distance=dictionary[nearest_food_state]
               
                #print (len(food_cord) + nearest_food_distance)
                #print dictionary
                Evaluation_function = (-1000*(len(food_cord))-nearest_food_distance)
                #print Evaluation_function
                return Evaluation_function
            else:
                return 0
        else:
            return -10000000000

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

    def getAction(self, gameState):   
        def maximum(state,depth):
            final_value= -100000000.00
            legalmoves = state.getLegalActions(0)
            depth = depth + 1
            if(depth == self.depth or state.isWin() or state.isLose()):
                return self.evaluationFunction(state)
            else:
                for action in legalmoves:
                    final_value = max(final_value,minimum(state.generateSuccessor(self.index,action),depth,1))
            return final_value
        
        def minimum(state,depth,ghost_num):
            final_value=100000000.00
            legalMoves = state.getLegalActions(ghost_num)
            if (state.isWin() or state.isLose()):
                return self.evaluationFunction(state)
            if(ghost_num == gameState.getNumAgents()-1):
                for action in legalMoves:
                    final_value=min(final_value,maximum(state.generateSuccessor(ghost_num,action),depth))
            else:
                for action in legalMoves:
                    final_value = min(final_value,minimum(state.generateSuccessor(ghost_num,action),depth,ghost_num+1))
            return final_value
        
        legalMoves = gameState.getLegalActions(0)
        dict_value_action={}
        for action in legalMoves:
            current_depth =0
            value = minimum(gameState.generateSuccessor(0,action),current_depth,1)
            dict_value_action[action]=value
            action=max(dict_value_action, key=dict_value_action.get)
        return action

    
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    def getAction(self, gameState):   
        def maximum(state,depth,alpha,beta):
            final_value= -100000000.00
            legalmoves = state.getLegalActions(0)
            depth = depth + 1
            if(depth == self.depth or state.isWin() or state.isLose()):
                return self.evaluationFunction(state)
            for action in legalmoves:
                final_value = max(final_value,minimum(state.generateSuccessor(self.index,action),depth,1,alpha,beta))
                alpha = max(alpha,final_value)
                if(final_value>beta):
                    return final_value
            return final_value
        def minimum(state,depth,ghost_num,alpha,beta):
            final_value=100000000.00
            legalMoves = state.getLegalActions(ghost_num)
            if (state.isWin() or state.isLose()):
                return self.evaluationFunction(state)
            if(ghost_num == gameState.getNumAgents()-1):
                for action in legalMoves:
                    final_value=min(final_value,maximum(state.generateSuccessor(ghost_num,action),depth,alpha,beta))
                    beta = min(beta,final_value)
                    if(final_value<alpha):
                        return final_value
                return final_value
            else:
                for action in legalMoves:
                    final_value = min(final_value,minimum(state.generateSuccessor(ghost_num,action),depth,ghost_num+1,alpha,beta))
                    beta = min(beta,final_value)
                    if(final_value<alpha):
                        return final_value
                return final_value
        legalMoves = gameState.getLegalActions(0)
        dict_value_action={}
        beta = 100000000.00
        alpha = -100000000.00
        for action in legalMoves:
            current_depth =0
            value = minimum(gameState.generateSuccessor(0,action),current_depth,1,alpha,beta)
            dict_value_action[action]=value
            action=max(dict_value_action, key=dict_value_action.get)
            alpha= max(alpha,value)
        return action
    

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    def getAction(self, gameState):   
        def maximum(state,depth):
            final_value= -100000000.00
            legalmoves = state.getLegalActions(0)
            depth = depth + 1
            if(depth == self.depth or state.isWin() or state.isLose()):
                return self.evaluationFunction(state)
            else:
                for action in legalmoves:
                    final_value = max(final_value,minimum(state.generateSuccessor(self.index,action),depth,1))
            return final_value
        
        def minimum(state,depth,ghost_num):
            final_value=100000000.00
            legalMoves = state.getLegalActions(ghost_num)
            final_value_chance=0.0
            if (state.isWin() or state.isLose()):
                return self.evaluationFunction(state)
            if(ghost_num == gameState.getNumAgents()-1):
                for action in legalMoves:
                    final_value_chance=final_value_chance + (maximum(state.generateSuccessor(ghost_num,action),depth)/ghost_num)
            else:
                for action in legalMoves:
                    final_value_chance = final_value_chance + (minimum(state.generateSuccessor(ghost_num,action),depth,ghost_num+1)/ghost_num)
            return final_value_chance
        
        legalMoves = gameState.getLegalActions(0)
        dict_value_action={}
        for action in legalMoves:
            current_depth =0
            value = minimum(gameState.generateSuccessor(0,action),current_depth,1)
            dict_value_action[action]=value
            action=max(dict_value_action, key=dict_value_action.get)
        return action

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).
      1.)food-count = Will Add the food count as initially the value is high it will keep decreasing so at the 
      beginning just need to have more rewarding states multiplued it with constant (0.8)
      2.)Ghost-distance- Finding the nearest ghost and then calculating Manhattan distance with it
      3.)Nearest-Food Pallet - Calculate the nearest food pallet from Pacman using Manhattan have taken exp(6) 
      because I am multiplying it with the ghost-distance to find the relativity between the nearest food and 
      the nearest Ghost so higher the value father the ghost and pacman is safe to eat the food.
      4.)Used the Capsule count just as a normalising factor (can discard not ext impt)
      5.)Used Scared timer when the ghost enter scared time and adding it to the final reward becasue pacman can't
      be hurt when ghost is scared. (It was worthy to note of adding this to reward actually helped my bound to push
      some scores above 1000)
      6.)The current Score of the game was finally added to change so that there could be a shift in it becasue of 
      all the above value considered
      DESCRIPTION: <write something here so we know what you did>
    """
    Pacman_position=currentGameState.getPacmanPosition()
    nextGameState =currentGameState.getLegalActions(0)
    Walls = currentGameState.getWalls()
    Wall_cord=Walls.asList()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    scaredtime=0
    for Ghost_scare_time in newScaredTimes:
        scaredtime = scaredtime + Ghost_scare_time
    Ghost_position=currentGameState.getGhostPositions()
    capsule = currentGameState.getCapsules()
    capsule_count = len(capsule)
    Ghost_count = len(Ghost_position)
    distance_ghost=[0]*Ghost_count
    dictionary_ghost={}
    food=currentGameState.getFood()
    food_cord = food.asList()
    food_count=len(food_cord) # factor 1
    dictionary_food={}
    distance = [0]*food_count
    visited_list=[]
    visited_list.append(Pacman_position)
    nearest_food_distance=0
    for i in range(food_count):
        for j in range(2):
            distance[i]=(distance[i]+abs((food_cord[i][j] - Pacman_position[j])) )   
        dictionary_food[food_cord[i]]=distance[i] 
    if(food_count > 0):       
        nearest_food_state=min(dictionary_food, key=dictionary_food.get)
        nearest_food_distance = dictionary_food[nearest_food_state]
        nearest_food_distance=(1.0/nearest_food_distance)**6
    for i in range(Ghost_count):
        for j in range(2):
            distance_ghost[i]=(distance_ghost[i]+abs((Ghost_position[i][j] - Pacman_position[j])) )   
        dictionary_ghost[Ghost_position[i]]=distance_ghost[i] 
    ghosty=min(dictionary_ghost, key=dictionary_ghost.get)
    ghosty_ka_distance=dictionary_ghost[ghosty]
    eval = currentGameState.getScore() + (nearest_food_distance*ghosty_ka_distance) + scaredtime +(0.8*food_count) -(capsule_count)
    return eval
# Abbreviation
better = betterEvaluationFunction

