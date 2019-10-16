import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from Configurations.Weights import localWeightDataPath

def CalculateMuTrackingWeight(self,theTree):
    self.muTrackingFile.w.var("m_eta").setVal(theTree.eta_1)
    self.value[0] = self.muTrackingFile.w.function("m_trk_ratio").getVal()

muTrackingWeight_2016 = Weight()
muTrackingWeight_2016.name = 'MuTrackingWeight'
muTrackingWeight_2016.muTrackingFile = ROOT.TFile.Open(localWeightDataPath+"htt_scalefactors_legacy_2016.root")
muTrackingWeight_2016.CalculateWeight = CalculateMuTrackingWeight

muTrackingWeight_2017 = Weight()
muTrackingWeight_2017.name = 'MuTrackingWeight'
muTrackingWeight_2017.muTrackingFile = ROOT.TFile.Open(localWeightDataPath+"htt_scalefactors_legacy_2017.root")
muTrackingWeight_2017.CalculateWeight = CalculateMuTrackingWeight

muTrackingWeight_2018 = Weight()
muTrackingWeight_2018.name = 'MuTrackingWeight'
muTrackingWeight_2018.muTrackingFile = ROOT.TFile.Open(localWeightDataPath+"htt_scalefactors_legacy_2018.root")
muTrackingWeight_2018.CalculateWeight = CalculateMuTrackingWeight
