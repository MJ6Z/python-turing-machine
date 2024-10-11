
class TuringMachine:
    def __init__(self, states, tape, transitions, start_state):
        self.states = states
        self.tape = list(tape)
        self.head = 0  # Head position
        self.state = start_state
        self.transitions = transitions
    def step(self):
        current_symbol = self.tape[self.head]
        key = (self.state, current_symbol)

        if key in self.transitions:
            new_symbol, direction, new_state = self.transitions[key]
            self.tape[self.head] = new_symbol
            self.state = new_state

            # Move the head
            if direction == 'R':
                self.head += 1
                if self.head == len(self.tape):  # Expand the tape if necessary
                    self.tape.append('')
            elif direction == 'L':
                if self.head > 0:
                    self.head -= 1
                else:
                    self.tape.insert(0, '')
                    self.head = 0
        else:
            # No transition, halt the machine
            return "Halted"

        return None  # Continue running

    def get_tape(self):
        return ''.join(self.tape).strip()

    def run(self):
        while True:
            result = self.step()
            print("state: ",self.state,"head position: ",self.head,"tape: ",self.get_tape())
            if result:
                return result



#define the states.
states = {'q0', 'q1', "qf"}
#define the tape.
tape = "000010"
#define the transition function.
transitions = {
    ('q0', '0'): ('0', 'R', 'q0'),
    ('q0', '1'): ('0', 'R', 'q1'),
    ('q1', '0'): ('1', 'R', 'qf'),
    ('q1', '1'): ('0', 'R', 'qf'),
}
start_state = 'q0'

tm = TuringMachine(states, tape, transitions, start_state)
result = tm.run()
print(f"Tape after processing: '{tm.get_tape()}'")
print(f"Result: {result}")

