
# class constructor
class Ranger:
  species = "human"
  def __init__(self, name, color, zord):
    self.name = name
    self.color = color
    self.zord = zord

# an instance method
  def morph(self):
    print(f"{self.zord}! It's morphin time!")

  # a static method
  def juicebar():
    print("Alpha 5 says meet at the juicebar, Rangers!")

# instantiate some rangers
Jason = Ranger("Jason", "Red", "Tyrannasorus")
Tommy = Ranger("Tommy", "Green", "Dragonzord")
Zack = Ranger("Zack", "Black", "Mastodon")
Kimberly = Ranger("Kimberly", "Pink", "Pterodactyl")
Trini = Ranger("Trini", "Yellow", "Sabre Tooth Tiger")
Billy = Ranger("Billy", "Blue", "Triceratops")

# call the static method
Ranger.juicebar()

# call the isntance method.  note the two acceptable forms of syntax to do so
Jason.morph()
Ranger.morph(Trini)
Billy.morph()
Zack.morph()
Kimberly.morph()
Ranger.morph(Tommy)