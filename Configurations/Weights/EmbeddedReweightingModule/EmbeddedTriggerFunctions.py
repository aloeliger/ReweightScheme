import ROOT

def CalculateEmbeddedTriggerWeight2016(self,theTree):
    theWeight = 1.0
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.embeddedWorkspace.w.var("m_pt").setVal(muVector.Pt())
    self.embeddedWorkspace.w.var("m_eta").setVal(muVector.Eta())
    self.embeddedWorkspace.w.var("m_iso").setVal(theTree.iso_1)
    self.embeddedWorkspace.w.var("gt_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt_eta").setVal(theTree.geneta_1)
    self.embeddedWorkspace.w.var("gt1_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt1_eta").setVal(theTree.geneta_1)
    #bugged gen_2 values
    #self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.genpt_2)
    #self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.geneta_2)
    self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.pt_2)
    self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.eta_2)
    self.embeddedWorkspace.w.var("t_pt").setVal(tauVector.Pt())
    self.embeddedWorkspace.w.var("t_eta").setVal(tauVector.Eta())
    self.embeddedWorkspace.w.var("t_phi").setVal(tauVector.Phi())
    self.embeddedWorkspace.w.var("t_dm").setVal(theTree.l2_decayMode)    

    if theTree.Trigger22:
        #theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg24_27_embed_kit_ratio").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_ic_embed_ratio").getVal()
    elif theTree.Trigger1920:
        #theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_MuTau_Mu20Leg_kit_ratio_embed").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_19_ic_embed_ratio").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("t_trg_mediumDeepTau_mutau_embed_ratio").getVal()

    self.value[0] = theWeight

def CalculateEmbeddedTriggerWeight2016_22UP(self,theTree,uncert):
    theWeight = 1.0
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.embeddedWorkspace.w.var("m_pt").setVal(muVector.Pt())
    self.embeddedWorkspace.w.var("m_eta").setVal(muVector.Eta())
    self.embeddedWorkspace.w.var("m_iso").setVal(theTree.iso_1)
    self.embeddedWorkspace.w.var("gt_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt_eta").setVal(theTree.geneta_1)
    self.embeddedWorkspace.w.var("gt1_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt1_eta").setVal(theTree.geneta_1)
    #bugged gen_2 values
    #self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.genpt_2)
    #self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.geneta_2)
    self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.pt_2)
    self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.eta_2)
    self.embeddedWorkspace.w.var("t_pt").setVal(tauVector.Pt())
    self.embeddedWorkspace.w.var("t_eta").setVal(tauVector.Eta())
    self.embeddedWorkspace.w.var("t_phi").setVal(tauVector.Phi())
    self.embeddedWorkspace.w.var("t_dm").setVal(theTree.l2_decayMode)    

    if theTree.Trigger22:
        #theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg24_27_embed_kit_ratio").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_ic_embed_ratio").getVal() * 1.02
    elif theTree.Trigger1920:
        #theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_MuTau_Mu20Leg_kit_ratio_embed").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_19_ic_embed_ratio").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("t_trg_mediumDeepTau_mutau_embed_ratio").getVal()

    self.uncertaintyVariationArrays[uncert][0] = theWeight

def CalculateEmbeddedTriggerWeight2016_22DOWN(self,theTree,uncert):
    theWeight = 1.0
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.embeddedWorkspace.w.var("m_pt").setVal(muVector.Pt())
    self.embeddedWorkspace.w.var("m_eta").setVal(muVector.Eta())
    self.embeddedWorkspace.w.var("m_iso").setVal(theTree.iso_1)
    self.embeddedWorkspace.w.var("gt_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt_eta").setVal(theTree.geneta_1)
    self.embeddedWorkspace.w.var("gt1_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt1_eta").setVal(theTree.geneta_1)
    #bugged gen_2 values
    #self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.genpt_2)
    #self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.geneta_2)
    self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.pt_2)
    self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.eta_2)
    self.embeddedWorkspace.w.var("t_pt").setVal(tauVector.Pt())
    self.embeddedWorkspace.w.var("t_eta").setVal(tauVector.Eta())
    self.embeddedWorkspace.w.var("t_phi").setVal(tauVector.Phi())
    self.embeddedWorkspace.w.var("t_dm").setVal(theTree.l2_decayMode)    

    if theTree.Trigger22:
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_ic_embed_ratio").getVal() * 0.98
    elif theTree.Trigger1920:
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_19_ic_embed_ratio").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("t_trg_mediumDeepTau_mutau_embed_ratio").getVal()

    self.uncertaintyVariationArrays[uncert][0] = theWeight

