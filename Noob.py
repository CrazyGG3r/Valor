import pygame
from entities import * 
import random as r 
import colors as cc
import colorgentool as genn
from classes import *
pygame.init()
import numpy as np
from collections import deque
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

import numpy as np
from collections import deque
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class Agent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)  # Replay memory buffer
        self.gamma = 0.95  # Discount factor
        self.epsilon = 1.0  # Exploration rate
        self.epsilon_min = 0.01  # Minimum exploration rate
        self.epsilon_decay = 0.995  # Exploration decay rate
        self.learning_rate = 0.001  # Learning rate
        self.model = self._build_model()
        self.filename = 'agentmodel.h5'
        print(self.model)

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        # if np.random.rand() <= self.epsilon:
        #     return np.random.choice(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])
    
    def replay(self, batch_size):
        if len(self.memory) < batch_size:
            return
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            next_state = np.reshape(next_state, (1, self.state_size))
            state = np.reshape(state, (1, self.state_size))
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def save(self,filename):
        self.model.save_weights(filename)

    def load(self, filename):
        self.model.load_weights(filename)


class Environment:
    def __init__(self,screen):
        self.valor = Bot([500,500],20,3,"Retardium",cc.colorlist[11])
        self.dushman = spawner(screen,self.valor) 
        for a in range(0,5):
            self.dushman.spawn(cc.colorlist[8])
        self.score = 0
        self.reward = 0
        self.scoredisplay = Text(((screen.get_width()//2)-70,10),50,cc.colorlist[12],"Score : 0 ",2)
        self.Episode = 0
        self.Episodedisplay = Text(((screen.get_width()//2)-400,10),50,cc.colorlist[12],f"Episode: {self.Episode}",2)
        self.texts = [self.scoredisplay,self.Episodedisplay]
        
    def reset(self,screen):
        self.Episode +=1 
        self.valor = Bot([500,500],20,3,"Retardium",cc.colorlist[11])
        self.dushman.reset_spawner()
        for a in range(0,5):
            self.dushman.spawn(cc.colorlist[5])
        self.score = 0
        self.scoredisplay.update_text("Score :".format(self.score))
   
    def is_collision(self,):
        for a in self.dushman.enemies:
            distance = ((self.valor.x - a.x) ** 2 + (self.valor.y - a.y) ** 2) ** 0.5
            if distance <= self.valor.radius + a.radius:
                return True
        return False
  
    def step(self,screen,action):#updating environment - implements actions -returns reward or gameover
        self.valor.move(action,screen)   
        for e in self.dushman.enemies:
            m = pygame.mouse.get_pos()
            e.move1(screen,self.valor.x,self.valor.y)
        if self.is_collision():
            self.reward -= 100
            self.reset(screen) #change ur reward here
            
        else:
            self.reward +=2 #good boy
            return self.get_state(),self.reward,False
        return self.get_state(),self.reward,False
    
    def get_state(self):
        state = []
        valorpos = (int(self.valor.x),int(self.valor.y))
        state.append(valorpos[0])
        state.append(valorpos[1])
        vectorr = int(self.valor.MovVector[0]),int(self.valor.MovVector[1])
        state.append(vectorr[0])
        state.append(vectorr[1])
        
        each_enemy = []
        for a in self.dushman.enemies:
            dx = self.valor.x - a.x
            dy = self.valor.y - a.y
            
            # Calculate the angle from enemy to player
            angle = np.arctan2(dy, dx)
            
            # Convert angle from radians to degrees and append to state
            angle_degrees = np.degrees(angle)
            state.append(int(angle_degrees))
        dist_from_each_Enemy = []
        for a in self.dushman.enemies:
            b = int(sqrt(((a.y - self.valor.y)*(a.y - self.valor.y)) + ((a.x-self.valor.x)*(a.x-self.valor.x))))
            state.append(b)
        state = np.reshape(state, (1, len(state)))
        print(state)
        return state
    
    def render(self,screen): 
        for a in self.dushman.enemies:
            a.draw(screen)
        self.valor.draw(screen)
        self.scoredisplay.update_text("Score: {}".format(self.score))
        self.Episodedisplay.update_text("Episode: {}".format(self.Episode))
        for a in self.texts:
            a.draw(screen)
        pass