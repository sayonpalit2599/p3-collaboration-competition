import torch.nn.functional as F

# Define hyperparameters
                           
SEED = 33                          # Random seed

NUM_EPISODES = 5000                # Max num of episodes
NUM_STEPS = 1000                   # Max timesteps per episodes 
UPDATE_EVERY = 20                  # Learning timestep interval
MULTIPLE_LEARN_PER_UPDATE = 10     # Number of learning passes

BUFFER_SIZE = int(1e6)             # replay buffer size
BATCH_SIZE = 128                   # minibatch size

ACTOR_FC1_UNITS = 400              # Number of units for layer 1 in the actor model
ACTOR_FC2_UNITS = 300              # Number of units for layer 2 in the actor model
CRITIC_FCS1_UNITS = 400            # Number of units for layer 1 in the critic model
CRITIC_FC2_UNITS = 300             # Number of units for layer 2 in the critic model
NON_LIN = F.relu                   # Non linearity operator used in the model
LR_ACTOR = 1e-3                    # learning rate of the actor 
LR_CRITIC = 1e-3                   # learning rate of the critic
WEIGHT_DECAY = 0                   # L2 weight decay

GAMMA = 0.995                      # Discount factor
TAU = 1e-3                         # For soft update of target parameters
CLIP_CRITIC_GRADIENT = False       # Clip gradient during Critic optimization

# Ornstein-Uhlenbeck noise

ADD_OU_NOISE = True                # Add Ornstein-Uhlenbeck noise
MU = 0.                            # Ornstein-Uhlenbeck noise parameter
THETA = 0.15                       # Ornstein-Uhlenbeck noise parameter
SIGMA = 0.2                        # Ornstein-Uhlenbeck noise parameter
NOISE = 1.0                        # Initial Noise Amplitude 
NOISE_REDUCTION = 1e-6     # Noise amplitude decay ratio
model_dir = 'weight1'