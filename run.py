import tracery
import random
from tracery.modifiers import base_english

CMythGenres = ['Ex Nihilo','World Diver','Emergence', 'Creation via Dismemberment','Split/Order']
GodNames = ['Emdos', 'Iren', 'Qhaais', 'Sierin','Xydos','Ynas','Conmos','Easis','Xuhanh','Phoaldin','Zubris','Dhovdite','Bodos','Vosarin','Imarin','Istar','Aion','Meotl','Matis','Myas','Udos','Cinean','Qytis','Mehrer']
DivineDomains = ['Sky','Sun','Moon',' Star', 'Light', 'Dawn', 'Storm', 'Wind','Thunder', 'Rain', 'Underworld','Earth','Nature','Water','Sea','River','Springs','Vegetation','Fertility','Forests','Animals','Artistry','Hunting','Healing','Wisdom','Fate','Time','Justice','Sleep','Wealth','Love','Oath','War','Death','Travellers',' Fire']
Titles = ['Commander', 'Exarch', 'Elder', 'Defender','Lord', 'Ruler', 'Supreme','Breaker','Sage']
WorldNames = ['Pluccoros','Blammaqar','Uddunor','Eossirat','Gleoddenem','Aeklinor','Jiafitis','Ceannomelan','Iakacyre','Vreverea','Xeonacion','Tosaxus','Eclumund','Xiyariel','Shaeddeaphere','Xeaqalar','Cucogoth','Eostroron','Fleotteamos','Drilidore','Aedeoque','Phaxoroth','Gliommetia','Ukkedin','Iafila']
VoidNames = ['Void','Gap','Hollow','Emptyness','Null']
CastleSynonyms = ['Acropolis','Alcazar','Citadel','Fort','Fortress','Hold','Keep','Manor','Palace', 'Safehold','Seat', 'Stronghold', 'Tower',  'Villa', 'Château']

rules = {
    'mythSynop': 'This is the tale of how #God#, the #Domain#-#Rank#, created the world of #World#.',
    'WorldName' : WorldNames,
    'GodName': GodNames,
    'GodDomain' : DivineDomains,
    'GodRank': Titles
    'origin': '#[God:#GodName#][Domain:#GodDomain#][Rank:#GodRank#][World:#WorldName#]mythSynop'
}



def randomMythGenre():
    mythGenre = random.choice(CMythGenres)
    print("Creation Myth Type is : " + mythGenre)
    if mythGenre == 'Ex Nihilo'
       exNihiloMyth =  {'creationMyth' : 'In the beginning, there was the #Void#. From their #Domain#-#Castle# they watched it for an eternity. Then, they gestured and spoke with voice without voice: "Let it be." And thus the world of #World# came to be.'}
       exNihiloOrigin = {'origin':'[Domain:#GodDomain#][World:#WorldName#]creationMyth'}
       rules.update(exNihiloMyth)
       rules.update(exNihiloOrigin)
       
       
       #    elif mythGenre == 'World Diver'
        
 #   elif mythGenre == 'Emergence'

 #   elif mythGenre == 'Creation vis Dismemberment'

 #   elif mythGenre == 'Split/Order'

 #   return






def main():
    randomMythGenre()
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    print(grammar.flatten("#mythSynop#"))  # prints, e.g., "Hello, world!"
    print(grammar.flatten('#creationMyth#'))


if __name__ == "__main__": main()
