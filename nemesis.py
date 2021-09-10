import random

from nemesisCard import NemesisCard
class Nemesis:
    def __init__(self, nemesisName):
        self.nemesisName = nemesisName
        self.health = None
        self.nemesisDeck = []
        self.nemesisCards = [[],[],[]]
        self.nemesisCardPersonnalCards = {
            "Rage": {
                1 : [],
                2 : [],
                3 : []
            }
        }
        self.cardLevel1 = []
        self.cardLevel2 = []
        self.cardLevel3 = []
        self.rageIncarneeFrappe = []
        self.nemesisToken = 0
        self.switcher = {"Rage": 70}
        self.createAllCards()
        self.nbCardToChoose = {
            1 : [1,3,5,8],
            2 : [3,5,6,7]
        }

    def setupNemesis(self,nbPlayers):
        self.health = self.switcher[self.nemesisName]
        self.createNemesisDeck(nbPlayers)
        self.additionnalSetup()

    def additionnalSetup(self):
        #If it's Rage Incarnne, create the "Frappe" deck and he starts with one nemesis Token
        if self.nemesisName == "Rage":
            invoquerRI = NemesisCard("Frappe","Invoquer","273",None,None,None,0)
            devasterRI = NemesisCard("Frappe","Dévaster","274",None,None,None,0)
            eviscererRI = NemesisCard("Frappe","Éviscérer","275",None,None,None,0)
            frenesieRI = NemesisCard("Frappe","Frénésie","276",None,None,None,0)
            raserRI = NemesisCard("Frappe","Raser","276",None,None,None,0)
            attraperRI = NemesisCard("Frappe","Attraper","278",None,None,None,0)
            self.rageIncarneeFrappe.extend([invoquerRI,devasterRI,eviscererRI,frenesieRI,raserRI,attraperRI])
            random.shuffle(self.rageIncarneeFrappe)
            self.nemesisToken = 1



    def createNemesisDeck(self,nbPlayers):
        lengthLevel1 = len(self.nemesisCards[0])
        lengthLevel2 = len(self.nemesisCards[1])
        lengthLevel3 = len(self.nemesisCards[2])


        for i in range(self.getCardByLevel(nbPlayers,1)):
            card1 = self.nemesisCards[0][random.randint(0,lengthLevel1-1)]
            self.cardLevel1.append(card1)
            self.nemesisCards[0].remove(card1)
            lengthLevel1 -= 1

        for k in range(self.getCardByLevel(nbPlayers,2)):
            card2 = self.nemesisCards[1][random.randint(0,lengthLevel2-1)]
            self.cardLevel2.append(card2)
            self.nemesisCards[1].remove(card2)
            lengthLevel2 -= 1

        for j in range(self.getCardByLevel(nbPlayers,3)):
            card3 = self.nemesisCards[2][random.randint(0,lengthLevel3-1)]
            self.cardLevel3.append(card3)
            self.nemesisCards[2].remove(card3)
            lengthLevel3 -= 1

        self.addNemesisPersonnalCards(self.cardLevel1,self.cardLevel2,self.cardLevel3)
        self.nemesisDeck.extend(self.cardLevel1)
        self.nemesisDeck.extend(self.cardLevel2)
        self.nemesisDeck.extend(self.cardLevel3)



    def getCardByLevel(self,nbPlayers,level):
        if level == 1 or level == 2:
            cardToChoose = self.nbCardToChoose[level][int(nbPlayers) - 1]
            return cardToChoose
        else:
            return 7

    def createAllCards(self):
        souffleDuLabyrinthe = NemesisCard("Serviteur","SouffleDuLabyrinthe","065",None,None,5,1)
        champDAgonie = NemesisCard("Pouvoir","Champs D'Agonie","204",2,"204",None,1)
        seigneurDuFleau = NemesisCard("Serviteur","Seigneur Du Fléau","205",None,None,6,1)
        saignementStatique = NemesisCard("Pouvoir","Saignement Statique","206",3,None,None,1)
        oeilduNeant = NemesisCard("Pouvoir","Oeil Du Néant", "207",2,"207",None,1)
        cracheurDeBrouillard = NemesisCard("Serviteur","Cracheur De Brouillard","208",None,None,5,1)
        embrocher = NemesisCard("Attaque","Embrocher","209",None,None,None,1)
        massacre = NemesisCard("Attaque","Massacre","210",None,None,None,1)
        cielTisse = NemesisCard("Pouvoir","Ciel Tissé","211",2,"211",None,1)
        affliction = NemesisCard("Attaque","Affliction","W205",None,None,None,1)
        droneDesCatacombes = NemesisCard("Serviteur", "Drone Des Catacombes", "W206", None, None, 5, 1)
        fileuseHurlante = NemesisCard("Serviteur", "Fileuse Hurlante", "W207", None, None, 5, 1)
        empietement = NemesisCard("Attaque", "Empiètement", "W207", None, None, None, 1)
        coeurDuNeant = NemesisCard("Pouvoir", "Coeur Du Néant", "W208", 2, "W208", None, 1)
        nuitSansFin = NemesisCard("Pouvoir", "Nuit Sans Fin", "W210", 3, None, None, 1)
        annulation = NemesisCard("Attaque", "Annulation", "W211", None, None, None, 1)
        collisionDesPlans = NemesisCard("Pouvoir","Collision Des Plans","W212",2,"W212",None,1)
        detritus = NemesisCard("Attaque", "Détritus", "W213", None, None, None, 1)
        self.nemesisCards[0].extend([souffleDuLabyrinthe,champDAgonie,seigneurDuFleau,saignementStatique,oeilduNeant,cracheurDeBrouillard,embrocher,massacre,cielTisse,affliction,droneDesCatacombes,fileuseHurlante,empietement,coeurDuNeant,collisionDesPlans,nuitSansFin,annulation,detritus])

        aggression = NemesisCard("Attaque", "Aggression", "066", None, None, None, 2)
        reveil = NemesisCard("Attaque", "Réveil", "212", None, None, None, 2)
        cauteriseur = NemesisCard("Serviteur", "Cautériseur", "213", None, None, 3, 2)
        dissiper = NemesisCard("Attaque", "Dissiper", "214", None, None, None, 2)
        machoireAceree = NemesisCard("Serviteur", "Mâchoire-Acérée", "215", None, None, 11, 2)
        devaster = NemesisCard("Attaque", "Dévaster", "216", None, None, None, 2)
        rayontPulverisant = NemesisCard("Pouvoir", "Rayon Pulvérisant", "217", 1, None, None, 2)
        porteVenin = NemesisCard("Serviteur", "Porte-Venin", "218", None, None, 9, 2)
        soleilAphotique = NemesisCard("Pouvoir", "Soleil Aphotique", "W214", 2, "W214", None, 2)
        fleauDuChaos = NemesisCard("Pouvoir", "Fléeau du Chaos", "W215", 2, "W215", None, 2)
        terreurDesMages = NemesisCard("Serviteur", "Terreur Des Mages", "W216", None, None, 9, 2)
        racineEstropiantes = NemesisCard("Serviteur", "Racines Estropiantes", "W217", None, None, 12, 2)
        gyreMorbide = NemesisCard("Pouvoir", "Gyre Morbide", "W218", 1, "W218", None, 2)
        mutilation = NemesisCard("Attaque", "Mutilation", "W219", None, None, None, 2)
        alphaScion = NemesisCard("Serviteur", "Alpha-Scion", "W220", None, None, 11, 2)
        chatiment = NemesisCard("Attaque", "Châtiment", "W221", None, None, None, 2)
        self.nemesisCards[1].extend([aggression,reveil,cauteriseur,dissiper,machoireAceree,devaster,rayontPulverisant,porteVenin,soleilAphotique,fleauDuChaos,terreurDesMages,
                                    racineEstropiantes,gyreMorbide,mutilation,alphaScion,chatiment])

        sinistreAbattoir = NemesisCard("Pouvoir", "Sinistre Abattoir", "067", 2, "067", None, 3)
        egideDeLaRuine = NemesisCard("Pouvoir", "Égide De La Ruine", "219", 1, "219", None, 3)
        rassemblerLesOmbres = NemesisCard("Attaque", "Rassembler Les Ombres", "220", None, None, None, 3)
        leDechiquete = NemesisCard("Serviteur", "Le Déchiqueté", "221", None, None, 14, 3)
        aneantir = NemesisCard("Attaque", "Anéantir", "222", None, None, None, 3)
        ruptureDeLaRealite = NemesisCard("Pouvoir", "Rupture De La Réalité", "223", 1, "223", None, 3)
        fracture = NemesisCard("Attaque", "Fracture", "224", None, None, None, 3)
        renverser = NemesisCard("Attaque", "Renverser", "225", None, None, None, 3)
        rituelApocalyptique = NemesisCard("Pouvoir", "Rituel Apocalyptique", "W222", 2, "W222", None, 3)
        bannissement = NemesisCard("Attaque","Bannissement", "W223", None, None, None, 3)
        destinCataclysmique = NemesisCard("Pouvoir", "Destin Cataclysmique", "W224", 1, "W224", None, 3)
        monstruositeDesAugures = NemesisCard("Serviteur", "Monstruosité Des Augures", "W225", None, None, 5, 3)
        englouttissement = NemesisCard("Attaque", "Engloutissement", "W226", None, None, None, 3)
        reprimande = NemesisCard("Attaque", "Réprimande", "W227", None, None, None, 3)
        etranglement = NemesisCard("Attaque", "Étranglement", "W228", None, None, None, 3)
        rayonFletrissant = NemesisCard("Pouvoir", "Rayon Flétrissant", "W229", 2, None, None, 3)
        self.nemesisCards[2].extend([sinistreAbattoir, egideDeLaRuine, rassemblerLesOmbres, leDechiquete, aneantir, ruptureDeLaRealite, fracture, renverser, rituelApocalyptique,
                                    bannissement, destinCataclysmique, monstruositeDesAugures, englouttissement, reprimande, etranglement, rayonFletrissant])
        #########PersonnalCards
        #Rage Incarnée
        #Level 1
        rageIncarneeLevel1 = []
        fendreRI = NemesisCard("Attaque","Fendre","264",None,None,None,1)
        provocateursRI = NemesisCard("Serviteur","Provocateurs","265",None,None,5,1)
        colereInflechissableRI = NemesisCard("Attaque","Colère Infléchissable","266",None,None,None,1)
        rageIncarneeLevel1.extend([fendreRI,provocateursRI,colereInflechissableRI])
        self.nemesisCardPersonnalCards["Rage"][1] = rageIncarneeLevel1
        #Level 2
        rageIncarneeLevel2 = []
        criDuSangRI = NemesisCard("Pouvoir","Cri Du Sang","267",2,"267",None,2)
        invoquerLeCarnage = NemesisCard("Pouvoir","Invoquer Le Carnage","268",2,"268",None,2)
        meprisRI = NemesisCard("Serviteur","Mépris","269",None,None,9,2)
        rageIncarneeLevel2.extend([criDuSangRI,invoquerLeCarnage,meprisRI])
        self.nemesisCardPersonnalCards["Rage"][2] = rageIncarneeLevel2
        #Level 3
        rageIncarneeLevel3 = []
        avatardeLaColereRI = NemesisCard("Serviteur","Avatar De La Colère","270",None,None,16,3)
        assautRI = NemesisCard("Attaque","Assaut","271",None,None,None,3)
        mortInarreetableRI = NemesisCard("Pouboir","Mort Innarêtable","272",2,"278",None,3)
        rageIncarneeLevel3.extend([avatardeLaColereRI,assautRI,mortInarreetableRI])
        self.nemesisCardPersonnalCards["Rage"][3] = rageIncarneeLevel3

    def addNemesisPersonnalCards(self, cardLevel1, cardLevel2, cardLevel3):
        self.cardLevel1.append(self.nemesisCardPersonnalCards[self.nemesisName][1][0])
        self.cardLevel1.append(self.nemesisCardPersonnalCards[self.nemesisName][1][1])
        self.cardLevel1.append(self.nemesisCardPersonnalCards[self.nemesisName][1][2])
        random.shuffle(self.cardLevel1)
        self.cardLevel2.append(self.nemesisCardPersonnalCards[self.nemesisName][2][0])
        self.cardLevel2.append(self.nemesisCardPersonnalCards[self.nemesisName][2][1])
        self.cardLevel2.append(self.nemesisCardPersonnalCards[self.nemesisName][2][2])
        random.shuffle(self.cardLevel2)
        self.cardLevel3.append(self.nemesisCardPersonnalCards[self.nemesisName][3][0])
        self.cardLevel3.append(self.nemesisCardPersonnalCards[self.nemesisName][3][1])
        self.cardLevel3.append(self.nemesisCardPersonnalCards[self.nemesisName][3][2])
        random.shuffle(self.cardLevel3)

















