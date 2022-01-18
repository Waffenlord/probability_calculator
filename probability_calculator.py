import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for k, v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)
    
    def draw(self, balls_num):
        new_list = list()
        if balls_num > len(self.contents):
            new_list = self.contents[:]
            self.contents.clear()
            return new_list
        
        else:
            for _ in range(balls_num):
                ball = random.choice(self.contents)
                new_list.append(ball)
                self.contents.remove(ball)
            return new_list

    def draw_experiment(self, balls_num):
        new_list = list()
        if balls_num > len(self.contents):
            new_list = self.contents[:]
            return new_list
        
        else:
            for _ in range(balls_num):
                ball = random.choice(self.contents)
                new_list.append(ball)
                
            return new_list


def experiment(hat, expected_balls = {"blue":2, "red":1} , num_balls_drawn = 0, num_experiments = 0):
    expected = expected_balls
    ocurrence = 0
    exp = num_experiments
    draw = dict()
    binary = list()
    while exp > 0:    
        drawn = hat.draw_experiment(num_balls_drawn)
        
        for x in drawn:
            draw[x] = draw.get(x, 0) + 1
        
        for k in expected:
            if k in draw and expected[k] <= draw[k]:
                binary.append('1')
            else:
                binary.append('0')

        if not '0' in binary:
            ocurrence += 1

        binary.clear()
        draw.clear()
              
           
        exp -= 1
    
    
    return ocurrence / num_experiments

    

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)

print(probability)


