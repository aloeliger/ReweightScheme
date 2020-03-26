import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from Configurations.Weights import localWeightDataPath

def CreateZPTWeight(self,theTree):
    self.ZPTFile.w.var("z_gen_mass").setVal(theTree.genM)
    self.ZPTFile.w.var("z_gen_pt").setVal(theTree.genpT)
    self.value[0] = self.ZPTFile.w.function("zptmass_weight_nom").getVal()

def CreateZPTUpWeight(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = (self.value[0]-0.1*(self.value[0]-1))

def CreateZPTDownWeight(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = (self.value[0]+0.1*(self.value[0]-1))

ZPTWeight_2018 = Weight()
ZPTWeight_2018.name = 'ZPTWeighting'
ZPTWeight_2018.hasUpDownUncertainties = True
ZPTWeight_2018.ZPTFile = ROOT.TFile.Open(localWeightDataPath+"htt_scalefactors_legacy_2018.root")
ZPTWeight_2018.CalculateWeight = CreateZPTWeight
ZPTWeight_2018.uncertaintyVariationList = [
    "ZPT_UP",
    "ZPT_DOWN"
]
ZPTWeight_2018.InitUncertaintyVariations()
ZPTWeight_2018.uncertaintyVariationFunctions={
    "ZPT_UP": CreateZPTUpWeight,
    "ZPT_DOWN": CreateZPTDownWeight
    }

ZPTWeight_2017 = Weight()
ZPTWeight_2017.name = 'ZPTWeighting'
ZPTWeight_2017.hasUpDownUncertainties = True
ZPTWeight_2017.ZPTFile = ROOT.TFile.Open(localWeightDataPath+"htt_scalefactors_legacy_2017.root")
ZPTWeight_2017.CalculateWeight = CreateZPTWeight
ZPTWeight_2017.uncertaintyVariationList = [
    "ZPT_UP",
    "ZPT_DOWN"
    ]
ZPTWeight_2017.InitUncertaintyVariations()
ZPTWeight_2017.uncertaintyVariationFunctions = {
    "ZPT_UP": CreateZPTUpWeight,
    "ZPT_DOWN": CreateZPTDownWeight
    }

ZPTWeight_2016 = Weight()
ZPTWeight_2016.name = 'ZPTWeighting'
ZPTWeight_2016.hasUpDownUncertainties = True
ZPTWeight_2016.ZPTFile = ROOT.TFile.Open(localWeightDataPath+"htt_scalefactors_legacy_2016.root")
ZPTWeight_2016.CalculateWeight = CreateZPTWeight
ZPTWeight_2016.uncertaintyVariationList=[
    "ZPT_UP",
    "ZPT_DOWN"
    ]
ZPTWeight_2016.InitUncertaintyVariations()
ZPTWeight_2016.uncertaintyVariationFunctions={
    "ZPT_UP":CreateZPTUpWeight,
    "ZPT_DOWN":CreateZPTDownWeight
    }
