import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight

def CalculatebTaggingWeight(self,theTree):
    self.value[0] = theTree.bweight

bTaggingWeight = Weight()
bTaggingWeight.name = 'bTaggingWeight'
bTaggingWeight.CalculateWeight = CalculatebTaggingWeight
