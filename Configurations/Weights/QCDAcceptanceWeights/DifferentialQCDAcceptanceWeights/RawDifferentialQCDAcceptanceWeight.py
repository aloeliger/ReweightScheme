import ROOT
from Configurations.Weights.WeightDefinition import Weight
from Configurations.Weights import localWeightDataPath

def CalculateRawWeight (self,theTree):
    self.value[0] = 1.0

def CalculateRawWeightUP(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2

def CalculateRawWeightDOWN(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5

ggHRawQCDScaleAcceptance = Weight()
ggHRawQCDScaleAcceptance.name = "RawQCDScaleAcceptance_ggH"
ggHRawQCDScaleAcceptance.hasUpDownUncertainties = True
ggHRawQCDScaleAcceptance.CalculateWeight = CalculateRawWeight
ggHRawQCDScaleAcceptance.uncertaintyVariationList = [
    "RawQCDScaleAcceptance_ggHUP",
    "RawQCDScaleAcceptance_ggHDOWN",
]
ggHRawQCDScaleAcceptance.InitUncertaintyVariations()
ggHRawQCDScaleAcceptance.uncertaintyVariationFunctions={
    "RawQCDScaleAcceptance_ggHUP":CalculateRawWeightUP,
    "RawQCDScaleAcceptance_ggHDOWN":CalculateRawWeightDOWN,

}

qqHRawQCDScaleAcceptance = Weight()
qqHRawQCDScaleAcceptance.name = "RawQCDScaleAcceptance_qqH"
qqHRawQCDScaleAcceptance.hasUpDownUncertainties = True
qqHRawQCDScaleAcceptance.CalculateWeight = CalculateRawWeight
qqHRawQCDScaleAcceptance.uncertaintyVariationList = [
    "RawQCDScaleAcceptance_qqHUP",
    "RawQCDScaleAcceptance_qqHDOWN",
]
qqHRawQCDScaleAcceptance.InitUncertaintyVariations()
qqHRawQCDScaleAcceptance.uncertaintyVariationFunctions={
    "RawQCDScaleAcceptance_qqHUP":CalculateRawWeightUP,
    "RawQCDScaleAcceptance_qqHDOWN":CalculateRawWeightDOWN,

}

VHRawQCDScaleAcceptance = Weight()
VHRawQCDScaleAcceptance.name = "RawQCDScaleAcceptance_VH"
VHRawQCDScaleAcceptance.hasUpDownUncertainties = True
VHRawQCDScaleAcceptance.CalculateWeight = CalculateRawWeight
VHRawQCDScaleAcceptance.uncertaintyVariationList = [
    "RawQCDScaleAcceptance_VHUP",
    "RawQCDScaleAcceptance_VHDOWN",
]
VHRawQCDScaleAcceptance.InitUncertaintyVariations()
VHRawQCDScaleAcceptance.uncertaintyVariationFunctions={
    "RawQCDScaleAcceptance_VHUP":CalculateRawWeightUP,
    "RawQCDScaleAcceptance_VHDOWN":CalculateRawWeightDOWN,

}

ggZHRawQCDScaleAcceptance = Weight()
ggZHRawQCDScaleAcceptance.name = "RawQCDScaleAcceptance_ggZH"
ggZHRawQCDScaleAcceptance.hasUpDownUncertainties = True
ggZHRawQCDScaleAcceptance.CalculateWeight = CalculateRawWeight
ggZHRawQCDScaleAcceptance.uncertaintyVariationList = [
    "RawQCDScaleAcceptance_ggZHUP",
    "RawQCDScaleAcceptance_ggZHDOWN",
]
ggZHRawQCDScaleAcceptance.InitUncertaintyVariations()
ggZHRawQCDScaleAcceptance.uncertaintyVariationFunctions={
    "RawQCDScaleAcceptance_ggZHUP":CalculateRawWeightUP,
    "RawQCDScaleAcceptance_ggZHDOWN":CalculateRawWeightDOWN,

}

ttHRawQCDScaleAcceptance = Weight()
ttHRawQCDScaleAcceptance.name = "RawQCDScaleAcceptance_ttH"
ttHRawQCDScaleAcceptance.hasUpDownUncertainties = True
ttHRawQCDScaleAcceptance.CalculateWeight = CalculateRawWeight
ttHRawQCDScaleAcceptance.uncertaintyVariationList = [
    "RawQCDScaleAcceptance_ttHUP",
    "RawQCDScaleAcceptance_ttHDOWN",
]
ttHRawQCDScaleAcceptance.InitUncertaintyVariations()
ttHRawQCDScaleAcceptance.uncertaintyVariationFunctions={
    "RawQCDScaleAcceptance_ttHUP":CalculateRawWeightUP,
    "RawQCDScaleAcceptance_ttHDOWN":CalculateRawWeightDOWN,

}
