import random

CMythGenres = ['Ex Nihilo','World Diver','Emergence', 'Creation via Dismemberment','Split/Order']
GodNames = ['Emdos', 'Iren', 'Qhaais', 'Sierin','Xydos','Ynas','Conmos','Easis','Xuhanh','Phoaldin','Zubris','Dhovdite','Bodos','Vosarin','Imarin','Istar','Aion','Meotl','Matis','Myas','Udos','Cinean','Qytis','Mehrer']
DivineDomains = ['Sky','Sun','Moon',' Star', 'Light', 'Dawn', 'Storm', 'Wind','Thunder', 'Rain', 'Underworld','Earth','Nature','Water','Sea','River','Springs','Vegetation','Fertility','Forests','Animals','Artistry','Hunting','Healing','Wisdom','Fate','Time','Justice','Sleep','Wealth','Love','Oath','War','Death','Travellers',' Fire']
Titles = ['Commander', 'Exarch', 'Elder', 'Defender','Lord', 'Ruler', 'Supreme','Breaker','Sage']
WorldNames = ['Pluccoros','Blammaqar','Uddunor','Eossirat','Gleoddenem','Aeklinor','Jiafitis','Ceannomelan','Iakacyre','Vreverea','Xeonacion','Tosaxus','Eclumund','Xiyariel','Shaeddeaphere','Xeaqalar','Cucogoth','Eostroron','Fleotteamos','Drilidore','Aedeoque','Phaxoroth','Gliommetia','Ukkedin','Iafila']
VoidNames = ['Void','Gap','Hollow','Emptyness','Null']
CastleSynonyms = ['Acropolis','Alcazar','Citadel','Fort','Fortress','Hold','Keep','Manor','Palace', 'Safehold','Seat', 'Stronghold', 'Tower',  'Villa', 'Château']


class God:
    def __init__(self):
        self.Name=random.choice(GodNames)
        self.Domain=random.choice(DivineDomains)
        self.Rank=random.choice(Titles)
        return;
    def getName(self):
        return self.Name
    def getDomain(self):
        return self.Domain
    def getRank(self):
        return self.Rank

class Myth:
    def __init__(self,CreatorGod):
        Creator=CreatorGod
        self.WorldName = random.choice(WorldNames)
        self.genre = random.choice(CMythGenres)
        return;
    def printSynopsis(self):
       print("This is the tale of how " + Creator.getName() + ", the" + Creator.getDomain() +"-" + Creator.getRank()+", created the world of "+ self.WorldName)
       return;

class Example():
    def main(self):
        #randomMythGenre()
        creatorGod = God()
        cMyth = Myth(creatorGod)
        cMyth.printSynopsis()
        return;

if __name__ == '__main__':
    Example().main()
#def randomMythGenre():
  #  mythGenre = random.choice(CMythGenres)
#    print("Creation Myth Type is : " + mythGenre)
#    if mythGenre == 'Ex Nihilo'
 #      exNihiloMyth =  {'creationMyth' : 'In the beginning, there was the #Void#. From their #Domain#-#Castle# they watched it for an eternity. Then, they gestured and spoke with voice without voice: "Let it be." And thus the world of #World# came to be.'}
 #      exNihiloOrigin = {'origin':'[Domain:#GodDomain#][World:#WorldName#]creationMyth'}
  #     rules.update(exNihiloMyth)
  #     rules.update(exNihiloOrigin)
       
       
       #    elif mythGenre == 'World Diver'
        
 #   elif mythGenre == 'Emergence'

 #   elif mythGenre == 'Creation vis Dismemberment'

 #   elif mythGenre == 'Split/Order'

 #   return
 