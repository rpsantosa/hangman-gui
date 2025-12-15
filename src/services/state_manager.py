import json

class StateManager:
    def __init__(self):
        self.state = {}

    def save_state(self, filename: str) -> None:
        with open(filename, 'w') as file:
            json.dump(self.state, file)

    def load_state(self, filename: str) -> None:
        try:
            with open(filename, 'r') as file:
                self.state = json.load(file)
        except FileNotFoundError:
            print("No saved state found. Starting a new game.")
            self.state = {}
        except json.JSONDecodeError:
            print("Error loading state. Starting a new game.")
            self.state = {}

    def set_state(self, key: str, value) -> None:
        self.state[key] = value

    def get_state(self, key: str):
        return self.state.get(key, None)