import random
map_height=5
map_width=10
down=[1,0] #y,x format
up=[-1,0]
right=[0,1]
left=[0,-1]
movement={"w":up,"d":right,"s":down,"a":left}

def snakemath(a,b):
        c=[0,0]
        c[0]=(a[0]+b[0])%map_height
        c[1]=(a[1]+b[1])%map_width
        return c

def applecheck(a,s):
    if s.bod[0]==a.p:
        a.reposition(s)
        s.grow()

class Snake():
    def __init__(self):
        self.alive = True
        self.length=1
        self.speed=1
        self.bod=[[0,0]] #y,x format
        self.dir=right 
    def dircheck(self,direction):
        if [self.dir[0]+direction[0],self.dir[1]+direction[1]]==[0,0]:
            return 0
        else:
            return 1
    def grow(self):
        self.length+=1
    # Use the stored old tail position
        self.bod.append(self._old_tail)
    def move(self,d):
        self.dir=d
        # Store old tail position before moving
        old_tail = self.bod[-1][:]
    # Move body segments (tail to head-1)
        for i in range(len(self.bod)-1, 0, -1):
            self.bod[i] = self.bod[i-1][:]
    
        self.bod[0] = snakemath(self.bod[0], d)
    # Store old tail for potential growth
        self._old_tail = old_tail
        for i in range(1,self.length):
            if self.bod[0]==self.bod[i]:
                self.alive=False
                print("Snake bit itself, game over")
                break
class Apple():
    def __init__(self):
        self.p=[random.randint(0,map_height-1),random.randint(0,map_width-1)] #y,x format
    
    def reposition(self,a):
        while True:
            self.p=[random.randint(0,map_height-1),random.randint(0,map_width-1)]
            if self.p not in a.bod:
                break
class Renderer():
    def __init__(self):
        self.map = [[1 for _ in range(map_width)] for _ in range(map_height)]
    
    def rend(self,snake,apple):
        for y in range(0,map_height): 
            for x in range(0,map_width):
                if [y,x] in snake.bod:
                    self.map[y][x]=0
                elif [y,x]==apple.p:
                    self.map[y][x]=8
                else:
                    self.map[y][x]=1
        for y in range(0,map_height): 
            for x in range(0,map_width):
                print(self.map[y][x],end=" ")
            print("\n")
    
    def gameplay(self,snake,apple):
            while snake.alive:
                print("SCORE:",snake.length-1)
                self.rend(snake,apple)
                d=input("enter dir")
                if d=='e':
                    break
                elif d in movement:
                    direction=movement[d]
                    print('input dir:',direction,'previous dir:',snake.dir)
                    if snake.dircheck(direction)==0:
                        print("snake cant 180")
                    else:
                        snake.move(direction)
                        print("After move dir:",snake.dir)
                        applecheck(apple,snake)
                else:
def test():
    s=Renderer()
    sk=Snake()
    a=Apple()
    s.gameplay(sk,a)

test()