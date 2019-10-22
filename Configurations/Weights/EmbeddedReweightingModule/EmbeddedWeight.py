import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from Configurations.Weights import localWeightDataPath

def CalculateEmbeddedWeight(self,theTree):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    theWeight = self.TauIDWeight
    if (theTree.genweight <= 1.0):
        theWeight = theWeight * theTree.genweight # can't forget this
    else:
        theWeight = theWeight* 0.0
    if theTree.l2_decayMode == 0:
        theWeight = theWeight * 0.975
    elif theTree.l2_decayMode == 1:
        theWeight = theWeight * 0.975 * 1.051
    elif theTree.l2_decayMode == 10:
        theWeight = theWeight * 0.975 * 0.975 * 0.975
    if self.year == "2018" or self.year == "2017":
        self.embeddedWorkspace.w.var("m_pt").setVal(muVector.Pt())
        self.embeddedWorkspace.w.var("m_eta").setVal(muVector.Eta())
        self.embeddedWorkspace.w.var("gt_pt").setVal(muVector.Pt())
        self.embeddedWorkspace.w.var("gt_eta").setVal(muVector.Pt())
        self.embeddedWorkspace.w.var("gt1_pt").setVal(muVector.Pt())
        self.embeddedWorkspace.w.var("gt1_eta").setVal(muVector.Eta())
        self.embeddedWorkspace.w.var("gt2_pt").setVal(tauVector.Pt())
        self.embeddedWorkspace.w.var("gt2_eta").setVal(tauVector.Eta())
        self.embeddedWorkspace.w.var("m_iso").setVal(theTree.iso_1)
        self.embeddedWorkspace.w.var("t_pt").setVal(tauVector.Pt())
        theWeight = theWeight*self.embeddedWorkspace.w.function("m_sel_trg_ratio").getVal()
        theWeight = theWeight*self.embeddedWorkspace.w.function("m_sel_idEmb_ratio").getVal()
        self.embeddedWorkspace.w.var("gt_pt").setVal(tauVector.Pt())
        self.embeddedWorkspace.w.var("gt_eta").setVal(tauVector.Eta())
        theWeight = theWeight*self.embeddedWorkspace.w.function("m_sel_idEmb_ratio").getVal()
        theWeight = theWeight*self.embeddedWorkspace.w.function("m_iso_binned_embed_kit_ratio").getVal()
        theWeight = theWeight*self.embeddedWorkspace.w.function("m_id_embed_kit_ratio").getVal()
        #this won't fly when 2016 comes around.
        #we'll need a year option that can be hardcoded with the kind 
        #of embedded weight (luckily)    
        if(theTree.Trigger24 or theTree.Trigger27):
            theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg24_27_embed_kit_ratio").getVal()
        elif(theTree.Trigger2027):
            if self.year == "2018":
                theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_binned_20_embed_ratio").getVal() #mu leg
                theWeight = theWeight * self.embeddedWorkspace.w.function("mt_emb_LooseChargedIsoPFTau27_tight_kit_ratio").getVal()#tau leg
            elif self.year == "2017":
                theWeight = theWeight * self.embeddedWorkspace.w.function("m_trg_MuTau_Mu20Leg_kit_ratio_embed").getVal()            
                theWeight = theWeight * self.embeddedWorkspace.w.function("mt_emb_LooseChargedIsoPFTau27_kit_ratio").getVal()                
    self.value[0] = theWeight

#2016 Weight still not complete!
embeddedWeight_2016 = Weight()
embeddedWeight_2016.name = 'EmbeddedWeighting'
embeddedWeight_2016.embeddedWorkspace = ROOT.TFile.Open(localWeightDataPath+"htt_scalefactors_legacy_2016.root")
embeddedWeight_2016.TauIDWeight = 0.85
embeddedWeight_2016.CalculateWeight = CalculateEmbeddedWeight
embeddedWeight_2016.year = "2016"

embeddedWeight_2017 = Weight()
embeddedWeight_2017.name = 'EmbeddedWeighting'
embeddedWeight_2017.embeddedWorkspace = ROOT.TFile.Open(localWeightDataPath+"htt_scalefactors_legacy_2017.root")
embeddedWeight_2017.TauIDWeight = 0.93
embeddedWeight_2017.CalculateWeight = CalculateEmbeddedWeight
embeddedWeight_2017.year = "2017"

embeddedWeight_2018 = Weight()
embeddedWeight_2018.name = 'EmbeddedWeighting'
embeddedWeight_2018.embeddedWorkspace = ROOT.TFile.Open(localWeightDataPath+"htt_scalefactors_legacy_2018.root")
embeddedWeight_2018.TauIDWeight = 0.88
embeddedWeight_2018.CalculateWeight = CalculateEmbeddedWeight
embeddedWeight_2018.year = "2018"
