import ROOT
import json
from Configurations.Weights.WeightDefinition import Weight as Weight

def calculateCrossSectionWeight(self, theTree):
    crossSectionWeighting = 1.0
    if self.timePeriod == '2016': #not fond of having the configuration spread out like this
        LHCLumi =  16.81e15
    elif self.timePeriod == '2016APV':
        LHCLumi = 19.52e15
    elif self.timePeriod == '2017':
        LHCLumi = 41.48e15
    elif self.timePeriod == '2018':
        LHCLumi = 59.83e15
    else:
        raise RuntimeError('Found unknown or absent time period for XS weights')
        
    crossSectionWeighting = self.XS * LHCLumi / self.totalNumberOfEvents

    genWeighting = 1.0
    if not self.forcedGenWeight == None:
        genWeighting = self.forcedGenWeight
    else:
        genWeighting = theTree.genWeight
    self.value[0] = crossSectionWeighting * genWeighting
    
    

crossSectionWeight = Weight()
crossSectionWeight.name = 'crossSectionWeighting'
crossSectionWeight.CalculateWeight = calculateCrossSectionWeight
crossSectionWeight.forcedGenWeight = None
