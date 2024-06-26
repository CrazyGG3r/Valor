import pygame 
from Noob import Environment,Agent
import design as d
import colorgentool as genn
import colors as cc
import random as r

pygame.init()

# Set up the screen
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Simple Game")


# pygame.init()

# i = pygame.display.Info()
# width,height = 1280,720
# pygame.mouse.set_visible(False)
# screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
def train(screen):
    color1 = cc.colorlist[12]
    color2 = cc.colorlist[10]
    newcolor = genn.diffuser(color1,color1)
    col = r.choice(newcolor)
    
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
    
    # parameters
    batch_size = 16
    replay_interval = 10  # Replay every 10 steps
    save_interval = 1000  # Save model weights every 1000 episodes
    
    running = True
    episode = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                running = False
        tra.update(pygame.mouse.get_pos())
        
        state = env.get_state() #state = (pos retardium, vector retardium, 
                                #         angle from bob,angle from bob,angle from bob,angle from bob,angle from bob,
                                #         dist  from bob,dist  from bob,dist  from bob dist  from bob,dist  from bob)
    
      
        action = agent.act(state) #0- left,1-right,2-up,3-down
    
        # Take action in the environment and get next state, reward, and done flag
        next_state, reward, done = env.step(screen,action)
    
        # Remember the experience
        agent.remember(state, action, reward, next_state, done)
    
        # Periodically perform replay
        if episode % replay_interval == 0:
            agent.replay(batch_size)
    
        # Save model weights periodically
        if episode % save_interval == 0:
            agent.save("agent_model.weights.h5")
    
        # Render the environment
        env.render(screen)
    
        # Update display
        pygame.display.update()
    
        # Check if the episode is finished
        if done:
            episode += 1
            print("Episode:", episode)
            env.reset()
    
        tra.draw(screen)
        bgg.draw(screen)
    # Save model weights after training
    

pygame.quit()