def CalculateEmbeddedTriggerWeight2016_1920UP(self,theTree,uncert):
    theWeight = 1.0
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.embeddedWorkspace.w.var("m_pt").setVal(muVector.Pt())
    self.embeddedWorkspace.w.var("m_eta").setVal(muVector.Eta())
    self.embeddedWorkspace.w.var("m_iso").setVal(theTree.iso_1)
    self.embeddedWorkspace.w.var("gt_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt_eta").setVal(theTree.geneta_1)
    self.embeddedWorkspace.w.var("gt1_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt1_eta").setVal(theTree.geneta_1)
    #bugged gen_2 values
    #self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.genpt_2)
    #self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.geneta_2)
    self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.pt_2)
    self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.eta_2)
    self.embeddedWorkspace.w.var("t_pt").setVal(tauVector.Pt())
    self.embeddedWorkspace.w.var("t_eta").setVal(tauVector.Eta())
    self.embeddedWorkspace.w.var("t_phi").setVal(tauVector.Phi())
    self.embeddedWorkspace.w.var("t_dm").setVal(theTree.l2_decayMode)    

    if theTree.Trigger22:
        #theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg24_27_embed_kit_ratio").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_ic_embed_ratio").getVal()
    elif theTree.Trigger1920:
        #theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_MuTau_Mu20Leg_kit_ratio_embed").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_19_ic_embed_ratio").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("t_trg_mediumDeepTau_mutau_embed_ratio_up").getVal()

    self.uncertaintyVariationArrays[uncert][0] = theWeight

def CalculateEmbeddedTriggerWeight2016_1920DOWN(self,theTree,uncert):
    theWeight = 1.0
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.embeddedWorkspace.w.var("m_pt").setVal(muVector.Pt())
    self.embeddedWorkspace.w.var("m_eta").setVal(muVector.Eta())
    self.embeddedWorkspace.w.var("m_iso").setVal(theTree.iso_1)
    self.embeddedWorkspace.w.var("gt_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt_eta").setVal(theTree.geneta_1)
    self.embeddedWorkspace.w.var("gt1_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt1_eta").setVal(theTree.geneta_1)
    #bugged gen_2 values
    #self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.genpt_2)
    #self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.geneta_2)
    self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.pt_2)
    self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.eta_2)
    self.embeddedWorkspace.w.var("t_pt").setVal(tauVector.Pt())
    self.embeddedWorkspace.w.var("t_eta").setVal(tauVector.Eta())
    self.embeddedWorkspace.w.var("t_phi").setVal(tauVector.Phi())
    self.embeddedWorkspace.w.var("t_dm").setVal(theTree.l2_decayMode)    

    if theTree.Trigger22:
        #theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg24_27_embed_kit_ratio").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_ic_embed_ratio").getVal()
    elif theTree.Trigger1920:
        #theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_MuTau_Mu20Leg_kit_ratio_embed").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_19_ic_embed_ratio").getVal()
        theWeight = theWeight * self.embeddedWorkspace.w.function("t_trg_mediumDeepTau_mutau_embed_ratio_down").getVal()

    self.uncertaintyVariationArrays[uncert][0] = theWeight

