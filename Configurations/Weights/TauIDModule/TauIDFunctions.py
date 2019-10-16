import ROOT

def CalculateTauIDWeight(self,theTree):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.value[0] = self.SFTool.getSFvsPT(tauVector.Pt())

def CalculateTauIDWeight_pT0to35_UP(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.uncertaintyVariationArrays[uncert][0] = self.SFTool.getSFvsPT(tauVector.Pt())
    if(tauVector.Pt() < 35.0):
        self.uncertaintyVariationArrays[uncert][0] = self.SFTool.getSFvsPT(tauVector.Pt(),unc='Up')

def CalculateTauIDWeight_pT0to35_DOWN(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.uncertaintyVariationArrays[uncert][0] = self.SFTool.getSFvsPT(tauVector.Pt())
    if(tauVector.Pt() < 35.0):
        self.uncertaintyVariationArrays[uncert][0] = self.SFTool.getSFvsPT(tauVector.Pt(),unc='Down')

def CalculateTauIDWeight_pT35to40_UP(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.uncertaintyVariationArrays[uncert][0] = self.SFTool.getSFvsPT(tauVector.Pt())
    if(tauVector.Pt() > 35.0 and tauVector.Pt() < 40.0):
        self.uncertaintyVariationArrays[uncert][0] = self.SFTool.getSFvsPT(tauVector.Pt(),unc='Up')

def CalculateTauIDWeight_pT35to40_DOWN(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.uncertaintyVariationArrays[uncert][0] = self.SFTool.getSFvsPT(tauVector.Pt())
    if(tauVector.Pt() > 35.0 and tauVector.Pt() < 40.0):
        self.uncertaintyVariationArrays[uncert][0] = self.SFTool.getSFvsPT(tauVector.Pt(),unc='Down')

def CalculateTauIDWeight_pTgt40_UP(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.uncertaintyVariationArrays[uncert][0] = self.SFTool.getSFvsPT(tauVector.Pt())
    if(tauVector.Pt() > 40.0):
        self.uncertaintyVariationArrays[uncert][0] = self.SFTool.getSFvsPT(tauVector.Pt(),unc='Up')

def CalculateTauIDWeight_pTgt40_DOWN(self,theTree,uncert):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.uncertaintyVariationArrays[uncert][0] = self.SFTool.getSFvsPT(tauVector.Pt())
    if(tauVector.Pt() > 40.0):
        self.uncertaintyVariationArrays[uncert][0] = self.SFTool.getSFvsPT(tauVector.Pt(),unc='Down')
