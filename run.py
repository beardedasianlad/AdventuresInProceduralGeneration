import tracery
import random
from tracery.modifiers import base_english

CMythGenres = ['Ex Nihilo','World Diver','Emergence', 'Creation via Dismemberment','Split/Order']

def randomMythGenre():
    mythGenre = random.choice(CMythGenres)
    return mythGenre



rules = {
    'mythSynop': 'This is the tale of how #GodName#, the #GodDomain#-#rank#, created the world as we know it.',
    'GodName': ['Emdos', 'Iren', 'Qhaais', 'Sierin','Xydos','Ynas','Conmos','Easis','Xuhanh','Phoaldin','Zubris','Dhovdite','Bodos','Vosarin','Imarin','Istar','Aion','Meotl','Matis','Myas','Udos','Cinean','Qytis','Mehrer'],
    'GodDomain' : ['Sky','Sun','Moon',' Star', 'Light', 'Dawn', 'Storm', 'Wind','Thunder', 'Rain', 'Underworld','Earth','Nature','Water','Sea','River','Springs','Vegetation','Fertility','Forests','Animals','Artistry','Hunting','Healing','Wisdom','Fate','Time','Justice','Sleep','Wealth','Love','Oath','War','Death','Travellers',' Fire'],
    'rank': ['Commander', 'Exarch', 'Elder', 'Defender','Lord', 'Ruler', 'Supreme','Breaker','Sage']
    
}



def main():
    print("Creation Myth Type is : " + randomMythGenre())
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    print(grammar.flatten("#mythSynop#"))  # prints, e.g., "Hello, world!"


if __name__ == "__main__": main()
