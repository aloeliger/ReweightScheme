import ROOT

def GetDESYScaleFactor(dataHisto,MCHisto,ZMass):
    #get the data entry for this ZMass
    dataEntry = dataHisto.Eval(ZMass)
    #get the MC entry for this ZMass
    MCEntry = MCHisto.Eval(ZMass)
    #divide the two of them and return that.
    return dataEntry/MCEntry

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
        """
        if abs(muVector.Eta()) < 0.9:
            self.value[0] = GetDESYScaleFactor(self.DESYTriggerSFFile.ZMassEtaLt0p9_Data,self.DESYTriggerSFFile.ZMassEtaLt0p9_MC,(muVector+tauVector).M())
        elif abs(muVector.Eta()) >= 0.9 and abs(muVector.Eta()) < 1.2:
            self.value[0] = GetDESYScaleFactor(self.DESYTriggerSFFile.ZMassEta0p9to1p2_Data,self.DESYTriggerSFFile.ZMassEta0p9to1p2_MC,(muVector+tauVector).M())
        elif abs(muVector.Eta()) >= 1.2 and abs(muVector.Eta()) < 2.1:
            self.value[0] = GetDESYScaleFactor(self.DESYTriggerSFFile.ZMassEta1p2to2p1_Data,self.DESYTriggerSFFile.ZMassEta1p2to2p1_MC,(muVector+tauVector).M())
        else:
            self.value[0] = GetDESYScaleFactor(self.DESYTriggerSFFile.ZMassEtaGt2p1_Data,self.DESYTriggerSFFile.ZMassEtaGt2p1_MC,(muVector+tauVector).M())
        """
        #self.value[0] = 1.0
        #self.value[0] = 0.85 # completely ad-hoc. Fantastic agreement.        
    elif theTree.Trigger1920:                        
        #print ""
        #print("Mu Value: "+str(self.TriggerSFFile.w.function("m_trgMu19leg_eta2p1_desy_ratio").getVal()))
        #print("tau Value: "+str(self.tauSFs.getTriggerScaleFactor(tauVector.Pt(),tauVector.Eta(),tauVector.Phi(),decayMode)))
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
