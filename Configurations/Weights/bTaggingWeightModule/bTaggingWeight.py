import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
import bTaggingScaleFactors as scaleFactors

def CalcualtebTaggingWeight(self,theTree):
    #okay, we strictly this is where we enforce the btag veto now.    
    # Our new btagging veto is nbtag <= 0
    # which is w(0|nbtagged at medium)
    # = prod_i=1^max(2) (1-btagging scale factor)_i    
    
    #okay, let's start with the medium weight
    mediumWeight = 0.0
    #three cases. One where nbtag == 0
    if theTree.nbtag == 0:
        mediumWeight = 1.0
    #one where nbtag == 1
    if theTree.nbtag == 1:
        # we need to consider if the first tagged bjet is a valid bjet with pt > 25
        # if not, we need to get the scale factor from whichever is valid
        if theTree.bpt_1 >= 25:
            mediumWeight = (1.0-scaleFactors.GetbTaggingScaleFactor(self.year,1,theTree.bpt_1,theTree.beta_1,theTree.bflavor_1))
        elif theTree.bpt_2 >= 25:
            mediumWeight = (1.0-scaleFactors.GetbTaggingScaleFactor(self.year,1,theTree.bpt_2,theTree.beta_2,theTree.bflavor_2))
        else:
            #just default to zero if we can't find real bjet information
            mediumWeight = 0
    #one where nbtag >= 2
    if theTree.nbtag >= 2:
        #okay, let's just do this in the case where both of our bjets are valid, otherwise we can default to zero
        if theTree.bpt_1 >= 25 and theTree.bpt_2 >= 25:
            mediumWeight = (1.0-scaleFactors.GetbTaggingScaleFactor(self.year,1,theTree.bpt_1,theTree.beta_1,theTree.bflavor_1))*(1.0-scaleFactors.GetbTaggingScaleFactor(self.year,1,theTree.bpt_2,theTree.beta_2,theTree.bflavor_2))
        else:
            mediumWeight = 0
    
    #loose weight has been removed
    
    self.value[0] = mediumWeight#*looseWeight

#this is now old and needs to be replaced.
def OldCalculatebTaggingWeight(self,theTree):
    self.value[0] = theTree.bweight

bTaggingWeight = Weight()
bTaggingWeight.name = 'bTaggingWeight'
bTaggingWeight.CalculateWeight = OldCalculatebTaggingWeight

bTaggingWeight_2016 = Weight()
bTaggingWeight_2016.name = 'bTaggingWeight'
bTaggingWeight_2016.CalculateWeight = CalcualtebTaggingWeight
bTaggingWeight_2016.year = '2016'

bTaggingWeight_2017 = Weight()
bTaggingWeight_2017.name = 'bTaggingWeight'
bTaggingWeight_2017.CalculateWeight = CalcualtebTaggingWeight
bTaggingWeight_2017.year = '2017'

bTaggingWeight_2018 = Weight()
bTaggingWeight_2018.name = 'bTaggingWeight'
bTaggingWeight_2018.CalculateWeight = CalcualtebTaggingWeight
bTaggingWeight_2018.year = '2018'
