import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from Configurations.Weights import localWeightDataPath
from DESYScaleFactor import DESYScaleFactor

def CalculateMuIDIso_2016(self,theTree):
    muVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    self.MuIDIsoFile.w.var("m_pt").setVal(muVector.Pt())
    self.MuIDIsoFile.w.var("m_iso").setVal(theTree.iso_1)
    self.MuIDIsoFile.w.var("m_eta").setVal(abs(muVector.Eta()))
    self.value[0] = self.MuIDIsoFile.w.function("m_idiso_desy_ratio").getVal()

def CalculateMuIDIso(self,theTree):
    muVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    self.MuIDIsoFile.w.var("m_pt").setVal(muVector.Pt())
    self.MuIDIsoFile.w.var("m_iso").setVal(theTree.iso_1)
    self.MuIDIsoFile.w.var("m_eta").setVal(abs(muVector.Eta()))
    self.value[0] = self.MuIDIsoFile.w.function("m_idiso_binned_kit_ratio").getVal()
    
def CalculateMuIDIsoUsingDesyFactor(self,theTree):
    muVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    self.value[0] = self.scaleFactor.GetScaleFactor(muVector.Pt(),muVector.Eta())


muIDIsoWeight_2016 = Weight()
muIDIsoWeight_2016.name = 'MuIDIso'
muIDIsoWeight_2016.MuIDIsoFile = ROOT.TFile.Open(localWeightDataPath+'htt_scalefactors_legacy_2016.root')
muIDIsoWeight_2016.scaleFactor = DESYScaleFactor(localWeightDataPath+'Muon_Run2016_legacy_IdIso.root')
muIDIsoWeight_2016.CalculateWeight = CalculateMuIDIsoUsingDesyFactor

muIDIsoWeight_2017 = Weight()
muIDIsoWeight_2017.name = 'MuIDIso'
muIDIsoWeight_2017.MuIDIsoFile = ROOT.TFile.Open(localWeightDataPath+'htt_scalefactors_legacy_2017.root')
muIDIsoWeight_2017.scaleFactor=DESYScaleFactor(localWeightDataPath+'Muon_IdIso_IsoLt0.15_eff_RerecoFall17.root')
muIDIsoWeight_2017.CalculateWeight = CalculateMuIDIsoUsingDesyFactor

muIDIsoWeight_2018 = Weight()
muIDIsoWeight_2018.name = 'MuIDIso'
muIDIsoWeight_2018.MuIDIsoFile = ROOT.TFile.Open(localWeightDataPath+'htt_scalefactors_legacy_2018.root')
muIDIsoWeight_2018.scaleFactor = DESYScaleFactor(localWeightDataPath+'Muon_Run2018_IdIso.root')
muIDIsoWeight_2018.CalculateWeight = CalculateMuIDIsoUsingDesyFactor
