import ROOT
import math
from Configurations.Weights.WeightDefinition import Weight
from Configurations.Weights import localWeightDataPath

def CalculateTopPtWeight(self,theTree):
    pttop1 = theTree.pt_top1
    if pttop1 > 472:
        pttop1 = 472
    pttop2 = theTree.pt_top2
    if pttop2 > 472:
        pttop2 = 472
    topfactor = math.sqrt(math.exp(0.088-0.00087*pttop1+0.00000092*pttop1*pttop1)*math.exp(0.088-0.00087*pttop2+0.00000092*pttop1*pttop2))
    if self.year == '2016':
        correction2016 = (1.0/self.otherCorrection.toppt_ratio_to_2016.Eval(pttop1))*(1.0/self.otherCorrection.toppt_ratio_to_2016.Eval(pttop2))
        topfactor = topfactor * correction2016
    self.value[0] = topfactor
    
def CalculateTopPtWeightUp(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = 2.0 * (self.value[0] - 1.0) + 1.0
def CalculateTopPtWeightDown(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = 1.0

topPtWeight = Weight()
topPtWeight.name = 'TopPtWeight'
topPtWeight.year = 'Other'
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

topPtWeight_2016 = Weight()
topPtWeight_2016.name = 'TopPtWeight'
topPtWeight_2016.year = '2016'
topPtWeight_2016.otherCorrection = ROOT.TFile.Open(localWeightDataPath+"toppt_correction_to_2016.root")
topPtWeight_2016.hasUpDownUncertainties = True
topPtWeight_2016.CalculateWeight = CalculateTopPtWeight
topPtWeight_2016.uncertaintyVariationList = [
    "TopPt_UP",
    "TopPt_DOWN"
]
topPtWeight_2016.InitUncertaintyVariations()
topPtWeight_2016.uncertaintyVariationFunctions={
    "TopPt_UP": CalculateTopPtWeightUp,
    "TopPt_DOWN": CalculateTopPtWeightDown
    }
