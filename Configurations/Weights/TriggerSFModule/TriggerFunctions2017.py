import ROOT

def CalculateTriggerWeight2017(self,theTree):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.TriggerSFFile.w.var("m_pt").setVal(muVector.Pt())
    #self.TriggerSFFile.w.var("m_phi").setVal(muVector.Phi())
    self.TriggerSFFile.w.var("m_eta").setVal(abs(muVector.Eta()))
    self.TriggerSFFile.w.var("m_iso").setVal(theTree.iso_1)    
    self.TriggerSFFile.w.var("t_pt").setVal(tauVector.Pt())    
    self.TriggerSFFile.w.var("t_phi").setVal(tauVector.Phi())
    self.TriggerSFFile.w.var("t_eta").setVal(abs(tauVector.Eta()))
    self.TriggerSFFile.w.var("t_dm").setVal(theTree.l2_decayMode)
    #decayMode = theTree.l2_decayMode
    #if decayMode == 11:
    #    decayMode = 10
    if theTree.Trigger24 or theTree.Trigger27:
        self.value[0] = self.TriggerSFFile.w.function("m_trg_ic_ratio").getVal()
    elif theTree.Trigger2027:        
        self.value[0] = self.TriggerSFFile.w.function("t_trg_pog_deeptau_medium_mutau_ratio").getVal() * self.TriggerSFFile.w.function("m_trg_MuTau_Mu20Leg_desy_ratio").getVal()

def CalculateTriggerWeight2017_Trigger24or27_UP(self,theTree,uncert):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.TriggerSFFile.w.var("m_pt").setVal(muVector.Pt())
    #self.TriggerSFFile.w.var("m_phi").setVal(muVector.Phi())
    self.TriggerSFFile.w.var("m_eta").setVal(abs(muVector.Eta()))
    self.TriggerSFFile.w.var("m_iso").setVal(theTree.iso_1)    
    self.TriggerSFFile.w.var("t_pt").setVal(tauVector.Pt())    
    self.TriggerSFFile.w.var("t_phi").setVal(tauVector.Phi())
    self.TriggerSFFile.w.var("t_eta").setVal(abs(tauVector.Eta()))
    self.TriggerSFFile.w.var("t_dm").setVal(theTree.l2_decayMode)
    #decayMode = theTree.l2_decayMode
    #if decayMode == 11:
    #    decayMode = 10
    if theTree.Trigger24 or theTree.Trigger27:
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("m_trg_ic_ratio").getVal() * 1.02    
    elif theTree.Trigger2027:        
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("t_trg_pog_deeptau_medium_mutau_ratio").getVal() * self.TriggerSFFile.w.function("m_trg_MuTau_Mu20Leg_desy_ratio").getVal()

def CalculateTriggerWeight2017_Trigger24or27_DOWN(self,theTree,uncert):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.TriggerSFFile.w.var("m_pt").setVal(muVector.Pt())
    #self.TriggerSFFile.w.var("m_phi").setVal(muVector.Phi())
    self.TriggerSFFile.w.var("m_eta").setVal(abs(muVector.Eta()))
    self.TriggerSFFile.w.var("m_iso").setVal(theTree.iso_1)    
    self.TriggerSFFile.w.var("t_pt").setVal(tauVector.Pt())    
    self.TriggerSFFile.w.var("t_phi").setVal(tauVector.Phi())
    self.TriggerSFFile.w.var("t_eta").setVal(abs(tauVector.Eta()))
    self.TriggerSFFile.w.var("t_dm").setVal(theTree.l2_decayMode)
    #decayMode = theTree.l2_decayMode
    #if decayMode == 11:
    #    decayMode = 10
    if theTree.Trigger24 or theTree.Trigger27:
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("m_trg_ic_ratio").getVal() * 0.98    
    elif theTree.Trigger2027:        
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("t_trg_pog_deeptau_medium_mutau_ratio").getVal() * self.TriggerSFFile.w.function("m_trg_MuTau_Mu20Leg_desy_ratio").getVal()

def CalculateTriggerWeight2017_Trigger2027_UP(self,theTree,uncert):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.TriggerSFFile.w.var("m_pt").setVal(muVector.Pt())
    #self.TriggerSFFile.w.var("m_phi").setVal(muVector.Phi())
    self.TriggerSFFile.w.var("m_eta").setVal(abs(muVector.Eta()))
    self.TriggerSFFile.w.var("m_iso").setVal(theTree.iso_1)    
    self.TriggerSFFile.w.var("t_pt").setVal(tauVector.Pt())    
    self.TriggerSFFile.w.var("t_phi").setVal(tauVector.Phi())
    self.TriggerSFFile.w.var("t_eta").setVal(abs(tauVector.Eta()))
    self.TriggerSFFile.w.var("t_dm").setVal(theTree.l2_decayMode)
    #decayMode = theTree.l2_decayMode
    #if decayMode == 11:
    #    decayMode = 10
    if theTree.Trigger24 or theTree.Trigger27:
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("m_trg_ic_ratio").getVal()
    elif theTree.Trigger2027:        
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("t_trg_pog_deeptau_medium_mutau_ratio_up").getVal() * self.TriggerSFFile.w.function("m_trg_MuTau_Mu20Leg_desy_ratio").getVal() * 1.02

def CalculateTriggerWeight2017_Trigger2027_DOWN(self,theTree,uncert):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.TriggerSFFile.w.var("m_pt").setVal(muVector.Pt())
    #self.TriggerSFFile.w.var("m_phi").setVal(muVector.Phi())
    self.TriggerSFFile.w.var("m_eta").setVal(abs(muVector.Eta()))
    self.TriggerSFFile.w.var("m_iso").setVal(theTree.iso_1)    
    self.TriggerSFFile.w.var("t_pt").setVal(tauVector.Pt())    
    self.TriggerSFFile.w.var("t_phi").setVal(tauVector.Phi())
    self.TriggerSFFile.w.var("t_eta").setVal(abs(tauVector.Eta()))
    self.TriggerSFFile.w.var("t_dm").setVal(theTree.l2_decayMode)
    #decayMode = theTree.l2_decayMode
    #if decayMode == 11:
    #    decayMode = 10
    if theTree.Trigger24 or theTree.Trigger27:
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("m_trg_ic_ratio").getVal()
    elif theTree.Trigger2027:        
        self.uncertaintyVariationArrays[uncert][0] = self.TriggerSFFile.w.function("t_trg_pog_deeptau_medium_mutau_ratio_down").getVal() * self.TriggerSFFile.w.function("m_trg_MuTau_Mu20Leg_desy_ratio").getVal() * 0.98
