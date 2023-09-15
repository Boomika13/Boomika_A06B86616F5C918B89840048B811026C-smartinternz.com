#Define the base class player
class player:
   def play(self):
     print("the player is playing cricket.")

#define the derived class Batsman
class Batsman(player):
     def play(self):
       print("the batsman is Batting.")  

#define the derived class Bowler
class Bowler (player):
  def play(self):
    print("the bowler is bowling.")

#create object of Batsman and Bowler classes
batsman=Batsman ()
bowler=Bowler ()

#call the play() method for each object
batsman.play()
bowler.play()


               


               