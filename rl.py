import random
from GameState import GameState


class NimQLearningBot:
    def __init__(self, num_piles, max_stones):
        self.num_piles = num_piles
        self.max_stones = max_stones
        self.q_table = {}  # Q-table implemented as a dictionary
        self.alpha = 0.1  # Learning rate
        self.gamma = 0.9  # Discount factor
        self.epsilon = 0.1  # Epsilon for epsilon-greedy policy

    def state_to_tuple(self, state):
        """
        Convert game state (list of pile sizes) to a tuple for use as dictionary key.
        """
        return tuple(set(state))

    def choose_action(self, state):
        """
        Epsilon-greedy action selection based on Q-values.
        """
        state_key = self.state_to_tuple(state)
        if random.random() < self.epsilon:
            # Random action (exploration)
            return random.randint(1, min(self.max_stones, max(state)))
        else:
            # Choose the best action based on Q-values (exploitation)
            if state_key not in self.q_table:
                # No Q-values for this state, choose randomly
                return random.randint(1, min(self.max_stones, max(state)))
            else:
                return max(range(1, min(self.max_stones, max(state)) + 1), key=lambda a: self.q_table[state_key].get(a, 0))

    def update_q_table(self, state, action, reward, next_state):
        """
        Update Q-values based on the Bellman equation.
        """
        state_key = self.state_to_tuple(state)
        next_state_key = self.state_to_tuple(next_state)
        current_q_value = self.q_table.setdefault(state_key, {}).get(action, 0)
        max_next_q_value = max(self.q_table.setdefault(next_state_key, {}).values(), default=0)
        new_q_value = current_q_value + self.alpha * (reward + self.gamma * max_next_q_value - current_q_value)
        self.q_table[state_key][action] = new_q_value

    def play_game(self, game):
        """
        Play a single game of Nim using Q-learning.
        """
        current_state = game.piles.copy()
        while not game.is_empty():
            action = self.choose_action(current_state)
            non_empty_piles = [i for i, stones in enumerate(current_state) if stones > 0]
            pile = random.choice(non_empty_piles)  # Choose a non-empty pile randomly
            stones_to_remove = min(action, current_state[pile])
            game.make_move(pile, stones_to_remove)
            next_state = game.piles.copy()
            reward = 1 if game.is_empty() else 0  # Reward 1 for winning the game
            self.update_q_table(current_state, action, reward, next_state)
            current_state = next_state

    def make_move(self, game):
        """
        Make a move in a game of Nim based on the learned Q-values.
        """
        current_state = game.piles.copy()
        state_key = self.state_to_tuple(current_state)
        if state_key not in self.q_table:
            # No Q-values for this state, choose randomly
            pile = random.choice([i for i, stones in enumerate(current_state) if stones > 0])
            stones_to_remove = random.randint(1, min(self.max_stones, current_state[pile]))
        else:
            # Choose action with the highest Q-value
            action = max(self.q_table[state_key], key=self.q_table[state_key].get)
            pile = random.choice([i for i, stones in enumerate(current_state) if stones > 0])
            stones_to_remove = min(action, current_state[pile])
        game.make_move(pile, stones_to_remove)


# Example usage:
# Initialize NimQLearningBot
bot = NimQLearningBot(num_piles=3, max_stones=5)

# Train the bot by playing multiple games
num_episodes = 100000
for _ in range(num_episodes):
    game = GameState([3, 4])  # Initialize the game state
    bot.play_game(game)

print(bot.q_table)

# Use the trained bot to play against a human player or another bot
game = GameState([3, 4])  # Initialize the game state
bot.make_move(game)
print(f"Bot makes move: {game.piles}")
