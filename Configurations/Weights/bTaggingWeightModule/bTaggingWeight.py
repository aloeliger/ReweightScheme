import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
import bTaggingScaleFactors as scaleFactors

def CalcualtebTaggingWeight(self,theTree):
    #okay, we strictly this is where we enforce the btag veto now.
    #the veto as written is nbtag <= 0 && nbtagL <= 1
    #okay, let's sit down and sort this out. 
    #I think this splits into two subweights,
    # one dedicated to nbtag <= 0
    # which is w(0|nbtagged at medium)
    # = prod_i=1^max(2) (1-btagging scale factor)_i
    # I think that nbtag considers only medium btags, so we should be good so far
    # okay, now we need to consider the loose portion of this
    # this is w(0|nbtagged at loose) + w(1|nbtagged at loose)
    # = prod_i1^max(2) (1-btagging scale factor)_i + sum_j prod_i!=j (1-sf)_i * sf_j
    #and we have to be a bit careful here to make sure the first jet isn't medium and getting the right
    # factor in the right place.
    
    #okay, let's start with the medium weight
    mediumWeight = 0.0
    #three cases. One where nbtag == 0
    if theTree.nbtag == 0:
        mediumWeight = 1.0
    #one where nbtag == 1
    if theTree.nbtag == 1:
        mediumWeight = (1.0-scaleFactors.GetbTaggingScaleFactor(self.year,1,theTree.bpt_1,theTree.beta_1,theTree.bflavor_1))
    #one where nbtag >= 2
    if theTree.nbtag >= 2:
        mediumWeight = (1.0-scaleFactors.GetbTaggingScaleFactor(self.year,1,theTree.bpt_1,theTree.beta_1,theTree.bflavor_1))*(1.0-scaleFactors.GetbTaggingScaleFactor(self.year,1,theTree.bpt_2,theTree.beta_2,theTree.bflavor_2))
    
    #the loose component is a little more complex
    looseWeight = 0.0
    #there are the same number of base cases as before, but there are sub cases where we have medium jets
    #first case where nbtagL == 0
    #this is the w(0|0)=1 case
    if theTree.nbtagL == 0:
        looseWeight = 1.0
    #this is the w(0|1)+w(1|1) = 1 case.
    if theTree.nbtagL == 1:
        looseWeight = 1.0
    #last case where nbtagL >= 2
    #this is the w(0|2)+w(1|2) case and is non trivial
    #especially with the medium njets
    if theTree.nbtagL >= 2:
        #if there are no nbtagged jets
        #then the first two are our jets
        if theTree.nbtag == 0:
            looseWeight = (1.0-scaleFactors.GetbTaggingScaleFactor(self.year,0,theTree.bpt_1,theTree.beta_1,theTree.bflavor_1))*(1.0-scaleFactors.GetbTaggingScaleFactor(self.year,0,theTree.bpt_2,theTree.beta_2,theTree.bflavor_2))
            looseWeight += (1.0-scaleFactors.GetbTaggingScaleFactor(self.year,0,theTree.bpt_1,theTree.beta_1,theTree.bflavor_1))*scaleFactors.GetbTaggingScaleFactor(self.year,0,theTree.bpt_2,theTree.beta_2,theTree.bflavor_2)
            looseWeight += (1.0-scaleFactors.GetbTaggingScaleFactor(self.year,0,theTree.bpt_2,theTree.beta_2,theTree.bflavor_2))* scaleFactors.GetbTaggingScaleFactor(self.year,0,theTree.bpt_1,theTree.beta_1,theTree.bflavor_1)
        #if there is one nbtaggedjet, then only the second jet has the information we need
        #we can treat any scale factor of the third (second loose jet) as 1
        if theTree.nbtag == 1:
            #this is technically the only term that survives. The second one
            #the first is (1.0-sf_1)*(1.0-1)
            #the last is (1.0-1)*sf_2
            looseWeight = (1.0-scaleFactors.GetbTaggingScaleFactor(self.year,0,theTree.bpt_2,theTree.beta_2,theTree.bflavor_2)) * 1
        if theTree.nbtag >= 2:
            #in this case, just treat the SF as 1?
            #so the whole weight drops out?
            looseWeight = 0
    #print(mediumWeight*looseWeight)
    self.value[0] = mediumWeight*looseWeight

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
