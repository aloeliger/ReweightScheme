import ROOT
from Configurations.Weights.WeightDefinition import Weight
from Configurations.Weights import localWeightDataPath

from AddggHTheoryUncertainties import qcd_ggF_uncert_2017 as ggH_Theory_Calculation

def CalculateggHTheoryNominal(self,theTree):
    self.value[0] = 1.0
    
def CalculateDummyggHTheoryUncertainty(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggHMuUP (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0+result[0]

def CalculateggHMuDOWN (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0-result[0]

def CalculateggHResUP (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0+result[1]

def CalculateggHResDOWN (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0-result[1]

def CalculateggHMig01UP (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0+result[2]

def CalculateggHMig01DOWN (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0-result[2]

def CalculateggHMig12UP (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0+result[3]

def CalculateggHMig12DOWN (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0-result[3]

def CalculateggHVBF2jUP (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0+result[4]

def CalculateggHVBF2jDOWN (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0-result[4]

def CalculateggHVBF3jUP (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0+result[5]

def CalculateggHVBF3jDOWN (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0-result[5]

def CalculateggHPT60UP (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0+result[6]

def CalculateggHPT60DOWN (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0-result[6]

def CalculateggHPT120UP (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0+result[7]

def CalculateggHPT120DOWN (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0-result[7]

def CalculateggHqmtopUP (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0+result[8]

def CalculateggHqmtopDOWN (self,theTree,uncert):
    result = ggH_Theory_Calculation(theTree.Rivet_nJets30,
                                    theTree.Rivet_higgsPt,
                                    theTree.Rivet_stage1_cat_pTjet30GeV)
    self.uncertaintyVariationArrays[uncert][0] = 1.0-result[8]

ggHTheoryWeight = Weight()
ggHTheoryWeight.name = 'ggHTheory'
ggHTheoryWeight.hasUpDownUncertainties = True
ggHTheoryWeight.CalculateWeight = CalculateggHTheoryNominal
ggHTheoryWeight.uncertaintyVariationList = [
    "ggHTheory_Mu_UP",
    "ggHTheory_Mu_DOWN",
    "ggHTheory_Res_UP",
    "ggHTheory_Res_DOWN",
    "ggHTheory_Mig01_UP",
    "ggHTheory_Mig01_DOWN",
    "ggHTheory_Mig12_UP",
    "ggHTheory_Mig12_DOWN",
    "ggHTheory_VBF2j_UP",
    "ggHTheory_VBF2j_DOWN",
    "ggHTheory_VBF3j_UP",
    "ggHTheory_VBF3j_DOWN",
    "ggHTheory_PT60_UP",
    "ggHTheory_PT60_DOWN",
    "ggHTheory_PT120_UP",
    "ggHTheory_PT120_DOWN",
    "ggHTheory_qmtop_UP",
    "ggHTheory_qmtop_DOWN",
]
ggHTheoryWeight.InitUncertaintyVariations()
ggHTheoryWeight.uncertaintyVariationFunctions={
    "ggHTheory_Mu_UP":CalculateggHMuUP,
    "ggHTheory_Mu_DOWN":CalculateggHMuDOWN,
    "ggHTheory_Res_UP":CalculateggHResUP,
    "ggHTheory_Res_DOWN":CalculateggHResDOWN,
    "ggHTheory_Mig01_UP":CalculateggHMig01UP,
    "ggHTheory_Mig01_DOWN":CalculateggHMig12DOWN,
    "ggHTheory_Mig12_UP":CalculateggHMig12UP,
    "ggHTheory_Mig12_DOWN":CalculateggHMig12DOWN,
    "ggHTheory_VBF2j_UP":CalculateggHVBF2jUP,
    "ggHTheory_VBF2j_DOWN":CalculateggHVBF2jDOWN,
    "ggHTheory_VBF3j_UP":CalculateggHVBF3jUP,
    "ggHTheory_VBF3j_DOWN":CalculateggHVBF3jDOWN,
    "ggHTheory_PT60_UP":CalculateggHPT60UP,
    "ggHTheory_PT60_DOWN":CalculateggHPT60DOWN,
    "ggHTheory_PT120_UP":CalculateggHPT120UP,
    "ggHTheory_PT120_DOWN":CalculateggHPT120DOWN,
    "ggHTheory_qmtop_UP":CalculateggHqmtopUP,
    "ggHTheory_qmtop_DOWN":CalculateggHqmtopDOWN,
}

dummyggHTheoryWeight = Weight()
dummyggHTheoryWeight.name = 'ggHTheory'
dummyggHTheoryWeight.hasUpDownUncertainties = True
dummyggHTheoryWeight.CalculateWeight = CalculateggHTheoryNominal
dummyggHTheoryWeight.uncertaintyVariationList = [
    "ggHTheory_Mu_UP",
    "ggHTheory_Mu_DOWN",
    "ggHTheory_Res_UP",
    "ggHTheory_Res_DOWN",
    "ggHTheory_Mig01_UP",
    "ggHTheory_Mig01_DOWN",
    "ggHTheory_Mig12_UP",
    "ggHTheory_Mig12_DOWN",
    "ggHTheory_VBF2j_UP",
    "ggHTheory_VBF2j_DOWN",
    "ggHTheory_VBF3j_UP",
    "ggHTheory_VBF3j_DOWN",
    "ggHTheory_PT60_UP",
    "ggHTheory_PT60_DOWN",
    "ggHTheory_PT120_UP",
    "ggHTheory_PT120_DOWN",
    "ggHTheory_qmtop_UP",
    "ggHTheory_qmtop_DOWN",
]
dummyggHTheoryWeight.InitUncertaintyVariations()
dummyggHTheoryWeight.uncertaintyVariationFunctions={
    "ggHTheory_Mu_UP":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_Mu_DOWN":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_Res_UP":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_Res_DOWN":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_Mig01_UP":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_Mig01_DOWN":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_Mig12_UP":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_Mig12_DOWN":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_VBF2j_UP":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_VBF2j_DOWN":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_VBF3j_UP":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_VBF3j_DOWN":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_PT60_UP":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_PT60_DOWN":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_PT120_UP":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_PT120_DOWN":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_qmtop_UP":CalculateDummyggHTheoryUncertainty,
    "ggHTheory_qmtop_DOWN":CalculateDummyggHTheoryUncertainty,
}
