import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight

def CalculatePrefiringWeighting(self,theTree):
    self.value[0] = theTree.prefiring_weight

PrefiringWeighting = Weight()
PrefiringWeighting.name = 'PrefiringWeighting'
PrefiringWeighting.CalculateWeight = CalculatePrefiringWeighting
