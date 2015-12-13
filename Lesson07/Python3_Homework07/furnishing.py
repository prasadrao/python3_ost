class furnishings():

    def __init__(self, room):
        self.room = room

class Bed(furnishings):
    name = "Bed"


class Sofa(furnishings):
    name = ""

class Table(furnishings):
    pass

class BookShelf(furnishings):
    pass

def map_the_home(home):
    furniture = {}
    for things in home:
        if things.room not in furniture.keys():
            furniture[things.room] = [things]
        else:
            furniture[things.room].append(things)

    return furniture

def counter(home):
    count_furn = { "Beds":0, "Bookshelves": 0, "Sofas":0, "Tables":0}
    for i in home:
        if type(i) == Bed:
            count_furn["Beds"] += 1

        elif type(i) == Sofa:
            count_furn["Sofas"] += 1

        elif type(i) == BookShelf:
            count_furn["Bookshelves"] += 1

        elif type(i) == Table:
            count_furn["Tables"] += 1

    for k, v in count_furn.items():
        print("{0} : {1}".format(k, v))

#def map_the_home(home):
#    furniture = {}
#    for things in home:
        #furniture[room.things] =

if __name__ == "__main__":

    home = [ Bed("BedRoom"), Sofa("Living Room") ]
    print(map_the_home(home))
    counter(home)
