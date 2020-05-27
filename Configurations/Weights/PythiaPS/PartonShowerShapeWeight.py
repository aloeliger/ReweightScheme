import ROOT
import math
from Configurations.Weights.WeightDefinition import Weight

def CalculatePSWeight(self,theTree):
    self.value[0] = 1.0

def CalculatePSWeight_UP(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = theTree.PythiaWeight_fsr_muR2*theTree.PythiaWeight_isr_muR2

def CalculatePSWeight_DOWN(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = theTree.PythiaWeight_fsr_muR0p5*theTree.PythiaWeight_isr_muR0p5

partonShowerWeight = Weight()
partonShowerWeight.name = 'PythiaPS'
partonShowerWeight.hasUpDownUncertainties = True
partonShowerWeight.CalculateWeight = CalculatePSWeight
partonShowerWeight.uncertaintyVariationList = [
    "PythiaPS_UP",
    "PythiaPS_DOWN",
]
partonShowerWeight.InitUncertaintyVariations()
partonShowerWeight.uncertaintyVariationFunctions={
    "PythiaPS_UP":CalculatePSWeight_UP,
    "PythiaPS_DOWN":CalculatePSWeight_DOWN,
}
