class Person:
    def __init__(self, name):
        self.name = name
        self.children = []
    def add_child(self, child):
        self.children.append(child)

def find_person(person, name):
    if person.name == name:
        return person
    for child in person.children:
        search = find_person(child, name)
        if search:
            return search
    return None

alice = Person("Alice")
bob = Person("Bob")
carol = Person("Carol")
daniel = Person("Daniel")
emma = Person("Emma")
frank = Person("Frank")

alice.add_child(bob)
alice.add_child(carol)
bob.add_child(daniel)
carol.add_child(emma)
carol.add_child(frank)

search_name = input("Enter a name to search for: ")
result = find_person(carol, search_name)

if result:
    print("Found: ", result.name)
    if len(result.children) > 0:
        print("Children: ")
        for child in result.children:
            print(child.name)
    else:
        print("No children")
else:
    print("No person found.")