def CalculateEmbeddedTriggerWeight1718(self,theTree):
    theWeight = 1.0
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.embeddedWorkspace.w.var("m_pt").setVal(muVector.Pt())
    self.embeddedWorkspace.w.var("m_eta").setVal(muVector.Eta())
    self.embeddedWorkspace.w.var("m_iso").setVal(theTree.iso_1)
    self.embeddedWorkspace.w.var("gt_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt_eta").setVal(theTree.geneta_1)
    self.embeddedWorkspace.w.var("gt1_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt1_eta").setVal(theTree.geneta_1)
    #bugged gen_2 values
    #self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.genpt_2)
    #self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.geneta_2)
    self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.pt_2)
    self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.eta_2)
    self.embeddedWorkspace.w.var("t_pt").setVal(tauVector.Pt())
    self.embeddedWorkspace.w.var("t_eta").setVal(tauVector.Eta())
    self.embeddedWorkspace.w.var("t_phi").setVal(tauVector.Phi())
    self.embeddedWorkspace.w.var("t_dm").setVal(theTree.l2_decayMode)    

    if(theTree.Trigger24 or theTree.Trigger27):
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_ic_embed_ratio").getVal()
    elif(theTree.Trigger2027):
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_20_ic_embed_ratio").getVal() #mu leg
        theWeight = theWeight * self.embeddedWorkspace.w.function("t_trg_mediumDeepTau_mutau_embed_ratio").getVal()#tau leg
    self.value[0] = theWeight

def CalculateEmbeddedTriggerWeight1718_24or27UP(self,theTree,uncert):
    theWeight = 1.0
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.embeddedWorkspace.w.var("m_pt").setVal(muVector.Pt())
    self.embeddedWorkspace.w.var("m_eta").setVal(muVector.Eta())
    self.embeddedWorkspace.w.var("m_iso").setVal(theTree.iso_1)
    self.embeddedWorkspace.w.var("gt_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt_eta").setVal(theTree.geneta_1)
    self.embeddedWorkspace.w.var("gt1_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt1_eta").setVal(theTree.geneta_1)
    #bugged gen_2 values
    #self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.genpt_2)
    #self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.geneta_2)
    self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.pt_2)
    self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.eta_2)
    self.embeddedWorkspace.w.var("t_pt").setVal(tauVector.Pt())
    self.embeddedWorkspace.w.var("t_eta").setVal(tauVector.Eta())
    self.embeddedWorkspace.w.var("t_phi").setVal(tauVector.Phi())
    self.embeddedWorkspace.w.var("t_dm").setVal(theTree.l2_decayMode)    

    if(theTree.Trigger24 or theTree.Trigger27):
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_ic_embed_ratio").getVal() * 1.02
    elif(theTree.Trigger2027):
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_20_ic_embed_ratio").getVal() #mu leg
        theWeight = theWeight * self.embeddedWorkspace.w.function("t_trg_mediumDeepTau_mutau_embed_ratio").getVal()#tau leg
    self.uncertaintyVariationArrays[uncert][0] = theWeight

def CalculateEmbeddedTriggerWeight1718_24or27DOWN(self,theTree,uncert):
    theWeight = 1.0
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.embeddedWorkspace.w.var("m_pt").setVal(muVector.Pt())
    self.embeddedWorkspace.w.var("m_eta").setVal(muVector.Eta())
    self.embeddedWorkspace.w.var("m_iso").setVal(theTree.iso_1)
    self.embeddedWorkspace.w.var("gt_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt_eta").setVal(theTree.geneta_1)
    self.embeddedWorkspace.w.var("gt1_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt1_eta").setVal(theTree.geneta_1)
    #bugged gen_2 values
    #self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.genpt_2)
    #self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.geneta_2)
    self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.pt_2)
    self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.eta_2)
    self.embeddedWorkspace.w.var("t_pt").setVal(tauVector.Pt())
    self.embeddedWorkspace.w.var("t_eta").setVal(tauVector.Eta())
    self.embeddedWorkspace.w.var("t_phi").setVal(tauVector.Phi())
    self.embeddedWorkspace.w.var("t_dm").setVal(theTree.l2_decayMode)    

    if(theTree.Trigger24 or theTree.Trigger27):
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_ic_embed_ratio").getVal() * 0.98
    elif(theTree.Trigger2027):
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_20_ic_embed_ratio").getVal() #mu leg
        theWeight = theWeight * self.embeddedWorkspace.w.function("t_trg_mediumDeepTau_mutau_embed_ratio").getVal()#tau leg
    self.uncertaintyVariationArrays[uncert][0] = theWeight


