import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from TauPOG.TauIDSFs.TauIDSFTool import TauIDSFTool

def CalculateTauFakeRateWeight(self,theTree):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    #self.value[0] = self.eleSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2) * self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)        
    self.value[0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateTauFakeRateWeight_eta0to0p4_Up(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if(abs(tauVector.Eta())<0.4):
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Up')        
        #print("Scale Factor Up: "+str(self.uncertaintyVariationArrays[uncert][0]))
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)
        

def CalculateTauFakeRateWeight_eta0to0p4_Down(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if(abs(tauVector.Eta())<0.4):
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Down')
        #print("Scale Factor Down: "+str(self.uncertaintyVariationArrays[uncert][0]))
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateTauFakeRateWeight_eta0p4to0p8_Up(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if(abs(tauVector.Eta())>0.4 and abs(tauVector.Eta())<0.8):
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Up')
        #print("Scale Factor Up: "+str(self.uncertaintyVariationArrays[uncert][0]))
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateTauFakeRateWeight_eta0p4to0p8_Down(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if(abs(tauVector.Eta())>0.4 and abs(tauVector.Eta())<0.8):
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Down')
        #print("Scale Factor Down: "+str(self.uncertaintyVariationArrays[uncert][0]))
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateTauFakeRateWeight_eta0p8to1p2_Up(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if(abs(tauVector.Eta())>0.8 and abs(tauVector.Eta())<1.2):
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Up')
        #print("Scale Factor Up: "+str(self.uncertaintyVariationArrays[uncert][0]))
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateTauFakeRateWeight_eta0p8to1p2_Down(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if(abs(tauVector.Eta())>0.8 and abs(tauVector.Eta())<1.2):
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Down')
        #print("Scale Factor Down: "+str(self.uncertaintyVariationArrays[uncert][0]))
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateTauFakeRateWeight_eta1p2to1p7_Up(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if(abs(tauVector.Eta())>1.2 and abs(tauVector.Eta())<1.7):
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Up')
        #print("Scale Factor Up: "+str(self.uncertaintyVariationArrays[uncert][0]))
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateTauFakeRateWeight_eta1p2to1p7_Down(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if(abs(tauVector.Eta())>1.2 and abs(tauVector.Eta())<1.7):
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Down')
        #print("Scale Factor Down: "+str(self.uncertaintyVariationArrays[uncert][0]))
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateTauFakeRateWeight_etagt1p7_Up(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if(abs(tauVector.Eta())>1.7):
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Up')
        #print("Scale Factor Up: "+str(self.uncertaintyVariationArrays[uncert][0]))
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateTauFakeRateWeight_etagt1p7_Down(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    if(abs(tauVector.Eta())>1.7):
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2,unc='Down')
        #print("Scale Factor Down: "+str(self.uncertaintyVariationArrays[uncert][0]))
    else:
        self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)

def CalculateTauFakeRateWeight_TauPt30to40_Up(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)
    if(tauVector.Pt() > 30 and tauVector.Pt() < 40):
        self.uncertaintyVariationArrays[uncert][0] = self.uncertaintyVariationArrays[uncert][0] * 1.1

def CalculateTauFakeRateWeight_TauPt30to40_Down(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)
    if(tauVector.Pt() > 30 and tauVector.Pt() < 40):
        self.uncertaintyVariationArrays[uncert][0] = self.uncertaintyVariationArrays[uncert][0] * 0.9

def CalculateTauFakeRateWeight_TauPt40to50_Up(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)
    if(tauVector.Pt() > 40 and tauVector.Pt() < 50):
        self.uncertaintyVariationArrays[uncert][0] = self.uncertaintyVariationArrays[uncert][0] * 1.1

def CalculateTauFakeRateWeight_TauPt40to50_Down(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)
    if(tauVector.Pt() > 40 and tauVector.Pt() < 50):
        self.uncertaintyVariationArrays[uncert][0] = self.uncertaintyVariationArrays[uncert][0] * 0.9

def CalculateTauFakeRateWeight_TauPtgt50_Up(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)
    if(tauVector.Pt() > 50):
        self.uncertaintyVariationArrays[uncert][0] = self.uncertaintyVariationArrays[uncert][0] * 1.1

def CalculateTauFakeRateWeight_TauPtgt50_Down(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.uncertaintyVariationArrays[uncert][0] = self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)
    if(tauVector.Pt() > 50):
        self.uncertaintyVariationArrays[uncert][0] = self.uncertaintyVariationArrays[uncert][0] * 0.9

tauFakeRateWeight_2016 = Weight()
tauFakeRateWeight_2016.name = 'TauFakeRateWeight'
tauFakeRateWeight_2016.eleSFTool = TauIDSFTool("2016Legacy",'DeepTau2017v2p1VSe','VVLoose')
tauFakeRateWeight_2016.muSFTool = TauIDSFTool("2016Legacy",'DeepTau2017v2p1VSmu','Tight')
tauFakeRateWeight_2016.CalculateWeight = CalculateTauFakeRateWeight
tauFakeRateWeight_2016.hasUpDownUncertainties = True
tauFakeRateWeight_2016.uncertaintyVariationList = [
    "TauFakeRateWeight_eta0to0p4_UP",
    "TauFakeRateWeight_eta0to0p4_DOWN",
    "TauFakeRateWeight_eta0p4to0p8_UP",
    "TauFakeRateWeight_eta0p4to0p8_DOWN",
    "TauFakeRateWeight_eta0p8to1p2_UP",
    "TauFakeRateWeight_eta0p8to1p2_DOWN",
    "TauFakeRateWeight_eta1p2to1p7_UP",
    "TauFakeRateWeight_eta1p2to1p7_DOWN",
    "TauFakeRateWeight_etagt1p7_UP",
    "TauFakeRateWeight_etagt1p7_DOWN",
    "TauFakeRateWeight_taupt30to40_UP",
    "TauFakeRateWeight_taupt30to40_DOWN",
    "TauFakeRateWeight_taupt40to50_UP",
    "TauFakeRateWeight_taupt40to50_DOWN",
    "TauFakeRateWeight_tauptgt50_UP",
    "TauFakeRateWeight_tauptgt50_DOWN",
]
tauFakeRateWeight_2016.InitUncertaintyVariations()
tauFakeRateWeight_2016.uncertaintyVariationFunctions = {
    "TauFakeRateWeight_eta0to0p4_UP":CalculateTauFakeRateWeight_eta0to0p4_Up,
    "TauFakeRateWeight_eta0to0p4_DOWN":CalculateTauFakeRateWeight_eta0to0p4_Down,
    "TauFakeRateWeight_eta0p4to0p8_UP":CalculateTauFakeRateWeight_eta0p4to0p8_Up,
    "TauFakeRateWeight_eta0p4to0p8_DOWN":CalculateTauFakeRateWeight_eta0p4to0p8_Down,
    "TauFakeRateWeight_eta0p8to1p2_UP":CalculateTauFakeRateWeight_eta0p8to1p2_Up,
    "TauFakeRateWeight_eta0p8to1p2_DOWN":CalculateTauFakeRateWeight_eta0p8to1p2_Down,
    "TauFakeRateWeight_eta1p2to1p7_UP":CalculateTauFakeRateWeight_eta1p2to1p7_Up,
    "TauFakeRateWeight_eta1p2to1p7_DOWN":CalculateTauFakeRateWeight_eta1p2to1p7_Down,
    "TauFakeRateWeight_etagt1p7_UP":CalculateTauFakeRateWeight_etagt1p7_Up,
    "TauFakeRateWeight_etagt1p7_DOWN":CalculateTauFakeRateWeight_etagt1p7_Down,
    "TauFakeRateWeight_taupt30to40_UP":CalculateTauFakeRateWeight_TauPt30to40_Up,
    "TauFakeRateWeight_taupt30to40_DOWN":CalculateTauFakeRateWeight_TauPt30to40_Down,
    "TauFakeRateWeight_taupt40to50_UP":CalculateTauFakeRateWeight_TauPt40to50_Up,
    "TauFakeRateWeight_taupt40to50_DOWN":CalculateTauFakeRateWeight_TauPt40to50_Down,
    "TauFakeRateWeight_tauptgt50_UP":CalculateTauFakeRateWeight_TauPtgt50_Up,
    "TauFakeRateWeight_tauptgt50_DOWN":CalculateTauFakeRateWeight_TauPtgt50_Down,
}

tauFakeRateWeight_2017 = Weight()
tauFakeRateWeight_2017.name = 'TauFakeRateWeight'
tauFakeRateWeight_2017.eleSFTool = TauIDSFTool("2017ReReco",'DeepTau2017v2p1VSe','VVLoose')
tauFakeRateWeight_2017.muSFTool = TauIDSFTool("2017ReReco",'DeepTau2017v2p1VSmu','Tight')
tauFakeRateWeight_2017.CalculateWeight = CalculateTauFakeRateWeight
tauFakeRateWeight_2017.hasUpDownUncertainties = True
tauFakeRateWeight_2017.uncertaintyVariationList = [
    "TauFakeRateWeight_eta0to0p4_UP",
    "TauFakeRateWeight_eta0to0p4_DOWN",
    "TauFakeRateWeight_eta0p4to0p8_UP",
    "TauFakeRateWeight_eta0p4to0p8_DOWN",
    "TauFakeRateWeight_eta0p8to1p2_UP",
    "TauFakeRateWeight_eta0p8to1p2_DOWN",
    "TauFakeRateWeight_eta1p2to1p7_UP",
    "TauFakeRateWeight_eta1p2to1p7_DOWN",
    "TauFakeRateWeight_etagt1p7_UP",
    "TauFakeRateWeight_etagt1p7_DOWN",
    "TauFakeRateWeight_taupt30to40_UP",
    "TauFakeRateWeight_taupt30to40_DOWN",
    "TauFakeRateWeight_taupt40to50_UP",
    "TauFakeRateWeight_taupt40to50_DOWN",
    "TauFakeRateWeight_tauptgt50_UP",
    "TauFakeRateWeight_tauptgt50_DOWN",
]
tauFakeRateWeight_2017.InitUncertaintyVariations()
tauFakeRateWeight_2017.uncertaintyVariationFunctions = {
    "TauFakeRateWeight_eta0to0p4_UP":CalculateTauFakeRateWeight_eta0to0p4_Up,
    "TauFakeRateWeight_eta0to0p4_DOWN":CalculateTauFakeRateWeight_eta0to0p4_Down,
    "TauFakeRateWeight_eta0p4to0p8_UP":CalculateTauFakeRateWeight_eta0p4to0p8_Up,
    "TauFakeRateWeight_eta0p4to0p8_DOWN":CalculateTauFakeRateWeight_eta0p4to0p8_Down,
    "TauFakeRateWeight_eta0p8to1p2_UP":CalculateTauFakeRateWeight_eta0p8to1p2_Up,
    "TauFakeRateWeight_eta0p8to1p2_DOWN":CalculateTauFakeRateWeight_eta0p8to1p2_Down,
    "TauFakeRateWeight_eta1p2to1p7_UP":CalculateTauFakeRateWeight_eta1p2to1p7_Up,
    "TauFakeRateWeight_eta1p2to1p7_DOWN":CalculateTauFakeRateWeight_eta1p2to1p7_Down,
    "TauFakeRateWeight_etagt1p7_UP":CalculateTauFakeRateWeight_etagt1p7_Up,
    "TauFakeRateWeight_etagt1p7_DOWN":CalculateTauFakeRateWeight_etagt1p7_Down,
    "TauFakeRateWeight_taupt30to40_UP":CalculateTauFakeRateWeight_TauPt30to40_Up,
    "TauFakeRateWeight_taupt30to40_DOWN":CalculateTauFakeRateWeight_TauPt30to40_Down,
    "TauFakeRateWeight_taupt40to50_UP":CalculateTauFakeRateWeight_TauPt40to50_Up,
    "TauFakeRateWeight_taupt40to50_DOWN":CalculateTauFakeRateWeight_TauPt40to50_Down,
    "TauFakeRateWeight_tauptgt50_UP":CalculateTauFakeRateWeight_TauPtgt50_Up,
    "TauFakeRateWeight_tauptgt50_DOWN":CalculateTauFakeRateWeight_TauPtgt50_Down,
}

tauFakeRateWeight_2018 = Weight()
tauFakeRateWeight_2018.name = 'TauFakeRateWeight'
tauFakeRateWeight_2018.eleSFTool = TauIDSFTool("2018ReReco",'DeepTau2017v2p1VSe','VVLoose')
tauFakeRateWeight_2018.muSFTool = TauIDSFTool("2018ReReco",'DeepTau2017v2p1VSmu','Tight')
tauFakeRateWeight_2018.CalculateWeight = CalculateTauFakeRateWeight
tauFakeRateWeight_2018.hasUpDownUncertainties = True
tauFakeRateWeight_2018.uncertaintyVariationList = [
    "TauFakeRateWeight_eta0to0p4_UP",
    "TauFakeRateWeight_eta0to0p4_DOWN",
    "TauFakeRateWeight_eta0p4to0p8_UP",
    "TauFakeRateWeight_eta0p4to0p8_DOWN",
    "TauFakeRateWeight_eta0p8to1p2_UP",
    "TauFakeRateWeight_eta0p8to1p2_DOWN",
    "TauFakeRateWeight_eta1p2to1p7_UP",
    "TauFakeRateWeight_eta1p2to1p7_DOWN",
    "TauFakeRateWeight_etagt1p7_UP",
    "TauFakeRateWeight_etagt1p7_DOWN",
    "TauFakeRateWeight_taupt30to40_UP",
    "TauFakeRateWeight_taupt30to40_DOWN",
    "TauFakeRateWeight_taupt40to50_UP",
    "TauFakeRateWeight_taupt40to50_DOWN",
    "TauFakeRateWeight_tauptgt50_UP",
    "TauFakeRateWeight_tauptgt50_DOWN",
]
tauFakeRateWeight_2018.InitUncertaintyVariations()
tauFakeRateWeight_2018.uncertaintyVariationFunctions = {
    "TauFakeRateWeight_eta0to0p4_UP":CalculateTauFakeRateWeight_eta0to0p4_Up,
    "TauFakeRateWeight_eta0to0p4_DOWN":CalculateTauFakeRateWeight_eta0to0p4_Down,
    "TauFakeRateWeight_eta0p4to0p8_UP":CalculateTauFakeRateWeight_eta0p4to0p8_Up,
    "TauFakeRateWeight_eta0p4to0p8_DOWN":CalculateTauFakeRateWeight_eta0p4to0p8_Down,
    "TauFakeRateWeight_eta0p8to1p2_UP":CalculateTauFakeRateWeight_eta0p8to1p2_Up,
    "TauFakeRateWeight_eta0p8to1p2_DOWN":CalculateTauFakeRateWeight_eta0p8to1p2_Down,
    "TauFakeRateWeight_eta1p2to1p7_UP":CalculateTauFakeRateWeight_eta1p2to1p7_Up,
    "TauFakeRateWeight_eta1p2to1p7_DOWN":CalculateTauFakeRateWeight_eta1p2to1p7_Down,
    "TauFakeRateWeight_etagt1p7_UP":CalculateTauFakeRateWeight_etagt1p7_Up,
    "TauFakeRateWeight_etagt1p7_DOWN":CalculateTauFakeRateWeight_etagt1p7_Down,
    "TauFakeRateWeight_taupt30to40_UP":CalculateTauFakeRateWeight_TauPt30to40_Up,
    "TauFakeRateWeight_taupt30to40_DOWN":CalculateTauFakeRateWeight_TauPt30to40_Down,
    "TauFakeRateWeight_taupt40to50_UP":CalculateTauFakeRateWeight_TauPt40to50_Up,
    "TauFakeRateWeight_taupt40to50_DOWN":CalculateTauFakeRateWeight_TauPt40to50_Down,
    "TauFakeRateWeight_tauptgt50_UP":CalculateTauFakeRateWeight_TauPtgt50_Up,
    "TauFakeRateWeight_tauptgt50_DOWN":CalculateTauFakeRateWeight_TauPtgt50_Down,
}
