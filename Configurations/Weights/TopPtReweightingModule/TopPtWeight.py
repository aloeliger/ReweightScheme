import ROOT
import math
from Configurations.Weights.WeightDefinition import Weight

def CalculateTopPtWeight(self,theTree):
    pttop1 = theTree.pt_top1
    if pttop1 > 472:
        pttop1 = 472
    pttop2 = theTree.pt_top2
    if pttop2 > 472:
        pttop2 = 472
    topfactor = math.sqrt(math.exp(0.088-0.00087*pttop1+0.00000092*pttop1*pttop1)*math.exp(0.088-0.00087*pttop2+0.00000092*pttop1*pttop2))
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