def CalculateEmbeddedTriggerWeight1718_2027UP(self,theTree,uncert):
    theWeight = 1.0
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.embeddedWorkspace.w.var("m_pt").setVal(muVector.Pt())
    self.embeddedWorkspace.w.var("m_eta").setVal(muVector.Eta())
    self.embeddedWorkspace.w.var("m_iso").setVal(theTree.iso_1)
    self.embeddedWorkspace.w.var("gt_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt_eta").setVal(theTree.geneta_1)
    self.embeddedWorkspace.w.var("gt1_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt1_eta").setVal(theTree.geneta_1)
    #bugged gen_2 values
    #self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.genpt_2)
    #self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.geneta_2)
    self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.pt_2)
    self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.eta_2)
    self.embeddedWorkspace.w.var("t_pt").setVal(tauVector.Pt())
    self.embeddedWorkspace.w.var("t_eta").setVal(tauVector.Eta())
    self.embeddedWorkspace.w.var("t_phi").setVal(tauVector.Phi())
    self.embeddedWorkspace.w.var("t_dm").setVal(theTree.l2_decayMode)    

    if(theTree.Trigger24 or theTree.Trigger27):
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_ic_embed_ratio").getVal()
    elif(theTree.Trigger2027):
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_20_ic_embed_ratio").getVal() #mu leg
        theWeight = theWeight * self.embeddedWorkspace.w.function("t_trg_mediumDeepTau_mutau_embed_ratio_up").getVal()#tau leg
    self.uncertaintyVariationArrays[uncert][0] = theWeight

def CalculateEmbeddedTriggerWeight1718_2027DOWN(self,theTree,uncert):
    theWeight = 1.0
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    self.embeddedWorkspace.w.var("m_pt").setVal(muVector.Pt())
    self.embeddedWorkspace.w.var("m_eta").setVal(muVector.Eta())
    self.embeddedWorkspace.w.var("m_iso").setVal(theTree.iso_1)
    self.embeddedWorkspace.w.var("gt_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt_eta").setVal(theTree.geneta_1)
    self.embeddedWorkspace.w.var("gt1_pt").setVal(theTree.genpt_1)
    self.embeddedWorkspace.w.var("gt1_eta").setVal(theTree.geneta_1)
    #bugged gen_2 values
    #self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.genpt_2)
    #self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.geneta_2)
    self.embeddedWorkspace.w.var("gt2_pt").setVal(theTree.pt_2)
    self.embeddedWorkspace.w.var("gt2_eta").setVal(theTree.eta_2)
    self.embeddedWorkspace.w.var("t_pt").setVal(tauVector.Pt())
    self.embeddedWorkspace.w.var("t_eta").setVal(tauVector.Eta())
    self.embeddedWorkspace.w.var("t_phi").setVal(tauVector.Phi())
    self.embeddedWorkspace.w.var("t_dm").setVal(theTree.l2_decayMode)    

    if(theTree.Trigger24 or theTree.Trigger27):
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_ic_embed_ratio").getVal()
    elif(theTree.Trigger2027):
        theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_20_ic_embed_ratio").getVal() #mu leg
        theWeight = theWeight * self.embeddedWorkspace.w.function("t_trg_mediumDeepTau_mutau_embed_ratio").getVal()#tau leg
    self.uncertaintyVariationArrays[uncert][0] = theWeight


