import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from TauPOG.TauIDSFs.TauIDSFTool import TauIDSFTool

def CalculateETauFakeRateWeight(self,theTree):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.value[0] = self.eleSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateETauFakeRateWeight_Barrel_Up(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if abs(theTree.eta_2) < 1.5:
        self.uncertaintyVariationArrays[uncert][0] = self.eleSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Up')
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.eleSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateETauFakeRateWeight_Barrel_Down(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if abs(theTree.eta_2) < 1.5:
        self.uncertaintyVariationArrays[uncert][0] = self.eleSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Down')
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.eleSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateETauFakeRateWeight_Endcap_Up(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if abs(theTree.eta_2) > 1.5:
        self.uncertaintyVariationArrays[uncert][0] = self.eleSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Up')
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.eleSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateETauFakeRateWeight_Endcap_Down(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if abs(theTree.eta_2) > 1.5:
        self.uncertaintyVariationArrays[uncert][0] = self.eleSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Down')
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.eleSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

eTauFakeRateWeight_2016 = Weight()
eTauFakeRateWeight_2016.name = 'eTauFakeRateWeight'
eTauFakeRateWeight_2016.eleSFTool = TauIDSFTool("2016Legacy",'DeepTau2017v2p1VSe','VLoose')
eTauFakeRateWeight_2016.CalculateWeight = CalculateETauFakeRateWeight
eTauFakeRateWeight_2016.hasUpDownUncertainties = True
eTauFakeRateWeight_2016.uncertaintyVariationList = [
    "eTauFakeRateWeight_Barrel_UP",
    "eTauFakeRateWeight_Barrel_DOWN",
    "eTauFakeRateWeight_Endcap_UP",
    "eTauFakeRateWeight_Endcap_DOWN",
]
eTauFakeRateWeight_2016.InitUncertaintyVariations()
eTauFakeRateWeight_2016.uncertaintyVariationFunctions = {
    "eTauFakeRateWeight_Barrel_UP":CalculateETauFakeRateWeight_Barrel_Up,
    "eTauFakeRateWeight_Barrel_DOWN":CalculateETauFakeRateWeight_Barrel_Down,
    "eTauFakeRateWeight_Endcap_UP":CalculateETauFakeRateWeight_Endcap_Up,
    "eTauFakeRateWeight_Endcap_DOWN":CalculateETauFakeRateWeight_Endcap_Down,
}

eTauFakeRateWeight_2017 = Weight()
eTauFakeRateWeight_2017.name = 'eTauFakeRateWeight'
eTauFakeRateWeight_2017.eleSFTool = TauIDSFTool("2017ReReco",'DeepTau2017v2p1VSe','VLoose')
eTauFakeRateWeight_2017.CalculateWeight = CalculateETauFakeRateWeight
eTauFakeRateWeight_2017.hasUpDownUncertainties = True
eTauFakeRateWeight_2017.uncertaintyVariationList = [
    "eTauFakeRateWeight_Barrel_UP",
    "eTauFakeRateWeight_Barrel_DOWN",
    "eTauFakeRateWeight_Endcap_UP",
    "eTauFakeRateWeight_Endcap_DOWN",
]
eTauFakeRateWeight_2017.InitUncertaintyVariations()
eTauFakeRateWeight_2017.uncertaintyVariationFunctions = {
    "eTauFakeRateWeight_Barrel_UP":CalculateETauFakeRateWeight_Barrel_Up,
    "eTauFakeRateWeight_Barrel_DOWN":CalculateETauFakeRateWeight_Barrel_Down,
    "eTauFakeRateWeight_Endcap_UP":CalculateETauFakeRateWeight_Endcap_Up,
    "eTauFakeRateWeight_Endcap_DOWN":CalculateETauFakeRateWeight_Endcap_Down,
}

eTauFakeRateWeight_2018 = Weight()
eTauFakeRateWeight_2018.name = 'eTauFakeRateWeight'
eTauFakeRateWeight_2018.eleSFTool = TauIDSFTool("2018ReReco",'DeepTau2017v2p1VSe','VLoose')
eTauFakeRateWeight_2018.CalculateWeight = CalculateETauFakeRateWeight
eTauFakeRateWeight_2018.hasUpDownUncertainties = True
eTauFakeRateWeight_2018.uncertaintyVariationList = [
    "eTauFakeRateWeight_Barrel_UP",
    "eTauFakeRateWeight_Barrel_DOWN",
    "eTauFakeRateWeight_Endcap_UP",
    "eTauFakeRateWeight_Endcap_DOWN",
]
eTauFakeRateWeight_2018.InitUncertaintyVariations()
eTauFakeRateWeight_2018.uncertaintyVariationFunctions = {
    "eTauFakeRateWeight_Barrel_UP":CalculateETauFakeRateWeight_Barrel_Up,
    "eTauFakeRateWeight_Barrel_DOWN":CalculateETauFakeRateWeight_Barrel_Down,
    "eTauFakeRateWeight_Endcap_UP":CalculateETauFakeRateWeight_Endcap_Up,
    "eTauFakeRateWeight_Endcap_DOWN":CalculateETauFakeRateWeight_Endcap_Down,
}
