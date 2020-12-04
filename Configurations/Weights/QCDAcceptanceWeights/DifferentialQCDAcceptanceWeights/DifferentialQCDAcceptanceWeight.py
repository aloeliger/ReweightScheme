import ROOT
from Configurations.Weights.WeightDefinition import Weight
from Configurations.Weights import localWeightDataPath

def prepUpAndDownConstants(self):
    self.weightHistogram_pth_0_45 = self.reweightFile.Get("h_scale_pth0to45")
    self.weight_pth_0_45_DOWN = self.weightHistogram_pth_0_45.GetBinContent(1)/self.weightHistogram_pth_0_45.GetBinContent(2)
    self.weight_pth_0_45_UP = self.weightHistogram_pth_0_45.GetBinContent(1)/self.weightHistogram_pth_0_45.GetBinContent(3)
    
    self.weightHistogram_pth_45_80 = self.reweightFile.Get("h_scale_pth45to80")
    self.weight_pth_45_80_DOWN = self.weightHistogram_pth_45_80.GetBinContent(1)/self.weightHistogram_pth_45_80.GetBinContent(2)
    self.weight_pth_45_80_UP = self.weightHistogram_pth_45_80.GetBinContent(1)/self.weightHistogram_pth_45_80.GetBinContent(3)

    self.weightHistogram_pth_80_120 = self.reweightFile.Get("h_scale_pth80to120")
    self.weight_pth_80_120_DOWN = self.weightHistogram_pth_80_120.GetBinContent(1)/self.weightHistogram_pth_80_120.GetBinContent(2)
    self.weight_pth_80_120_UP = self.weightHistogram_pth_80_120.GetBinContent(1)/self.weightHistogram_pth_80_120.GetBinContent(3)

    self.weightHistogram_pth_120_200 = self.reweightFile.Get("h_scale_pth120to200")
    self.weight_pth_120_200_DOWN = self.weightHistogram_pth_120_200.GetBinContent(1)/self.weightHistogram_pth_120_200.GetBinContent(2)
    self.weight_pth_120_200_UP = self.weightHistogram_pth_120_200.GetBinContent(1)/self.weightHistogram_pth_120_200.GetBinContent(3)

    self.weightHistogram_pth_200_350 = self.reweightFile.Get("h_scale_pth200to350")
    self.weight_pth_200_350_DOWN = self.weightHistogram_pth_200_350.GetBinContent(1)/self.weightHistogram_pth_200_350.GetBinContent(2)
    self.weight_pth_200_350_UP = self.weightHistogram_pth_200_350.GetBinContent(1)/self.weightHistogram_pth_200_350.GetBinContent(3)

    self.weightHistogram_pth_350_450 = self.reweightFile.Get("h_scale_pth350to450")
    self.weight_pth_350_450_DOWN = self.weightHistogram_pth_350_450.GetBinContent(1)/self.weightHistogram_pth_350_450.GetBinContent(2)
    self.weight_pth_350_450_UP = self.weightHistogram_pth_350_450.GetBinContent(1)/self.weightHistogram_pth_350_450.GetBinContent(3)

    self.weightHistogram_pth_gt450 = self.reweightFile.Get("h_scale_pthgt450")
    self.weight_pth_gt450_DOWN = self.weightHistogram_pth_gt450.GetBinContent(1)/self.weightHistogram_pth_gt450.GetBinContent(2)
    self.weight_pth_gt450_UP = self.weightHistogram_pth_gt450.GetBinContent(1)/self.weightHistogram_pth_gt450.GetBinContent(3)

    self.weightHistogram_njets_0 = self.reweightFile.Get("h_scale_njets0")
    self.weight_njets_0_DOWN = self.weightHistogram_njets_0.GetBinContent(1)/self.weightHistogram_njets_0.GetBinContent(2)
    self.weight_njets_0_UP = self.weightHistogram_njets_0.GetBinContent(1)/self.weightHistogram_njets_0.GetBinContent(3)

    self.weightHistogram_njets_1 = self.reweightFile.Get("h_scale_njets1")
    self.weight_njets_1_DOWN = self.weightHistogram_njets_1.GetBinContent(1)/self.weightHistogram_njets_1.GetBinContent(2)
    self.weight_njets_1_UP = self.weightHistogram_njets_1.GetBinContent(1)/self.weightHistogram_njets_1.GetBinContent(3)

    self.weightHistogram_njets_2 = self.reweightFile.Get("h_scale_njets2")
    self.weight_njets_2_DOWN = self.weightHistogram_njets_2.GetBinContent(1)/self.weightHistogram_njets_2.GetBinContent(2)
    self.weight_njets_2_UP = self.weightHistogram_njets_2.GetBinContent(1)/self.weightHistogram_njets_2.GetBinContent(3)

    self.weightHistogram_njets_3 = self.reweightFile.Get("h_scale_njets3")
    self.weight_njets_3_DOWN = self.weightHistogram_njets_3.GetBinContent(1)/self.weightHistogram_njets_3.GetBinContent(2)
    self.weight_njets_3_UP = self.weightHistogram_njets_3.GetBinContent(1)/self.weightHistogram_njets_3.GetBinContent(3)

    self.weightHistogram_njets_4 = self.reweightFile.Get("h_scale_njets4")
    self.weight_njets_4_DOWN = self.weightHistogram_njets_4.GetBinContent(1)/self.weightHistogram_njets_4.GetBinContent(2)
    self.weight_njets_4_UP = self.weightHistogram_njets_4.GetBinContent(1)/self.weightHistogram_njets_4.GetBinContent(3)

    self.weightHistogram_j1pt_30_60 = self.reweightFile.Get("h_scale_j1pt30to60")
    self.weight_j1pt_30_60_DOWN = self.weightHistogram_j1pt_30_60.GetBinContent(1)/self.weightHistogram_j1pt_30_60.GetBinContent(2)
    self.weight_j1pt_30_60_UP = self.weightHistogram_j1pt_30_60.GetBinContent(1)/self.weightHistogram_j1pt_30_60.GetBinContent(3)

    self.weightHistogram_j1pt_60_120 = self.reweightFile.Get("h_scale_j1pt60to120")
    self.weight_j1pt_60_120_DOWN = self.weightHistogram_j1pt_60_120.GetBinContent(1)/self.weightHistogram_j1pt_60_120.GetBinContent(2)
    self.weight_j1pt_60_120_UP = self.weightHistogram_j1pt_60_120.GetBinContent(1)/self.weightHistogram_j1pt_60_120.GetBinContent(3)

    self.weightHistogram_j1pt_30_60 = self.reweightFile.Get("h_scale_j1pt30to60")
    self.weight_j1pt_30_60_DOWN = self.weightHistogram_j1pt_30_60.GetBinContent(1)/self.weightHistogram_j1pt_30_60.GetBinContent(2)
    self.weight_j1pt_30_60_UP = self.weightHistogram_j1pt_30_60.GetBinContent(1)/self.weightHistogram_j1pt_30_60.GetBinContent(3)

    self.weightHistogram_j1pt60_120 = self.reweightFile.Get("h_scale_j1pt60to120")
    self.weight_j1pt60_120_DOWN = self.weightHistogram_j1pt60_120.GetBinContent(1)/self.weightHistogram_j1pt60_120.GetBinContent(2)
    self.weight_j1pt60_120_UP = self.weightHistogram_j1pt60_120.GetBinContent(1)/self.weightHistogram_j1pt60_120.GetBinContent(3)

    self.weightHistogram_j1pt_120_200 = self.reweightFile.Get("h_scale_j1pt120to200")
    self.weight_j1pt_120_200_DOWN = self.weightHistogram_j1pt_120_200.GetBinContent(1)/self.weightHistogram_j1pt_120_200.GetBinContent(2)
    self.weight_j1pt_120_200_UP = self.weightHistogram_j1pt_120_200.GetBinContent(1)/self.weightHistogram_j1pt_120_200.GetBinContent(3)

    self.weightHistogram_j1pt_200_350 = self.reweightFile.Get("h_scale_j1pt200to350")
    self.weight_j1pt_200_350_DOWN = self.weightHistogram_j1pt_200_350.GetBinContent(1)/self.weightHistogram_j1pt_200_350.GetBinContent(2)
    self.weight_j1pt_200_350_UP = self.weightHistogram_j1pt_200_350.GetBinContent(1)/self.weightHistogram_j1pt_200_350.GetBinContent(3)

    self.weightHistogram_j1pt_gt350 = self.reweightFile.Get("h_scale_j1ptgt350")
    self.weight_j1pt_gt350_DOWN = self.weightHistogram_j1pt_gt350.GetBinContent(1)/self.weightHistogram_j1pt_gt350.GetBinContent(2)
    self.weight_j1pt_gt350_UP = self.weightHistogram_j1pt_gt350.GetBinContent(1)/self.weightHistogram_j1pt_gt350.GetBinContent(3)

def CalculateDifferentialStyleWeight(self,theTree):
    self.value[0] = 1.0

