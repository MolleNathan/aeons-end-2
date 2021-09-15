class Player:
    def __init__(self,name, number, power, maxCharge, starterBreach, deck, hand):
        self.name = name
        self.number = number
        self.deck = deck
        self.hand = hand
        self.discard = []
        self.power = power
        self.maxHealth = 12
        self.maxCharge = maxCharge
        self.charge = 0
        self.health = 12
        self.starterBreach = starterBreach
        self.spellBoard = [None, None, None, None]


    def playerDiscardSpell(self,index):
        spellDiscarded = self.spellBoard[index]
        self.spellBoard.remove(index)
        self.discard.add(spellDiscarded)

    def looseCharge(self, nbChargeToLoose):
        self.charge -= nbChargeToLoose

    def checkEffet(self,effect):
        isPossible = False
        if effect == 2:
            if self.charge > 0:
                return isPossible

        return isPossible


    def doEffect(self, effect):
        if effect == 2:
            self.charge -= 1