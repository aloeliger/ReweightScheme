import ROOT
import math
from Configurations.Weights.WeightDefinition import Weight

def CalculateTopPtWeight(self,theTree):
    pttop1 = theTree.pt_top1
    if pttop1 > 400:
        pttop1 = 400
    pttop2 = theTree.pt_top2
    if pttop2 > 400:
        pttop2 = 400
    topfactor = math.sqrt(math.exp(0.0615-0.0005*pttop1)*math.exp(0.0615-0.0005*pttop2))
    self.value[0] = topfactor
    
def CalculateTopPtWeightUp(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = 2.0 * (self.value[0] - 1.0) + 1.0
def CalculateTopPtWeightDown(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = 1.0

topPtWeight = Weight()
topPtWeight.name = 'TopPtWeight'
topPtWeight.hasUpDownUncertainties = True
topPtWeight.CalculateWeight = CalculateTopPtWeight
topPtWeight.uncertaintyVariationList = [
    "TopPt_UP",
    "TopPt_DOWN"
]
topPtWeight.InitUncertaintyVariations()
topPtWeight.uncertaintyVariationFunctions={
    "TopPt_UP": CalculateTopPtWeightUp,
    "TopPt_DOWN": CalculateTopPtWeightDown
    }