def CalculateDifferentialStyleWeight_pth_0_45_UP(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2 *self.weight_pth_0_45_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_0_45_DOWN(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5 *self.weight_pth_0_45_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_45_80_UP(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2 *self.weight_pth_45_80_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_45_80_DOWN(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5 *self.weight_pth_45_80_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_80_120_UP(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2 *self.weight_pth_80_120_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_80_120_DOWN(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5 *self.weight_pth_80_120_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_120_200_UP(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2 *self.weight_pth_120_200_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_120_200_DOWN(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5 *self.weight_pth_120_200_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_200_350_UP(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2 *self.weight_pth_200_350_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_200_350_DOWN(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5 *self.weight_pth_200_350_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_350_450_UP(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2 *self.weight_pth_350_450_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_350_450_DOWN(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5 *self.weight_pth_350_450_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_gt450_UP(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2 *self.weight_pth_gt450_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_pth_gt450_DOWN(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5 *self.weight_pth_gt450_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_njets_0_UP(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.weight_njets_0_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_njets_0_DOWN(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.weight_njets_0_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_njets_1_UP(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.weight_njets_1_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_njets_1_DOWN(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.weight_njets_1_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_njets_2_UP(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.weight_njets_2_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_njets_2_DOWN(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.weight_njets_2_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_njets_3_UP(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.weight_njets_3_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_njets_3_DOWN(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.weight_njets_3_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_njets_GE4_UP(self,theTree,uncert):
    if (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.weight_njets_4_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_njets_GE4_DOWN(self,theTree,uncert):
    if (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.weight_njets_4_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_j1pt_30_60_UP(self,theTree,uncert):
    if(theTree.Rivet_nJets30 >= 1 and theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.weight_j1pt_30_60_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_j1pt_30_60_DOWN(self,theTree,uncert):
    if(theTree.Rivet_nJets30 >= 1 and theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.weight_j1pt_30_60_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_j1pt_60_120_UP(self,theTree,uncert):
    if(theTree.Rivet_nJets30 >= 1 and theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.weight_j1pt_60_120_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_j1pt_60_120_DOWN(self,theTree,uncert):
    if(theTree.Rivet_nJets30 >= 1 and theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.weight_j1pt_60_120_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_j1pt_120_200_UP(self,theTree,uncert):
    if(theTree.Rivet_nJets30 >= 1 and theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.weight_j1pt_120_200_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_j1pt_120_200_DOWN(self,theTree,uncert):
    if(theTree.Rivet_nJets30 >= 1 and theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.weight_j1pt_120_200_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_j1pt_200_350_UP(self,theTree,uncert):
    if(theTree.Rivet_nJets30 >= 1 and theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.weight_j1pt_200_350_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_j1pt_200_350_DOWN(self,theTree,uncert):
    if(theTree.Rivet_nJets30 >= 1 and theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.weight_j1pt_200_350_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_j1pt_gt350_UP(self,theTree,uncert):
    if(theTree.Rivet_nJets30 >= 1 and theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.weight_j1pt_gt350_UP
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateDifferentialStyleWeight_j1pt_gt350_DOWN(self,theTree,uncert):
    if(theTree.Rivet_nJets30 >= 1 and theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.weight_j1pt_gt350_DOWN
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

ggHStyleWeight_Differential = Weight()
ggHStyleWeight_Differential.name = 'QCDScaleAcceptance_Differential_ggH'
ggHStyleWeight_Differential.reweightFile = ROOT.TFile(localWeightDataPath+'/theory_uncertainties_differential/ggH_htt125.root')
ggHStyleWeight_Differential.hasUpDownUncertainties = True
ggHStyleWeight_Differential.CalculateWeight = CalculateDifferentialStyleWeight
ggHStyleWeight_Differential.uncertaintyVariationList = [
    'QCDScaleAcceptance_Differential_ggH_pth_0_45UP',
    'QCDScaleAcceptance_Differential_ggH_pth_0_45DOWN',
    'QCDScaleAcceptance_Differential_ggH_pth_45_80UP',
    'QCDScaleAcceptance_Differential_ggH_pth_45_80DOWN',
    'QCDScaleAcceptance_Differential_ggH_pth_80_120UP',
    'QCDScaleAcceptance_Differential_ggH_pth_80_120DOWN',
    'QCDScaleAcceptance_Differential_ggH_pth_120_200UP',
    'QCDScaleAcceptance_Differential_ggH_pth_120_200DOWN',
    'QCDScaleAcceptance_Differential_ggH_pth_200_350UP',
    'QCDScaleAcceptance_Differential_ggH_pth_200_350DOWN',
    'QCDScaleAcceptance_Differential_ggH_pth_350_450UP',
    'QCDScaleAcceptance_Differential_ggH_pth_350_450DOWN',
    'QCDScaleAcceptance_Differential_ggH_pth_gt450UP',
    'QCDScaleAcceptance_Differential_ggH_pth_gt450DOWN',
    'QCDScaleAcceptance_Differential_ggH_njets0UP',
    'QCDScaleAcceptance_Differential_ggH_njets0DOWN',
    'QCDScaleAcceptance_Differential_ggH_njets1UP',
    'QCDScaleAcceptance_Differential_ggH_njets1DOWN',
    'QCDScaleAcceptance_Differential_ggH_njets2UP',
    'QCDScaleAcceptance_Differential_ggH_njets2DOWN',
    'QCDScaleAcceptance_Differential_ggH_njets3UP',
    'QCDScaleAcceptance_Differential_ggH_njets3DOWN',
    'QCDScaleAcceptance_Differential_ggH_njets4UP',
    'QCDScaleAcceptance_Differential_ggH_njets4DOWN',
    'QCDScaleAcceptance_Differential_ggH_j1pt_30_60UP',
    'QCDScaleAcceptance_Differential_ggH_j1pt_30_60DOWN',
    'QCDScaleAcceptance_Differential_ggH_j1pt_60_120UP',
    'QCDScaleAcceptance_Differential_ggH_j1pt_60_120DOWN',
    'QCDScaleAcceptance_Differential_ggH_j1pt_120_200UP',
    'QCDScaleAcceptance_Differential_ggH_j1pt_120_200DOWN',
    'QCDScaleAcceptance_Differential_ggH_j1pt_200_350UP',
    'QCDScaleAcceptance_Differential_ggH_j1pt_200_350DOWN',
    'QCDScaleAcceptance_Differential_ggH_j1pt_gt350UP',
    'QCDScaleAcceptance_Differential_ggH_j1pt_gt350DOWN',
]
ggHStyleWeight_Differential.InitUncertaintyVariations()
ggHStyleWeight_Differential.uncertaintyVariationFunctions={
    'QCDScaleAcceptance_Differential_ggH_pth_0_45UP':CalculateDifferentialStyleWeight_pth_0_45_UP,
    'QCDScaleAcceptance_Differential_ggH_pth_0_45DOWN':CalculateDifferentialStyleWeight_pth_0_45_DOWN,
    'QCDScaleAcceptance_Differential_ggH_pth_45_80UP':CalculateDifferentialStyleWeight_pth_45_80_UP,
    'QCDScaleAcceptance_Differential_ggH_pth_45_80DOWN':CalculateDifferentialStyleWeight_pth_45_80_DOWN,
    'QCDScaleAcceptance_Differential_ggH_pth_80_120UP':CalculateDifferentialStyleWeight_pth_80_120_UP,
    'QCDScaleAcceptance_Differential_ggH_pth_80_120DOWN':CalculateDifferentialStyleWeight_pth_80_120_DOWN,
    'QCDScaleAcceptance_Differential_ggH_pth_120_200UP':CalculateDifferentialStyleWeight_pth_120_200_UP,
    'QCDScaleAcceptance_Differential_ggH_pth_120_200DOWN':CalculateDifferentialStyleWeight_pth_120_200_DOWN,
    'QCDScaleAcceptance_Differential_ggH_pth_200_350UP':CalculateDifferentialStyleWeight_pth_200_350_UP,
    'QCDScaleAcceptance_Differential_ggH_pth_200_350DOWN':CalculateDifferentialStyleWeight_pth_200_350_DOWN,
    'QCDScaleAcceptance_Differential_ggH_pth_350_450UP':CalculateDifferentialStyleWeight_pth_350_450_UP,
    'QCDScaleAcceptance_Differential_ggH_pth_350_450DOWN':CalculateDifferentialStyleWeight_pth_350_450_DOWN,
    'QCDScaleAcceptance_Differential_ggH_pth_gt450UP':CalculateDifferentialStyleWeight_pth_gt450_UP,
    'QCDScaleAcceptance_Differential_ggH_pth_gt450DOWN':CalculateDifferentialStyleWeight_pth_gt450_DOWN,
    'QCDScaleAcceptance_Differential_ggH_njets0UP':CalculateDifferentialStyleWeight_njets_0_UP,
    'QCDScaleAcceptance_Differential_ggH_njets0DOWN':CalculateDifferentialStyleWeight_njets_0_DOWN,
    'QCDScaleAcceptance_Differential_ggH_njets1UP':CalculateDifferentialStyleWeight_njets_1_UP,
    'QCDScaleAcceptance_Differential_ggH_njets1DOWN':CalculateDifferentialStyleWeight_njets_1_DOWN,
    'QCDScaleAcceptance_Differential_ggH_njets2UP':CalculateDifferentialStyleWeight_njets_2_UP,
    'QCDScaleAcceptance_Differential_ggH_njets2DOWN':CalculateDifferentialStyleWeight_njets_2_DOWN,
    'QCDScaleAcceptance_Differential_ggH_njets3UP':CalculateDifferentialStyleWeight_njets_3_UP,
    'QCDScaleAcceptance_Differential_ggH_njets3DOWN':CalculateDifferentialStyleWeight_njets_3_DOWN,
    'QCDScaleAcceptance_Differential_ggH_njets4UP':CalculateDifferentialStyleWeight_njets_GE4_UP,
    'QCDScaleAcceptance_Differential_ggH_njets4DOWN':CalculateDifferentialStyleWeight_njets_GE4_DOWN,
    'QCDScaleAcceptance_Differential_ggH_j1pt_30_60UP':CalculateDifferentialStyleWeight_j1pt_30_60_UP,
    'QCDScaleAcceptance_Differential_ggH_j1pt_30_60DOWN':CalculateDifferentialStyleWeight_j1pt_30_60_DOWN,
    'QCDScaleAcceptance_Differential_ggH_j1pt_60_120UP':CalculateDifferentialStyleWeight_j1pt_60_120_UP,
    'QCDScaleAcceptance_Differential_ggH_j1pt_60_120DOWN':CalculateDifferentialStyleWeight_j1pt_60_120_DOWN,
    'QCDScaleAcceptance_Differential_ggH_j1pt_120_200UP':CalculateDifferentialStyleWeight_j1pt_120_200_UP,
    'QCDScaleAcceptance_Differential_ggH_j1pt_120_200DOWN':CalculateDifferentialStyleWeight_j1pt_120_200_DOWN,
    'QCDScaleAcceptance_Differential_ggH_j1pt_200_350UP':CalculateDifferentialStyleWeight_j1pt_200_350_UP,
    'QCDScaleAcceptance_Differential_ggH_j1pt_200_350DOWN':CalculateDifferentialStyleWeight_j1pt_200_350_DOWN,
    'QCDScaleAcceptance_Differential_ggH_j1pt_gt350UP':CalculateDifferentialStyleWeight_j1pt_gt350_UP,
    'QCDScaleAcceptance_Differential_ggH_j1pt_gt350DOWN':CalculateDifferentialStyleWeight_j1pt_gt350_DOWN,
}
ggHStyleWeight_Differential.prepUpAndDownConstants = prepUpAndDownConstants
ggHStyleWeight_Differential.prepUpAndDownConstants(ggHStyleWeight_Differential)

qqHStyleWeight_Differential = Weight()
qqHStyleWeight_Differential.name = 'QCDScaleAcceptance_Differential_qqH'
qqHStyleWeight_Differential.reweightFile = ROOT.TFile(localWeightDataPath+'/theory_uncertainties_differential/qqH_htt125.root')
qqHStyleWeight_Differential.hasUpDownUncertainties = True
qqHStyleWeight_Differential.CalculateWeight = CalculateDifferentialStyleWeight
qqHStyleWeight_Differential.uncertaintyVariationList = [
    'QCDScaleAcceptance_Differential_qqH_pth_0_45UP',
    'QCDScaleAcceptance_Differential_qqH_pth_0_45DOWN',
    'QCDScaleAcceptance_Differential_qqH_pth_45_80UP',
    'QCDScaleAcceptance_Differential_qqH_pth_45_80DOWN',
    'QCDScaleAcceptance_Differential_qqH_pth_80_120UP',
    'QCDScaleAcceptance_Differential_qqH_pth_80_120DOWN',
    'QCDScaleAcceptance_Differential_qqH_pth_120_200UP',
    'QCDScaleAcceptance_Differential_qqH_pth_120_200DOWN',
    'QCDScaleAcceptance_Differential_qqH_pth_200_350UP',
    'QCDScaleAcceptance_Differential_qqH_pth_200_350DOWN',
    'QCDScaleAcceptance_Differential_qqH_pth_350_450UP',
    'QCDScaleAcceptance_Differential_qqH_pth_350_450DOWN',
    'QCDScaleAcceptance_Differential_qqH_pth_gt450UP',
    'QCDScaleAcceptance_Differential_qqH_pth_gt450DOWN',
    'QCDScaleAcceptance_Differential_qqH_njets0UP',
    'QCDScaleAcceptance_Differential_qqH_njets0DOWN',
    'QCDScaleAcceptance_Differential_qqH_njets1UP',
    'QCDScaleAcceptance_Differential_qqH_njets1DOWN',
    'QCDScaleAcceptance_Differential_qqH_njets2UP',
    'QCDScaleAcceptance_Differential_qqH_njets2DOWN',
    'QCDScaleAcceptance_Differential_qqH_njets3UP',
    'QCDScaleAcceptance_Differential_qqH_njets3DOWN',
    'QCDScaleAcceptance_Differential_qqH_njets4UP',
    'QCDScaleAcceptance_Differential_qqH_njets4DOWN',
    'QCDScaleAcceptance_Differential_qqH_j1pt_30_60UP',
    'QCDScaleAcceptance_Differential_qqH_j1pt_30_60DOWN',
    'QCDScaleAcceptance_Differential_qqH_j1pt_60_120UP',
    'QCDScaleAcceptance_Differential_qqH_j1pt_60_120DOWN',
    'QCDScaleAcceptance_Differential_qqH_j1pt_120_200UP',
    'QCDScaleAcceptance_Differential_qqH_j1pt_120_200DOWN',
    'QCDScaleAcceptance_Differential_qqH_j1pt_200_350UP',
    'QCDScaleAcceptance_Differential_qqH_j1pt_200_350DOWN',
    'QCDScaleAcceptance_Differential_qqH_j1pt_gt350UP',
    'QCDScaleAcceptance_Differential_qqH_j1pt_gt350DOWN',
]
qqHStyleWeight_Differential.InitUncertaintyVariations()
qqHStyleWeight_Differential.uncertaintyVariationFunctions={
    'QCDScaleAcceptance_Differential_qqH_pth_0_45UP':CalculateDifferentialStyleWeight_pth_0_45_UP,
    'QCDScaleAcceptance_Differential_qqH_pth_0_45DOWN':CalculateDifferentialStyleWeight_pth_0_45_DOWN,
    'QCDScaleAcceptance_Differential_qqH_pth_45_80UP':CalculateDifferentialStyleWeight_pth_45_80_UP,
    'QCDScaleAcceptance_Differential_qqH_pth_45_80DOWN':CalculateDifferentialStyleWeight_pth_45_80_DOWN,
    'QCDScaleAcceptance_Differential_qqH_pth_80_120UP':CalculateDifferentialStyleWeight_pth_80_120_UP,
    'QCDScaleAcceptance_Differential_qqH_pth_80_120DOWN':CalculateDifferentialStyleWeight_pth_80_120_DOWN,
    'QCDScaleAcceptance_Differential_qqH_pth_120_200UP':CalculateDifferentialStyleWeight_pth_120_200_UP,
    'QCDScaleAcceptance_Differential_qqH_pth_120_200DOWN':CalculateDifferentialStyleWeight_pth_120_200_DOWN,
    'QCDScaleAcceptance_Differential_qqH_pth_200_350UP':CalculateDifferentialStyleWeight_pth_200_350_UP,
    'QCDScaleAcceptance_Differential_qqH_pth_200_350DOWN':CalculateDifferentialStyleWeight_pth_200_350_DOWN,
    'QCDScaleAcceptance_Differential_qqH_pth_350_450UP':CalculateDifferentialStyleWeight_pth_350_450_UP,
    'QCDScaleAcceptance_Differential_qqH_pth_350_450DOWN':CalculateDifferentialStyleWeight_pth_350_450_DOWN,
    'QCDScaleAcceptance_Differential_qqH_pth_gt450UP':CalculateDifferentialStyleWeight_pth_gt450_UP,
    'QCDScaleAcceptance_Differential_qqH_pth_gt450DOWN':CalculateDifferentialStyleWeight_pth_gt450_DOWN,
    'QCDScaleAcceptance_Differential_qqH_njets0UP':CalculateDifferentialStyleWeight_njets_0_UP,
    'QCDScaleAcceptance_Differential_qqH_njets0DOWN':CalculateDifferentialStyleWeight_njets_0_DOWN,
    'QCDScaleAcceptance_Differential_qqH_njets1UP':CalculateDifferentialStyleWeight_njets_1_UP,
    'QCDScaleAcceptance_Differential_qqH_njets1DOWN':CalculateDifferentialStyleWeight_njets_1_DOWN,
    'QCDScaleAcceptance_Differential_qqH_njets2UP':CalculateDifferentialStyleWeight_njets_2_UP,
    'QCDScaleAcceptance_Differential_qqH_njets2DOWN':CalculateDifferentialStyleWeight_njets_2_DOWN,
    'QCDScaleAcceptance_Differential_qqH_njets3UP':CalculateDifferentialStyleWeight_njets_3_UP,
    'QCDScaleAcceptance_Differential_qqH_njets3DOWN':CalculateDifferentialStyleWeight_njets_3_DOWN,
    'QCDScaleAcceptance_Differential_qqH_njets4UP':CalculateDifferentialStyleWeight_njets_GE4_UP,
    'QCDScaleAcceptance_Differential_qqH_njets4DOWN':CalculateDifferentialStyleWeight_njets_GE4_DOWN,
    'QCDScaleAcceptance_Differential_qqH_j1pt_30_60UP':CalculateDifferentialStyleWeight_j1pt_30_60_UP,
    'QCDScaleAcceptance_Differential_qqH_j1pt_30_60DOWN':CalculateDifferentialStyleWeight_j1pt_30_60_DOWN,
    'QCDScaleAcceptance_Differential_qqH_j1pt_60_120UP':CalculateDifferentialStyleWeight_j1pt_60_120_UP,
    'QCDScaleAcceptance_Differential_qqH_j1pt_60_120DOWN':CalculateDifferentialStyleWeight_j1pt_60_120_DOWN,
    'QCDScaleAcceptance_Differential_qqH_j1pt_120_200UP':CalculateDifferentialStyleWeight_j1pt_120_200_UP,
    'QCDScaleAcceptance_Differential_qqH_j1pt_120_200DOWN':CalculateDifferentialStyleWeight_j1pt_120_200_DOWN,
    'QCDScaleAcceptance_Differential_qqH_j1pt_200_350UP':CalculateDifferentialStyleWeight_j1pt_200_350_UP,
    'QCDScaleAcceptance_Differential_qqH_j1pt_200_350DOWN':CalculateDifferentialStyleWeight_j1pt_200_350_DOWN,
    'QCDScaleAcceptance_Differential_qqH_j1pt_gt350UP':CalculateDifferentialStyleWeight_j1pt_gt350_UP,
    'QCDScaleAcceptance_Differential_qqH_j1pt_gt350DOWN':CalculateDifferentialStyleWeight_j1pt_gt350_DOWN,
}
qqHStyleWeight_Differential.prepUpAndDownConstants = prepUpAndDownConstants
qqHStyleWeight_Differential.prepUpAndDownConstants(qqHStyleWeight_Differential)

WminusHStyleWeight_Differential = Weight()
WminusHStyleWeight_Differential.name = 'QCDScaleAcceptance_Differential_WminusH'
WminusHStyleWeight_Differential.reweightFile = ROOT.TFile(localWeightDataPath+'/theory_uncertainties_differential/WminusH125.root')
WminusHStyleWeight_Differential.hasUpDownUncertainties = True
WminusHStyleWeight_Differential.CalculateWeight = CalculateDifferentialStyleWeight
WminusHStyleWeight_Differential.uncertaintyVariationList = [
    'QCDScaleAcceptance_Differential_WminusH_pth_0_45UP',
    'QCDScaleAcceptance_Differential_WminusH_pth_0_45DOWN',
    'QCDScaleAcceptance_Differential_WminusH_pth_45_80UP',
    'QCDScaleAcceptance_Differential_WminusH_pth_45_80DOWN',
    'QCDScaleAcceptance_Differential_WminusH_pth_80_120UP',
    'QCDScaleAcceptance_Differential_WminusH_pth_80_120DOWN',
    'QCDScaleAcceptance_Differential_WminusH_pth_120_200UP',
    'QCDScaleAcceptance_Differential_WminusH_pth_120_200DOWN',
    'QCDScaleAcceptance_Differential_WminusH_pth_200_350UP',
    'QCDScaleAcceptance_Differential_WminusH_pth_200_350DOWN',
    'QCDScaleAcceptance_Differential_WminusH_pth_350_450UP',
    'QCDScaleAcceptance_Differential_WminusH_pth_350_450DOWN',
    'QCDScaleAcceptance_Differential_WminusH_pth_gt450UP',
    'QCDScaleAcceptance_Differential_WminusH_pth_gt450DOWN',
    'QCDScaleAcceptance_Differential_WminusH_njets0UP',
    'QCDScaleAcceptance_Differential_WminusH_njets0DOWN',
    'QCDScaleAcceptance_Differential_WminusH_njets1UP',
    'QCDScaleAcceptance_Differential_WminusH_njets1DOWN',
    'QCDScaleAcceptance_Differential_WminusH_njets2UP',
    'QCDScaleAcceptance_Differential_WminusH_njets2DOWN',
    'QCDScaleAcceptance_Differential_WminusH_njets3UP',
    'QCDScaleAcceptance_Differential_WminusH_njets3DOWN',
    'QCDScaleAcceptance_Differential_WminusH_njets4UP',
    'QCDScaleAcceptance_Differential_WminusH_njets4DOWN',
    'QCDScaleAcceptance_Differential_WminusH_j1pt_30_60UP',
    'QCDScaleAcceptance_Differential_WminusH_j1pt_30_60DOWN',
    'QCDScaleAcceptance_Differential_WminusH_j1pt_60_120UP',
    'QCDScaleAcceptance_Differential_WminusH_j1pt_60_120DOWN',
    'QCDScaleAcceptance_Differential_WminusH_j1pt_120_200UP',
    'QCDScaleAcceptance_Differential_WminusH_j1pt_120_200DOWN',
    'QCDScaleAcceptance_Differential_WminusH_j1pt_200_350UP',
    'QCDScaleAcceptance_Differential_WminusH_j1pt_200_350DOWN',
    'QCDScaleAcceptance_Differential_WminusH_j1pt_gt350UP',
    'QCDScaleAcceptance_Differential_WminusH_j1pt_gt350DOWN',
]
WminusHStyleWeight_Differential.InitUncertaintyVariations()
WminusHStyleWeight_Differential.uncertaintyVariationFunctions={
    'QCDScaleAcceptance_Differential_WminusH_pth_0_45UP':CalculateDifferentialStyleWeight_pth_0_45_UP,
    'QCDScaleAcceptance_Differential_WminusH_pth_0_45DOWN':CalculateDifferentialStyleWeight_pth_0_45_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_pth_45_80UP':CalculateDifferentialStyleWeight_pth_45_80_UP,
    'QCDScaleAcceptance_Differential_WminusH_pth_45_80DOWN':CalculateDifferentialStyleWeight_pth_45_80_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_pth_80_120UP':CalculateDifferentialStyleWeight_pth_80_120_UP,
    'QCDScaleAcceptance_Differential_WminusH_pth_80_120DOWN':CalculateDifferentialStyleWeight_pth_80_120_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_pth_120_200UP':CalculateDifferentialStyleWeight_pth_120_200_UP,
    'QCDScaleAcceptance_Differential_WminusH_pth_120_200DOWN':CalculateDifferentialStyleWeight_pth_120_200_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_pth_200_350UP':CalculateDifferentialStyleWeight_pth_200_350_UP,
    'QCDScaleAcceptance_Differential_WminusH_pth_200_350DOWN':CalculateDifferentialStyleWeight_pth_200_350_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_pth_350_450UP':CalculateDifferentialStyleWeight_pth_350_450_UP,
    'QCDScaleAcceptance_Differential_WminusH_pth_350_450DOWN':CalculateDifferentialStyleWeight_pth_350_450_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_pth_gt450UP':CalculateDifferentialStyleWeight_pth_gt450_UP,
    'QCDScaleAcceptance_Differential_WminusH_pth_gt450DOWN':CalculateDifferentialStyleWeight_pth_gt450_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_njets0UP':CalculateDifferentialStyleWeight_njets_0_UP,
    'QCDScaleAcceptance_Differential_WminusH_njets0DOWN':CalculateDifferentialStyleWeight_njets_0_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_njets1UP':CalculateDifferentialStyleWeight_njets_1_UP,
    'QCDScaleAcceptance_Differential_WminusH_njets1DOWN':CalculateDifferentialStyleWeight_njets_1_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_njets2UP':CalculateDifferentialStyleWeight_njets_2_UP,
    'QCDScaleAcceptance_Differential_WminusH_njets2DOWN':CalculateDifferentialStyleWeight_njets_2_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_njets3UP':CalculateDifferentialStyleWeight_njets_3_UP,
    'QCDScaleAcceptance_Differential_WminusH_njets3DOWN':CalculateDifferentialStyleWeight_njets_3_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_njets4UP':CalculateDifferentialStyleWeight_njets_GE4_UP,
    'QCDScaleAcceptance_Differential_WminusH_njets4DOWN':CalculateDifferentialStyleWeight_njets_GE4_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_j1pt_30_60UP':CalculateDifferentialStyleWeight_j1pt_30_60_UP,
    'QCDScaleAcceptance_Differential_WminusH_j1pt_30_60DOWN':CalculateDifferentialStyleWeight_j1pt_30_60_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_j1pt_60_120UP':CalculateDifferentialStyleWeight_j1pt_60_120_UP,
    'QCDScaleAcceptance_Differential_WminusH_j1pt_60_120DOWN':CalculateDifferentialStyleWeight_j1pt_60_120_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_j1pt_120_200UP':CalculateDifferentialStyleWeight_j1pt_120_200_UP,
    'QCDScaleAcceptance_Differential_WminusH_j1pt_120_200DOWN':CalculateDifferentialStyleWeight_j1pt_120_200_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_j1pt_200_350UP':CalculateDifferentialStyleWeight_j1pt_200_350_UP,
    'QCDScaleAcceptance_Differential_WminusH_j1pt_200_350DOWN':CalculateDifferentialStyleWeight_j1pt_200_350_DOWN,
    'QCDScaleAcceptance_Differential_WminusH_j1pt_gt350UP':CalculateDifferentialStyleWeight_j1pt_gt350_UP,
    'QCDScaleAcceptance_Differential_WminusH_j1pt_gt350DOWN':CalculateDifferentialStyleWeight_j1pt_gt350_DOWN,
}
WminusHStyleWeight_Differential.prepUpAndDownConstants = prepUpAndDownConstants
WminusHStyleWeight_Differential.prepUpAndDownConstants(WminusHStyleWeight_Differential)

WplusHStyleWeight_Differential = Weight()
WplusHStyleWeight_Differential.name = 'QCDScaleAcceptance_Differential_WplusH'
WplusHStyleWeight_Differential.reweightFile = ROOT.TFile(localWeightDataPath+'/theory_uncertainties_differential/Wplus125.root')
WplusHStyleWeight_Differential.hasUpDownUncertainties = True
WplusHStyleWeight_Differential.CalculateWeight = CalculateDifferentialStyleWeight
WplusHStyleWeight_Differential.uncertaintyVariationList = [
    'QCDScaleAcceptance_Differential_WplusH_pth_0_45UP',
    'QCDScaleAcceptance_Differential_WplusH_pth_0_45DOWN',
    'QCDScaleAcceptance_Differential_WplusH_pth_45_80UP',
    'QCDScaleAcceptance_Differential_WplusH_pth_45_80DOWN',
    'QCDScaleAcceptance_Differential_WplusH_pth_80_120UP',
    'QCDScaleAcceptance_Differential_WplusH_pth_80_120DOWN',
    'QCDScaleAcceptance_Differential_WplusH_pth_120_200UP',
    'QCDScaleAcceptance_Differential_WplusH_pth_120_200DOWN',
    'QCDScaleAcceptance_Differential_WplusH_pth_200_350UP',
    'QCDScaleAcceptance_Differential_WplusH_pth_200_350DOWN',
    'QCDScaleAcceptance_Differential_WplusH_pth_350_450UP',
    'QCDScaleAcceptance_Differential_WplusH_pth_350_450DOWN',
    'QCDScaleAcceptance_Differential_WplusH_pth_gt450UP',
    'QCDScaleAcceptance_Differential_WplusH_pth_gt450DOWN',
    'QCDScaleAcceptance_Differential_WplusH_njets0UP',
    'QCDScaleAcceptance_Differential_WplusH_njets0DOWN',
    'QCDScaleAcceptance_Differential_WplusH_njets1UP',
    'QCDScaleAcceptance_Differential_WplusH_njets1DOWN',
    'QCDScaleAcceptance_Differential_WplusH_njets2UP',
    'QCDScaleAcceptance_Differential_WplusH_njets2DOWN',
    'QCDScaleAcceptance_Differential_WplusH_njets3UP',
    'QCDScaleAcceptance_Differential_WplusH_njets3DOWN',
    'QCDScaleAcceptance_Differential_WplusH_njets4UP',
    'QCDScaleAcceptance_Differential_WplusH_njets4DOWN',
    'QCDScaleAcceptance_Differential_WplusH_j1pt_30_60UP',
    'QCDScaleAcceptance_Differential_WplusH_j1pt_30_60DOWN',
    'QCDScaleAcceptance_Differential_WplusH_j1pt_60_120UP',
    'QCDScaleAcceptance_Differential_WplusH_j1pt_60_120DOWN',
    'QCDScaleAcceptance_Differential_WplusH_j1pt_120_200UP',
    'QCDScaleAcceptance_Differential_WplusH_j1pt_120_200DOWN',
    'QCDScaleAcceptance_Differential_WplusH_j1pt_200_350UP',
    'QCDScaleAcceptance_Differential_WplusH_j1pt_200_350DOWN',
    'QCDScaleAcceptance_Differential_WplusH_j1pt_gt350UP',
    'QCDScaleAcceptance_Differential_WplusH_j1pt_gt350DOWN',
]
WplusHStyleWeight_Differential.InitUncertaintyVariations()
WplusHStyleWeight_Differential.uncertaintyVariationFunctions={
    'QCDScaleAcceptance_Differential_WplusH_pth_0_45UP':CalculateDifferentialStyleWeight_pth_0_45_UP,
    'QCDScaleAcceptance_Differential_WplusH_pth_0_45DOWN':CalculateDifferentialStyleWeight_pth_0_45_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_pth_45_80UP':CalculateDifferentialStyleWeight_pth_45_80_UP,
    'QCDScaleAcceptance_Differential_WplusH_pth_45_80DOWN':CalculateDifferentialStyleWeight_pth_45_80_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_pth_80_120UP':CalculateDifferentialStyleWeight_pth_80_120_UP,
    'QCDScaleAcceptance_Differential_WplusH_pth_80_120DOWN':CalculateDifferentialStyleWeight_pth_80_120_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_pth_120_200UP':CalculateDifferentialStyleWeight_pth_120_200_UP,
    'QCDScaleAcceptance_Differential_WplusH_pth_120_200DOWN':CalculateDifferentialStyleWeight_pth_120_200_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_pth_200_350UP':CalculateDifferentialStyleWeight_pth_200_350_UP,
    'QCDScaleAcceptance_Differential_WplusH_pth_200_350DOWN':CalculateDifferentialStyleWeight_pth_200_350_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_pth_350_450UP':CalculateDifferentialStyleWeight_pth_350_450_UP,
    'QCDScaleAcceptance_Differential_WplusH_pth_350_450DOWN':CalculateDifferentialStyleWeight_pth_350_450_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_pth_gt450UP':CalculateDifferentialStyleWeight_pth_gt450_UP,
    'QCDScaleAcceptance_Differential_WplusH_pth_gt450DOWN':CalculateDifferentialStyleWeight_pth_gt450_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_njets0UP':CalculateDifferentialStyleWeight_njets_0_UP,
    'QCDScaleAcceptance_Differential_WplusH_njets0DOWN':CalculateDifferentialStyleWeight_njets_0_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_njets1UP':CalculateDifferentialStyleWeight_njets_1_UP,
    'QCDScaleAcceptance_Differential_WplusH_njets1DOWN':CalculateDifferentialStyleWeight_njets_1_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_njets2UP':CalculateDifferentialStyleWeight_njets_2_UP,
    'QCDScaleAcceptance_Differential_WplusH_njets2DOWN':CalculateDifferentialStyleWeight_njets_2_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_njets3UP':CalculateDifferentialStyleWeight_njets_3_UP,
    'QCDScaleAcceptance_Differential_WplusH_njets3DOWN':CalculateDifferentialStyleWeight_njets_3_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_njets4UP':CalculateDifferentialStyleWeight_njets_GE4_UP,
    'QCDScaleAcceptance_Differential_WplusH_njets4DOWN':CalculateDifferentialStyleWeight_njets_GE4_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_j1pt_30_60UP':CalculateDifferentialStyleWeight_j1pt_30_60_UP,
    'QCDScaleAcceptance_Differential_WplusH_j1pt_30_60DOWN':CalculateDifferentialStyleWeight_j1pt_30_60_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_j1pt_60_120UP':CalculateDifferentialStyleWeight_j1pt_60_120_UP,
    'QCDScaleAcceptance_Differential_WplusH_j1pt_60_120DOWN':CalculateDifferentialStyleWeight_j1pt_60_120_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_j1pt_120_200UP':CalculateDifferentialStyleWeight_j1pt_120_200_UP,
    'QCDScaleAcceptance_Differential_WplusH_j1pt_120_200DOWN':CalculateDifferentialStyleWeight_j1pt_120_200_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_j1pt_200_350UP':CalculateDifferentialStyleWeight_j1pt_200_350_UP,
    'QCDScaleAcceptance_Differential_WplusH_j1pt_200_350DOWN':CalculateDifferentialStyleWeight_j1pt_200_350_DOWN,
    'QCDScaleAcceptance_Differential_WplusH_j1pt_gt350UP':CalculateDifferentialStyleWeight_j1pt_gt350_UP,
    'QCDScaleAcceptance_Differential_WplusH_j1pt_gt350DOWN':CalculateDifferentialStyleWeight_j1pt_gt350_DOWN,
}
WplusHStyleWeight_Differential.prepUpAndDownConstants = prepUpAndDownConstants
WplusHStyleWeight_Differential.prepUpAndDownConstants(WplusHStyleWeight_Differential)

ZHStyleWeight_Differential = Weight()
ZHStyleWeight_Differential.name = 'QCDScaleAcceptance_Differential_ZH'
ZHStyleWeight_Differential.reweightFile = ROOT.TFile(localWeightDataPath+'/theory_uncertainties_differential/ZH125.root')
ZHStyleWeight_Differential.hasUpDownUncertainties = True
ZHStyleWeight_Differential.CalculateWeight = CalculateDifferentialStyleWeight
ZHStyleWeight_Differential.uncertaintyVariationList = [
    'QCDScaleAcceptance_Differential_ZH_pth_0_45UP',
    'QCDScaleAcceptance_Differential_ZH_pth_0_45DOWN',
    'QCDScaleAcceptance_Differential_ZH_pth_45_80UP',
    'QCDScaleAcceptance_Differential_ZH_pth_45_80DOWN',
    'QCDScaleAcceptance_Differential_ZH_pth_80_120UP',
    'QCDScaleAcceptance_Differential_ZH_pth_80_120DOWN',
    'QCDScaleAcceptance_Differential_ZH_pth_120_200UP',
    'QCDScaleAcceptance_Differential_ZH_pth_120_200DOWN',
    'QCDScaleAcceptance_Differential_ZH_pth_200_350UP',
    'QCDScaleAcceptance_Differential_ZH_pth_200_350DOWN',
    'QCDScaleAcceptance_Differential_ZH_pth_350_450UP',
    'QCDScaleAcceptance_Differential_ZH_pth_350_450DOWN',
    'QCDScaleAcceptance_Differential_ZH_pth_gt450UP',
    'QCDScaleAcceptance_Differential_ZH_pth_gt450DOWN',
    'QCDScaleAcceptance_Differential_ZH_njets0UP',
    'QCDScaleAcceptance_Differential_ZH_njets0DOWN',
    'QCDScaleAcceptance_Differential_ZH_njets1UP',
    'QCDScaleAcceptance_Differential_ZH_njets1DOWN',
    'QCDScaleAcceptance_Differential_ZH_njets2UP',
    'QCDScaleAcceptance_Differential_ZH_njets2DOWN',
    'QCDScaleAcceptance_Differential_ZH_njets3UP',
    'QCDScaleAcceptance_Differential_ZH_njets3DOWN',
    'QCDScaleAcceptance_Differential_ZH_njets4UP',
    'QCDScaleAcceptance_Differential_ZH_njets4DOWN',
    'QCDScaleAcceptance_Differential_ZH_j1pt_30_60UP',
    'QCDScaleAcceptance_Differential_ZH_j1pt_30_60DOWN',
    'QCDScaleAcceptance_Differential_ZH_j1pt_60_120UP',
    'QCDScaleAcceptance_Differential_ZH_j1pt_60_120DOWN',
    'QCDScaleAcceptance_Differential_ZH_j1pt_120_200UP',
    'QCDScaleAcceptance_Differential_ZH_j1pt_120_200DOWN',
    'QCDScaleAcceptance_Differential_ZH_j1pt_200_350UP',
    'QCDScaleAcceptance_Differential_ZH_j1pt_200_350DOWN',
    'QCDScaleAcceptance_Differential_ZH_j1pt_gt350UP',
    'QCDScaleAcceptance_Differential_ZH_j1pt_gt350DOWN',
]
ZHStyleWeight_Differential.InitUncertaintyVariations()
ZHStyleWeight_Differential.uncertaintyVariationFunctions={
    'QCDScaleAcceptance_Differential_ZH_pth_0_45UP':CalculateDifferentialStyleWeight_pth_0_45_UP,
    'QCDScaleAcceptance_Differential_ZH_pth_0_45DOWN':CalculateDifferentialStyleWeight_pth_0_45_DOWN,
    'QCDScaleAcceptance_Differential_ZH_pth_45_80UP':CalculateDifferentialStyleWeight_pth_45_80_UP,
    'QCDScaleAcceptance_Differential_ZH_pth_45_80DOWN':CalculateDifferentialStyleWeight_pth_45_80_DOWN,
    'QCDScaleAcceptance_Differential_ZH_pth_80_120UP':CalculateDifferentialStyleWeight_pth_80_120_UP,
    'QCDScaleAcceptance_Differential_ZH_pth_80_120DOWN':CalculateDifferentialStyleWeight_pth_80_120_DOWN,
    'QCDScaleAcceptance_Differential_ZH_pth_120_200UP':CalculateDifferentialStyleWeight_pth_120_200_UP,
    'QCDScaleAcceptance_Differential_ZH_pth_120_200DOWN':CalculateDifferentialStyleWeight_pth_120_200_DOWN,
    'QCDScaleAcceptance_Differential_ZH_pth_200_350UP':CalculateDifferentialStyleWeight_pth_200_350_UP,
    'QCDScaleAcceptance_Differential_ZH_pth_200_350DOWN':CalculateDifferentialStyleWeight_pth_200_350_DOWN,
    'QCDScaleAcceptance_Differential_ZH_pth_350_450UP':CalculateDifferentialStyleWeight_pth_350_450_UP,
    'QCDScaleAcceptance_Differential_ZH_pth_350_450DOWN':CalculateDifferentialStyleWeight_pth_350_450_DOWN,
    'QCDScaleAcceptance_Differential_ZH_pth_gt450UP':CalculateDifferentialStyleWeight_pth_gt450_UP,
    'QCDScaleAcceptance_Differential_ZH_pth_gt450DOWN':CalculateDifferentialStyleWeight_pth_gt450_DOWN,
    'QCDScaleAcceptance_Differential_ZH_njets0UP':CalculateDifferentialStyleWeight_njets_0_UP,
    'QCDScaleAcceptance_Differential_ZH_njets0DOWN':CalculateDifferentialStyleWeight_njets_0_DOWN,
    'QCDScaleAcceptance_Differential_ZH_njets1UP':CalculateDifferentialStyleWeight_njets_1_UP,
    'QCDScaleAcceptance_Differential_ZH_njets1DOWN':CalculateDifferentialStyleWeight_njets_1_DOWN,
    'QCDScaleAcceptance_Differential_ZH_njets2UP':CalculateDifferentialStyleWeight_njets_2_UP,
    'QCDScaleAcceptance_Differential_ZH_njets2DOWN':CalculateDifferentialStyleWeight_njets_2_DOWN,
    'QCDScaleAcceptance_Differential_ZH_njets3UP':CalculateDifferentialStyleWeight_njets_3_UP,
    'QCDScaleAcceptance_Differential_ZH_njets3DOWN':CalculateDifferentialStyleWeight_njets_3_DOWN,
    'QCDScaleAcceptance_Differential_ZH_njets4UP':CalculateDifferentialStyleWeight_njets_GE4_UP,
    'QCDScaleAcceptance_Differential_ZH_njets4DOWN':CalculateDifferentialStyleWeight_njets_GE4_DOWN,
    'QCDScaleAcceptance_Differential_ZH_j1pt_30_60UP':CalculateDifferentialStyleWeight_j1pt_30_60_UP,
    'QCDScaleAcceptance_Differential_ZH_j1pt_30_60DOWN':CalculateDifferentialStyleWeight_j1pt_30_60_DOWN,
    'QCDScaleAcceptance_Differential_ZH_j1pt_60_120UP':CalculateDifferentialStyleWeight_j1pt_60_120_UP,
    'QCDScaleAcceptance_Differential_ZH_j1pt_60_120DOWN':CalculateDifferentialStyleWeight_j1pt_60_120_DOWN,
    'QCDScaleAcceptance_Differential_ZH_j1pt_120_200UP':CalculateDifferentialStyleWeight_j1pt_120_200_UP,
    'QCDScaleAcceptance_Differential_ZH_j1pt_120_200DOWN':CalculateDifferentialStyleWeight_j1pt_120_200_DOWN,
    'QCDScaleAcceptance_Differential_ZH_j1pt_200_350UP':CalculateDifferentialStyleWeight_j1pt_200_350_UP,
    'QCDScaleAcceptance_Differential_ZH_j1pt_200_350DOWN':CalculateDifferentialStyleWeight_j1pt_200_350_DOWN,
    'QCDScaleAcceptance_Differential_ZH_j1pt_gt350UP':CalculateDifferentialStyleWeight_j1pt_gt350_UP,
    'QCDScaleAcceptance_Differential_ZH_j1pt_gt350DOWN':CalculateDifferentialStyleWeight_j1pt_gt350_DOWN,
}
ZHStyleWeight_Differential.prepUpAndDownConstants = prepUpAndDownConstants
ZHStyleWeight_Differential.prepUpAndDownConstants(ZHStyleWeight_Differential)

GGZHLLTTStyleWeight_Differential = Weight()
GGZHLLTTStyleWeight_Differential.name = 'QCDScaleAcceptance_Differential_GGZHLLTT'
GGZHLLTTStyleWeight_Differential.reweightFile = ROOT.TFile(localWeightDataPath+'/theory_uncertainties_differential/GGZHLLTT125.root')
GGZHLLTTStyleWeight_Differential.hasUpDownUncertainties = True
GGZHLLTTStyleWeight_Differential.CalculateWeight = CalculateDifferentialStyleWeight
GGZHLLTTStyleWeight_Differential.uncertaintyVariationList = [
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_0_45UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_0_45DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_45_80UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_45_80DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_80_120UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_80_120DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_120_200UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_120_200DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_200_350UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_200_350DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_350_450UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_350_450DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_gt450UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_gt450DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets0UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets0DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets1UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets1DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets2UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets2DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets3UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets3DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets4UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets4DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_30_60UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_30_60DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_60_120UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_60_120DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_120_200UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_120_200DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_200_350UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_200_350DOWN',
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_gt350UP',
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_gt350DOWN',
]
GGZHLLTTStyleWeight_Differential.InitUncertaintyVariations()
GGZHLLTTStyleWeight_Differential.uncertaintyVariationFunctions={
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_0_45UP':CalculateDifferentialStyleWeight_pth_0_45_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_0_45DOWN':CalculateDifferentialStyleWeight_pth_0_45_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_45_80UP':CalculateDifferentialStyleWeight_pth_45_80_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_45_80DOWN':CalculateDifferentialStyleWeight_pth_45_80_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_80_120UP':CalculateDifferentialStyleWeight_pth_80_120_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_80_120DOWN':CalculateDifferentialStyleWeight_pth_80_120_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_120_200UP':CalculateDifferentialStyleWeight_pth_120_200_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_120_200DOWN':CalculateDifferentialStyleWeight_pth_120_200_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_200_350UP':CalculateDifferentialStyleWeight_pth_200_350_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_200_350DOWN':CalculateDifferentialStyleWeight_pth_200_350_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_350_450UP':CalculateDifferentialStyleWeight_pth_350_450_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_350_450DOWN':CalculateDifferentialStyleWeight_pth_350_450_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_gt450UP':CalculateDifferentialStyleWeight_pth_gt450_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_pth_gt450DOWN':CalculateDifferentialStyleWeight_pth_gt450_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets0UP':CalculateDifferentialStyleWeight_njets_0_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets0DOWN':CalculateDifferentialStyleWeight_njets_0_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets1UP':CalculateDifferentialStyleWeight_njets_1_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets1DOWN':CalculateDifferentialStyleWeight_njets_1_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets2UP':CalculateDifferentialStyleWeight_njets_2_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets2DOWN':CalculateDifferentialStyleWeight_njets_2_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets3UP':CalculateDifferentialStyleWeight_njets_3_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets3DOWN':CalculateDifferentialStyleWeight_njets_3_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets4UP':CalculateDifferentialStyleWeight_njets_GE4_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_njets4DOWN':CalculateDifferentialStyleWeight_njets_GE4_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_30_60UP':CalculateDifferentialStyleWeight_j1pt_30_60_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_30_60DOWN':CalculateDifferentialStyleWeight_j1pt_30_60_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_60_120UP':CalculateDifferentialStyleWeight_j1pt_60_120_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_60_120DOWN':CalculateDifferentialStyleWeight_j1pt_60_120_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_120_200UP':CalculateDifferentialStyleWeight_j1pt_120_200_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_120_200DOWN':CalculateDifferentialStyleWeight_j1pt_120_200_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_200_350UP':CalculateDifferentialStyleWeight_j1pt_200_350_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_200_350DOWN':CalculateDifferentialStyleWeight_j1pt_200_350_DOWN,
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_gt350UP':CalculateDifferentialStyleWeight_j1pt_gt350_UP,
    'QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_gt350DOWN':CalculateDifferentialStyleWeight_j1pt_gt350_DOWN,
}
GGZHLLTTStyleWeight_Differential.prepUpAndDownConstants = prepUpAndDownConstants
GGZHLLTTStyleWeight_Differential.prepUpAndDownConstants(GGZHLLTTStyleWeight_Differential)

GGZHNNTTStyleWeight_Differential = Weight()
GGZHNNTTStyleWeight_Differential.name = 'QCDScaleAcceptance_Differential_GGZHNNTT'
GGZHNNTTStyleWeight_Differential.reweightFile = ROOT.TFile(localWeightDataPath+'/theory_uncertainties_differential/GGZHNNTT125.root')
GGZHNNTTStyleWeight_Differential.hasUpDownUncertainties = True
GGZHNNTTStyleWeight_Differential.CalculateWeight = CalculateDifferentialStyleWeight
GGZHNNTTStyleWeight_Differential.uncertaintyVariationList = [
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_0_45UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_0_45DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_45_80UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_45_80DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_80_120UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_80_120DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_120_200UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_120_200DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_200_350UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_200_350DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_350_450UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_350_450DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_gt450UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_gt450DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets0UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets0DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets1UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets1DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets2UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets2DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets3UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets3DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets4UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets4DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_30_60UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_30_60DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_60_120UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_60_120DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_120_200UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_120_200DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_200_350UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_200_350DOWN',
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_gt350UP',
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_gt350DOWN',
]
GGZHNNTTStyleWeight_Differential.InitUncertaintyVariations()
GGZHNNTTStyleWeight_Differential.uncertaintyVariationFunctions={
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_0_45UP':CalculateDifferentialStyleWeight_pth_0_45_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_0_45DOWN':CalculateDifferentialStyleWeight_pth_0_45_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_45_80UP':CalculateDifferentialStyleWeight_pth_45_80_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_45_80DOWN':CalculateDifferentialStyleWeight_pth_45_80_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_80_120UP':CalculateDifferentialStyleWeight_pth_80_120_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_80_120DOWN':CalculateDifferentialStyleWeight_pth_80_120_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_120_200UP':CalculateDifferentialStyleWeight_pth_120_200_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_120_200DOWN':CalculateDifferentialStyleWeight_pth_120_200_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_200_350UP':CalculateDifferentialStyleWeight_pth_200_350_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_200_350DOWN':CalculateDifferentialStyleWeight_pth_200_350_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_350_450UP':CalculateDifferentialStyleWeight_pth_350_450_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_350_450DOWN':CalculateDifferentialStyleWeight_pth_350_450_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_gt450UP':CalculateDifferentialStyleWeight_pth_gt450_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_pth_gt450DOWN':CalculateDifferentialStyleWeight_pth_gt450_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets0UP':CalculateDifferentialStyleWeight_njets_0_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets0DOWN':CalculateDifferentialStyleWeight_njets_0_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets1UP':CalculateDifferentialStyleWeight_njets_1_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets1DOWN':CalculateDifferentialStyleWeight_njets_1_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets2UP':CalculateDifferentialStyleWeight_njets_2_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets2DOWN':CalculateDifferentialStyleWeight_njets_2_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets3UP':CalculateDifferentialStyleWeight_njets_3_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets3DOWN':CalculateDifferentialStyleWeight_njets_3_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets4UP':CalculateDifferentialStyleWeight_njets_GE4_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_njets4DOWN':CalculateDifferentialStyleWeight_njets_GE4_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_30_60UP':CalculateDifferentialStyleWeight_j1pt_30_60_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_30_60DOWN':CalculateDifferentialStyleWeight_j1pt_30_60_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_60_120UP':CalculateDifferentialStyleWeight_j1pt_60_120_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_60_120DOWN':CalculateDifferentialStyleWeight_j1pt_60_120_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_120_200UP':CalculateDifferentialStyleWeight_j1pt_120_200_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_120_200DOWN':CalculateDifferentialStyleWeight_j1pt_120_200_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_200_350UP':CalculateDifferentialStyleWeight_j1pt_200_350_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_200_350DOWN':CalculateDifferentialStyleWeight_j1pt_200_350_DOWN,
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_gt350UP':CalculateDifferentialStyleWeight_j1pt_gt350_UP,
    'QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_gt350DOWN':CalculateDifferentialStyleWeight_j1pt_gt350_DOWN,
}
GGZHNNTTStyleWeight_Differential.prepUpAndDownConstants = prepUpAndDownConstants
GGZHNNTTStyleWeight_Differential.prepUpAndDownConstants(GGZHNNTTStyleWeight_Differential)

GGZHQQTTStyleWeight_Differential = Weight()
GGZHQQTTStyleWeight_Differential.name = 'QCDScaleAcceptance_Differential_GGZHQQTT'
GGZHQQTTStyleWeight_Differential.reweightFile = ROOT.TFile(localWeightDataPath+'/theory_uncertainties_differential/GGZHQQTT125.root')
GGZHQQTTStyleWeight_Differential.hasUpDownUncertainties = True
GGZHQQTTStyleWeight_Differential.CalculateWeight = CalculateDifferentialStyleWeight
GGZHQQTTStyleWeight_Differential.uncertaintyVariationList = [
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_0_45UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_0_45DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_45_80UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_45_80DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_80_120UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_80_120DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_120_200UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_120_200DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_200_350UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_200_350DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_350_450UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_350_450DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_gt450UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_gt450DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets0UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets0DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets1UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets1DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets2UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets2DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets3UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets3DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets4UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets4DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_30_60UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_30_60DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_60_120UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_60_120DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_120_200UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_120_200DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_200_350UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_200_350DOWN',
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_gt350UP',
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_gt350DOWN',
]
GGZHQQTTStyleWeight_Differential.InitUncertaintyVariations()
GGZHQQTTStyleWeight_Differential.uncertaintyVariationFunctions={
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_0_45UP':CalculateDifferentialStyleWeight_pth_0_45_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_0_45DOWN':CalculateDifferentialStyleWeight_pth_0_45_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_45_80UP':CalculateDifferentialStyleWeight_pth_45_80_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_45_80DOWN':CalculateDifferentialStyleWeight_pth_45_80_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_80_120UP':CalculateDifferentialStyleWeight_pth_80_120_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_80_120DOWN':CalculateDifferentialStyleWeight_pth_80_120_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_120_200UP':CalculateDifferentialStyleWeight_pth_120_200_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_120_200DOWN':CalculateDifferentialStyleWeight_pth_120_200_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_200_350UP':CalculateDifferentialStyleWeight_pth_200_350_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_200_350DOWN':CalculateDifferentialStyleWeight_pth_200_350_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_350_450UP':CalculateDifferentialStyleWeight_pth_350_450_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_350_450DOWN':CalculateDifferentialStyleWeight_pth_350_450_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_gt450UP':CalculateDifferentialStyleWeight_pth_gt450_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_pth_gt450DOWN':CalculateDifferentialStyleWeight_pth_gt450_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets0UP':CalculateDifferentialStyleWeight_njets_0_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets0DOWN':CalculateDifferentialStyleWeight_njets_0_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets1UP':CalculateDifferentialStyleWeight_njets_1_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets1DOWN':CalculateDifferentialStyleWeight_njets_1_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets2UP':CalculateDifferentialStyleWeight_njets_2_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets2DOWN':CalculateDifferentialStyleWeight_njets_2_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets3UP':CalculateDifferentialStyleWeight_njets_3_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets3DOWN':CalculateDifferentialStyleWeight_njets_3_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets4UP':CalculateDifferentialStyleWeight_njets_GE4_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_njets4DOWN':CalculateDifferentialStyleWeight_njets_GE4_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_30_60UP':CalculateDifferentialStyleWeight_j1pt_30_60_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_30_60DOWN':CalculateDifferentialStyleWeight_j1pt_30_60_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_60_120UP':CalculateDifferentialStyleWeight_j1pt_60_120_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_60_120DOWN':CalculateDifferentialStyleWeight_j1pt_60_120_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_120_200UP':CalculateDifferentialStyleWeight_j1pt_120_200_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_120_200DOWN':CalculateDifferentialStyleWeight_j1pt_120_200_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_200_350UP':CalculateDifferentialStyleWeight_j1pt_200_350_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_200_350DOWN':CalculateDifferentialStyleWeight_j1pt_200_350_DOWN,
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_gt350UP':CalculateDifferentialStyleWeight_j1pt_gt350_UP,
    'QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_gt350DOWN':CalculateDifferentialStyleWeight_j1pt_gt350_DOWN,
}
GGZHQQTTStyleWeight_Differential.prepUpAndDownConstants = prepUpAndDownConstants
GGZHQQTTStyleWeight_Differential.prepUpAndDownConstants(GGZHQQTTStyleWeight_Differential)

ttHStyleWeight_Differential = Weight()
ttHStyleWeight_Differential.name = 'QCDScaleAcceptance_Differential_ttH'
ttHStyleWeight_Differential.reweightFile = ROOT.TFile(localWeightDataPath+'/theory_uncertainties_differential/ttHTT125.root')
ttHStyleWeight_Differential.hasUpDownUncertainties = True
ttHStyleWeight_Differential.CalculateWeight = CalculateDifferentialStyleWeight
ttHStyleWeight_Differential.uncertaintyVariationList = [
    'QCDScaleAcceptance_Differential_ttH_pth_0_45UP',
    'QCDScaleAcceptance_Differential_ttH_pth_0_45DOWN',
    'QCDScaleAcceptance_Differential_ttH_pth_45_80UP',
    'QCDScaleAcceptance_Differential_ttH_pth_45_80DOWN',
    'QCDScaleAcceptance_Differential_ttH_pth_80_120UP',
    'QCDScaleAcceptance_Differential_ttH_pth_80_120DOWN',
    'QCDScaleAcceptance_Differential_ttH_pth_120_200UP',
    'QCDScaleAcceptance_Differential_ttH_pth_120_200DOWN',
    'QCDScaleAcceptance_Differential_ttH_pth_200_350UP',
    'QCDScaleAcceptance_Differential_ttH_pth_200_350DOWN',
    'QCDScaleAcceptance_Differential_ttH_pth_350_450UP',
    'QCDScaleAcceptance_Differential_ttH_pth_350_450DOWN',
    'QCDScaleAcceptance_Differential_ttH_pth_gt450UP',
    'QCDScaleAcceptance_Differential_ttH_pth_gt450DOWN',
    'QCDScaleAcceptance_Differential_ttH_njets0UP',
    'QCDScaleAcceptance_Differential_ttH_njets0DOWN',
    'QCDScaleAcceptance_Differential_ttH_njets1UP',
    'QCDScaleAcceptance_Differential_ttH_njets1DOWN',
    'QCDScaleAcceptance_Differential_ttH_njets2UP',
    'QCDScaleAcceptance_Differential_ttH_njets2DOWN',
    'QCDScaleAcceptance_Differential_ttH_njets3UP',
    'QCDScaleAcceptance_Differential_ttH_njets3DOWN',
    'QCDScaleAcceptance_Differential_ttH_njets4UP',
    'QCDScaleAcceptance_Differential_ttH_njets4DOWN',
    'QCDScaleAcceptance_Differential_ttH_j1pt_30_60UP',
    'QCDScaleAcceptance_Differential_ttH_j1pt_30_60DOWN',
    'QCDScaleAcceptance_Differential_ttH_j1pt_60_120UP',
    'QCDScaleAcceptance_Differential_ttH_j1pt_60_120DOWN',
    'QCDScaleAcceptance_Differential_ttH_j1pt_120_200UP',
    'QCDScaleAcceptance_Differential_ttH_j1pt_120_200DOWN',
    'QCDScaleAcceptance_Differential_ttH_j1pt_200_350UP',
    'QCDScaleAcceptance_Differential_ttH_j1pt_200_350DOWN',
    'QCDScaleAcceptance_Differential_ttH_j1pt_gt350UP',
    'QCDScaleAcceptance_Differential_ttH_j1pt_gt350DOWN',
]
ttHStyleWeight_Differential.InitUncertaintyVariations()
ttHStyleWeight_Differential.uncertaintyVariationFunctions={
    'QCDScaleAcceptance_Differential_ttH_pth_0_45UP':CalculateDifferentialStyleWeight_pth_0_45_UP,
    'QCDScaleAcceptance_Differential_ttH_pth_0_45DOWN':CalculateDifferentialStyleWeight_pth_0_45_DOWN,
    'QCDScaleAcceptance_Differential_ttH_pth_45_80UP':CalculateDifferentialStyleWeight_pth_45_80_UP,
    'QCDScaleAcceptance_Differential_ttH_pth_45_80DOWN':CalculateDifferentialStyleWeight_pth_45_80_DOWN,
    'QCDScaleAcceptance_Differential_ttH_pth_80_120UP':CalculateDifferentialStyleWeight_pth_80_120_UP,
    'QCDScaleAcceptance_Differential_ttH_pth_80_120DOWN':CalculateDifferentialStyleWeight_pth_80_120_DOWN,
    'QCDScaleAcceptance_Differential_ttH_pth_120_200UP':CalculateDifferentialStyleWeight_pth_120_200_UP,
    'QCDScaleAcceptance_Differential_ttH_pth_120_200DOWN':CalculateDifferentialStyleWeight_pth_120_200_DOWN,
    'QCDScaleAcceptance_Differential_ttH_pth_200_350UP':CalculateDifferentialStyleWeight_pth_200_350_UP,
    'QCDScaleAcceptance_Differential_ttH_pth_200_350DOWN':CalculateDifferentialStyleWeight_pth_200_350_DOWN,
    'QCDScaleAcceptance_Differential_ttH_pth_350_450UP':CalculateDifferentialStyleWeight_pth_350_450_UP,
    'QCDScaleAcceptance_Differential_ttH_pth_350_450DOWN':CalculateDifferentialStyleWeight_pth_350_450_DOWN,
    'QCDScaleAcceptance_Differential_ttH_pth_gt450UP':CalculateDifferentialStyleWeight_pth_gt450_UP,
    'QCDScaleAcceptance_Differential_ttH_pth_gt450DOWN':CalculateDifferentialStyleWeight_pth_gt450_DOWN,
    'QCDScaleAcceptance_Differential_ttH_njets0UP':CalculateDifferentialStyleWeight_njets_0_UP,
    'QCDScaleAcceptance_Differential_ttH_njets0DOWN':CalculateDifferentialStyleWeight_njets_0_DOWN,
    'QCDScaleAcceptance_Differential_ttH_njets1UP':CalculateDifferentialStyleWeight_njets_1_UP,
    'QCDScaleAcceptance_Differential_ttH_njets1DOWN':CalculateDifferentialStyleWeight_njets_1_DOWN,
    'QCDScaleAcceptance_Differential_ttH_njets2UP':CalculateDifferentialStyleWeight_njets_2_UP,
    'QCDScaleAcceptance_Differential_ttH_njets2DOWN':CalculateDifferentialStyleWeight_njets_2_DOWN,
    'QCDScaleAcceptance_Differential_ttH_njets3UP':CalculateDifferentialStyleWeight_njets_3_UP,
    'QCDScaleAcceptance_Differential_ttH_njets3DOWN':CalculateDifferentialStyleWeight_njets_3_DOWN,
    'QCDScaleAcceptance_Differential_ttH_njets4UP':CalculateDifferentialStyleWeight_njets_GE4_UP,
    'QCDScaleAcceptance_Differential_ttH_njets4DOWN':CalculateDifferentialStyleWeight_njets_GE4_DOWN,
    'QCDScaleAcceptance_Differential_ttH_j1pt_30_60UP':CalculateDifferentialStyleWeight_j1pt_30_60_UP,
    'QCDScaleAcceptance_Differential_ttH_j1pt_30_60DOWN':CalculateDifferentialStyleWeight_j1pt_30_60_DOWN,
    'QCDScaleAcceptance_Differential_ttH_j1pt_60_120UP':CalculateDifferentialStyleWeight_j1pt_60_120_UP,
    'QCDScaleAcceptance_Differential_ttH_j1pt_60_120DOWN':CalculateDifferentialStyleWeight_j1pt_60_120_DOWN,
    'QCDScaleAcceptance_Differential_ttH_j1pt_120_200UP':CalculateDifferentialStyleWeight_j1pt_120_200_UP,
    'QCDScaleAcceptance_Differential_ttH_j1pt_120_200DOWN':CalculateDifferentialStyleWeight_j1pt_120_200_DOWN,
    'QCDScaleAcceptance_Differential_ttH_j1pt_200_350UP':CalculateDifferentialStyleWeight_j1pt_200_350_UP,
    'QCDScaleAcceptance_Differential_ttH_j1pt_200_350DOWN':CalculateDifferentialStyleWeight_j1pt_200_350_DOWN,
    'QCDScaleAcceptance_Differential_ttH_j1pt_gt350UP':CalculateDifferentialStyleWeight_j1pt_gt350_UP,
    'QCDScaleAcceptance_Differential_ttH_j1pt_gt350DOWN':CalculateDifferentialStyleWeight_j1pt_gt350_DOWN,
}
ttHStyleWeight_Differential.prepUpAndDownConstants = prepUpAndDownConstants
ttHStyleWeight_Differential.prepUpAndDownConstants(ttHStyleWeight_Differential)
