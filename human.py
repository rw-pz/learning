
class Human:

    def __init__(self,name,surname,age,) -> None:
        self.name = name
        self.surname = surname
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name}, my surname is {self.surname}")
    
    def grow(self):
        self.age += 1

def display(people: list)-> None:
    for human in people:
        human.introduce()
    
def main():
    people = [Human("a","b",30),Human("c","d",35)]
    display(people)

if __name__ == "__main__":
    main()


#kwargs,args