class Player:
    player_count=0

    def Track_player(self,name,level):
        self.name=name
        self.level=level
        Player.player_count+=1
        return (f"Name {self.name} and level is {self.level}")
    def count_player(self):
        return self.player_count

ob1=Player()
print(ob1.Track_player("Ankit",5))
print(ob1.Track_player("Amit",2))

print(ob1.count_player())