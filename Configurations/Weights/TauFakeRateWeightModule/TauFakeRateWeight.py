import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from TauPOG.TauIDSFs.TauIDSFTool import TauIDSFTool

def CalculateTauFakeRateWeight(self,theTree):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    self.value[0] = self.eleSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2) * self.muSFTool.getSFvsEta(tauVector.Eta(),theTree.gen_match_2)
    

tauFakeRateWeight_2016 = Weight()
tauFakeRateWeight_2016.name = 'TauFakeRateWeight'
tauFakeRateWeight_2016.eleSFTool = TauIDSFTool("2016Legacy",'antiEleMVA6','VLoose')
tauFakeRateWeight_2016.muSFTool = TauIDSFTool("2016Legacy",'antiMu3','Tight')
tauFakeRateWeight_2016.CalculateWeight = CalculateTauFakeRateWeight

tauFakeRateWeight_2017 = Weight()
tauFakeRateWeight_2017.name = 'TauFakeRateWeight'
tauFakeRateWeight_2017.eleSFTool = TauIDSFTool("2017ReReco",'antiEleMVA6','VLoose')
tauFakeRateWeight_2017.muSFTool = TauIDSFTool("2017ReReco",'antiMu3','Tight')
tauFakeRateWeight_2017.CalculateWeight = CalculateTauFakeRateWeight

tauFakeRateWeight_2018 = Weight()
tauFakeRateWeight_2018.name = 'TauFakeRateWeight'
tauFakeRateWeight_2018.eleSFTool = TauIDSFTool("2018ReReco",'antiEleMVA6','VLoose')
tauFakeRateWeight_2018.muSFTool = TauIDSFTool("2018ReReco",'antiMu3','Tight')
tauFakeRateWeight_2018.CalculateWeight = CalculateTauFakeRateWeight
