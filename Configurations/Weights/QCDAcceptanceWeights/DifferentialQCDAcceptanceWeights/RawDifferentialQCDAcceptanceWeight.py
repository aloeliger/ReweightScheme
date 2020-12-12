import ROOT
from Configurations.Weights.WeightDefinition import Weight
from Configurations.Weights import localWeightDataPath

def CalculateRawWeight (self,theTree):
    self.value[0] = 1.0

def CalculateDummyUncertainty(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = 1.0

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

dummyggHRawQCDScaleAcceptance = Weight()
dummyggHRawQCDScaleAcceptance.name = "RawQCDScaleAcceptance_ggH"
dummyggHRawQCDScaleAcceptance.hasUpDownUncertainties = True
dummyggHRawQCDScaleAcceptance.CalculateWeight = CalculateRawWeight
dummyggHRawQCDScaleAcceptance.uncertaintyVariationList = [
    "RawQCDScaleAcceptance_ggHUP",
    "RawQCDScaleAcceptance_ggHDOWN",
]
dummyggHRawQCDScaleAcceptance.InitUncertaintyVariations()
dummyggHRawQCDScaleAcceptance.uncertaintyVariationFunctions={
    "RawQCDScaleAcceptance_ggHUP":CalculateDummyUncertainty,
    "RawQCDScaleAcceptance_ggHDOWN":CalculateDummyUncertainty,

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

dummyqqHRawQCDScaleAcceptance = Weight()
dummyqqHRawQCDScaleAcceptance.name = "RawQCDScaleAcceptance_qqH"
dummyqqHRawQCDScaleAcceptance.hasUpDownUncertainties = True
dummyqqHRawQCDScaleAcceptance.CalculateWeight = CalculateRawWeight
dummyqqHRawQCDScaleAcceptance.uncertaintyVariationList = [
    "RawQCDScaleAcceptance_qqHUP",
    "RawQCDScaleAcceptance_qqHDOWN",
]
dummyqqHRawQCDScaleAcceptance.InitUncertaintyVariations()
dummyqqHRawQCDScaleAcceptance.uncertaintyVariationFunctions={
    "RawQCDScaleAcceptance_qqHUP":CalculateDummyUncertainty,
    "RawQCDScaleAcceptance_qqHDOWN":CalculateDummyUncertainty,

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

dummyVHRawQCDScaleAcceptance = Weight()
dummyVHRawQCDScaleAcceptance.name = "RawQCDScaleAcceptance_VH"
dummyVHRawQCDScaleAcceptance.hasUpDownUncertainties = True
dummyVHRawQCDScaleAcceptance.CalculateWeight = CalculateRawWeight
dummyVHRawQCDScaleAcceptance.uncertaintyVariationList = [
    "RawQCDScaleAcceptance_VHUP",
    "RawQCDScaleAcceptance_VHDOWN",
]
dummyVHRawQCDScaleAcceptance.InitUncertaintyVariations()
dummyVHRawQCDScaleAcceptance.uncertaintyVariationFunctions={
    "RawQCDScaleAcceptance_VHUP":CalculateDummyUncertainty,
    "RawQCDScaleAcceptance_VHDOWN":CalculateDummyUncertainty,

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

dummyggZHRawQCDScaleAcceptance = Weight()
dummyggZHRawQCDScaleAcceptance.name = "RawQCDScaleAcceptance_ggZH"
dummyggZHRawQCDScaleAcceptance.hasUpDownUncertainties = True
dummyggZHRawQCDScaleAcceptance.CalculateWeight = CalculateRawWeight
dummyggZHRawQCDScaleAcceptance.uncertaintyVariationList = [
    "RawQCDScaleAcceptance_ggZHUP",
    "RawQCDScaleAcceptance_ggZHDOWN",
]
dummyggZHRawQCDScaleAcceptance.InitUncertaintyVariations()
dummyggZHRawQCDScaleAcceptance.uncertaintyVariationFunctions={
    "RawQCDScaleAcceptance_ggZHUP":CalculateDummyUncertainty,
    "RawQCDScaleAcceptance_ggZHDOWN":CalculateDummyUncertainty,

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

dummyttHRawQCDScaleAcceptance = Weight()
dummyttHRawQCDScaleAcceptance.name = "RawQCDScaleAcceptance_ttH"
dummyttHRawQCDScaleAcceptance.hasUpDownUncertainties = True
dummyttHRawQCDScaleAcceptance.CalculateWeight = CalculateRawWeight
dummyttHRawQCDScaleAcceptance.uncertaintyVariationList = [
    "RawQCDScaleAcceptance_ttHUP",
    "RawQCDScaleAcceptance_ttHDOWN",
]
dummyttHRawQCDScaleAcceptance.InitUncertaintyVariations()
dummyttHRawQCDScaleAcceptance.uncertaintyVariationFunctions={
    "RawQCDScaleAcceptance_ttHUP":CalculateDummyUncertainty,
    "RawQCDScaleAcceptance_ttHDOWN":CalculateDummyUncertainty,

}
