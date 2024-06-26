import pygame 
from Noob import Environment,Agent
import design as d
import colorgentool as genn
import colors as cc
import random as r

# Initialize Pygame
pygame.init()

# Set up the screen
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Simple Game")


pygame.init()

i = pygame.display.Info()
# width,height = 1280,720
# pygame.mouse.set_visible(False)
# screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
def testing(screen):
    color1 = cc.colorlist[12]
    
    newcolor = genn.diffuser(color1,color1)
    
    
    bg = cc.colorlist[0]
    movr = False
    keyy = None
    clock = pygame.time.Clock()
    keys_pressed = set()
    fps = 60
    ti =  0
    
    bgg = d.Background(screen,12,1)
    tra = d.Trailsquare(5)
    
    
    # Initialize the environment and agent
    env = Environment(screen)
    agent = Agent(state_size=14, action_size=4)
    agent.load('agent_model.weights.h5') #load the trained model
    
    running = True
    episode = 0
    clock = pygame.time.Clock()
    
    while running:
        clock.tick(fps)

        tra.update(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return
    
        # Get current state
        state = env.get_state()
    
        # Choose action
        action = agent.act(state)
    
        # Take action in the environment and get next state, reward, and done flag
        next_state, reward, done = env.step(screen,action)
    
        # Remember the experience
        agent.remember(state, action, reward, next_state, done)
    
        # Render the environment
        env.render(screen)
    
        # Update display
        pygame.display.update()
        
        bgg.draw(screen)
        # Check if the episode is finished
        if done:
            env.reset()
        tra.draw(screen)
    
        


