import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        
        for color, count in balls.items():
            self.contents.extend([color] * count)
        
        print(self.contents)
    
    def draw(self, num_balls_drawn):
        draw_pot = []
        
        if num_balls_drawn >= len(self.contents):
            draw_pot = self.contents
            self.contents = []
        else:
            for i in range(num_balls_drawn):
                ball = self.contents.pop(random.randrange(0, len(self.contents)))
                draw_pot.append(ball)

        return draw_pot


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0

    for num in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        success = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                success = False
                break

        if success:
            successes += 1

    probability = successes / num_experiments
    return probability
