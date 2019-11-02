import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight

def CalculatePrefiringWeighting(self,theTree):
    self.value[0] = theTree.prefiring_weight

def CalculatePrefiringWeightingUp(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = theTree.prefiring_weight_up

def CalculatePrefiringWeightingDown(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = theTree.prefiring_weight_down

PrefiringWeighting = Weight()
PrefiringWeighting.name = 'PrefiringWeighting'
PrefiringWeighting.CalculateWeight = CalculatePrefiringWeighting
PrefiringWeighting.hasUpDownUncertainties = True
PrefiringWeighting.uncertaintyVariationList = [
    "PrefiringWeighting_UP",
    "PrefiringWeighting_DOWN",
]
PrefiringWeighting.InitUncertaintyVariations()
PrefiringWeighting.uncertaintyVariationFunctions = {
    "PrefiringWeighting_UP":CalculatePrefiringWeightingUp,
    "PrefiringWeighting_DOWN":CalculatePrefiringWeightingDown,
}
