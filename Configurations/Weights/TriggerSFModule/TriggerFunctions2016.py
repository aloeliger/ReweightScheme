import ROOT

def CalculateTriggerWeight2016(self,theTree):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.TriggerSFFile.w.var("m_pt").setVal(muVector.Pt())
    self.TriggerSFFile.w.var("m_iso").setVal(theTree.iso_1)
    self.TriggerSFFile.w.var("m_eta").setVal(abs(muVector.Eta()))
    decayMode = theTree.l2_decayMode
    if decayMode == 11:
        decayMode = 10
    if theTree.Trigger22:        
        self.value[0] = self.TriggerSFFile.w.function("m_trgIsoMu22_desy_ratio").getVal()
    elif theTree.Trigger1920:                        
        self.value[0] = self.TriggerSFFile.w.function("m_trgMu19leg_eta2p1_desy_ratio").getVal() * self.tauSFs.getTriggerScaleFactor(tauVector.Pt(),tauVector.Eta(),tauVector.Phi(),decayMode)

def CalculateTriggerWeight2016_Trigger22_UP(self,theTree,uncert):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.TriggerSFFile.w.var("m_pt").setVal(muVector.Pt())
    self.TriggerSFFile.w.var("m_iso").setVal(theTree.iso_1)
    self.TriggerSFFile.w.var("m_eta").setVal(abs(muVector.Eta()))
    decayMode = theTree.l2_decayMode
    if decayMode == 11:
        decayMode = 10
    if theTree.Trigger22:        
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("m_trgIsoMu22_desy_ratio").getVal() * 1.02
    elif theTree.Trigger1920:                        
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("m_trgMu19leg_eta2p1_desy_ratio").getVal() * self.tauSFs.getTriggerScaleFactor(tauVector.Pt(),tauVector.Eta(),tauVector.Phi(),decayMode)

def CalculateTriggerWeight2016_Trigger22_DOWN(self,theTree,uncert):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.TriggerSFFile.w.var("m_pt").setVal(muVector.Pt())
    self.TriggerSFFile.w.var("m_iso").setVal(theTree.iso_1)
    self.TriggerSFFile.w.var("m_eta").setVal(abs(muVector.Eta()))
    decayMode = theTree.l2_decayMode
    if decayMode == 11:
        decayMode = 10
    if theTree.Trigger22:        
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("m_trgIsoMu22_desy_ratio").getVal() * 0.98
    elif theTree.Trigger1920:                        
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("m_trgMu19leg_eta2p1_desy_ratio").getVal() * self.tauSFs.getTriggerScaleFactor(tauVector.Pt(),tauVector.Eta(),tauVector.Phi(),decayMode)

def CalculateTriggerWeight2016_Trigger1920_UP(self,theTree,uncert):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.TriggerSFFile.w.var("m_pt").setVal(muVector.Pt())
    self.TriggerSFFile.w.var("m_iso").setVal(theTree.iso_1)
    self.TriggerSFFile.w.var("m_eta").setVal(abs(muVector.Eta()))
    decayMode = theTree.l2_decayMode
    if decayMode == 11:
        decayMode = 10
    if theTree.Trigger22:        
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("m_trgIsoMu22_desy_ratio").getVal()
    elif theTree.Trigger1920:                        
        self.value[0] = self.TriggerSFFile.w.function("m_trgMu19leg_eta2p1_desy_ratio").getVal() * self.tauSFs.getTriggerScaleFactorUncert(tauVector.Pt(),tauVector.Eta(),tauVector.Phi(),decayMode,'Up')

def CalculateTriggerWeight2016_Trigger1920_DOWN(self,theTree,uncert):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.TriggerSFFile.w.var("m_pt").setVal(muVector.Pt())
    self.TriggerSFFile.w.var("m_iso").setVal(theTree.iso_1)
    self.TriggerSFFile.w.var("m_eta").setVal(abs(muVector.Eta()))
    decayMode = theTree.l2_decayMode
    if decayMode == 11:
        decayMode = 10
    if theTree.Trigger22:        
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("m_trgIsoMu22_desy_ratio").getVal()
    elif theTree.Trigger1920:                        
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("m_trgMu19leg_eta2p1_desy_ratio").getVal() * self.tauSFs.getTriggerScaleFactorUncert(tauVector.Pt(),tauVector.Eta(),tauVector.Phi(),decayMode,'Down')
