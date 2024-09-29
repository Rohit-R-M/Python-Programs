"""
Define class Movie derived from actor and director. Use constructor to 
initialize the members and display the details of movie by overriding the display function.
"""
class Actor:
    def __init__(self,name,age):
        self.actor_name=name
        self.actor_age=age
    def display(self):
        print(f'Actor name:{self.actor_name}\nActor age:{self.actor_age}')

class Director:
    def __init__(self,name,expirience):
        self.dir_name=name
        self.dir_expirience=expirience
    def display(self):
        print(f'Director name:{self.dir_name}\nDirector expirience:{self.dir_expirience}')

class Movie(Actor,Director):
    def __init__(self, a, b,c,d,e):
        Actor.__init__(self, a, b)
        Director.__init__(self, c, d)
        self.movie_name=e
    def display(self):
        Actor.display(self)
        Director.display(self)
        print(f'Movie name:{self.movie_name}')

movie=Movie(input("Enter the actor name: "),
            int(input("actor age: ")),
            input("Enter the director name: "),
            int(input("Enter the director age: ")),
            input("Enter the movie name: "))

movie.display()