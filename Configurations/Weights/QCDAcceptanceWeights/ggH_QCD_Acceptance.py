import ROOT
from Configurations.Weights.WeightDefinition import Weight
from Configurations.Weights import localWeightDataPath

def prepUpAndDownConstants(self):
    self.weightHistogram_0jet = self.reweightFile.demo.Get("h_nevents_ggH_scale_0jet")
    self.constantUP_0jet = self.weightHistogram_0jet.GetBinContent(1)/self.weightHistogram_0jet.GetBinContent(5)
    self.constantDOWN_0jet = self.weightHistogram_0jet.GetBinContent(1)/self.weightHistogram_0jet.GetBinContent(9)

    self.weightHistogram_1jet_lowpt = self.reweightFile.demo.Get("h_nevents_ggH_scale_1jet_lowpt")
    self.constantUP_1jet_lowpt = self.weightHistogram_1jet_lowpt.GetBinContent(1)/self.weightHistogram_1jet_lowpt.GetBinContent(5)
    self.constantDOWN_1jet_lowpt = self.weightHistogram_1jet_lowpt.GetBinContent(1)/self.weightHistogram_1jet_lowpt.GetBinContent(9)
    
    self.weightHistogram_2jet_lowpt = self.reweightFile.demo.Get("h_nevents_ggH_scale_2jet_lowpt")
    self.constantUP_2jet_lowpt = self.weightHistogram_2jet_lowpt.GetBinContent(1)/self.weightHistogram_2jet_lowpt.GetBinContent(5)
    self.constantDOWN_2jet_lowpt = self.weightHistogram_2jet_lowpt.GetBinContent(1)/self.weightHistogram_2jet_lowpt.GetBinContent(9)
    
    self.weightHistogram_highpt = self.reweightFile.demo.Get("h_nevents_ggH_scale_highpt")
    self.constantUP_highpt = self.weightHistogram_highpt.GetBinContent(1)/self.weightHistogram_highpt.GetBinContent(5)
    self.constantDOWN_highpt = self.weightHistogram_highpt.GetBinContent(1)/self.weightHistogram_highpt.GetBinContent(9)

    self.weightHistogram_very_highpt = self.reweightFile.demo.Get("h_nevents_ggH_scale_very_highpt")
    self.constantUP_very_highpt = self.weightHistogram_very_highpt.GetBinContent(1)/self.weightHistogram_very_highpt.GetBinContent(5)
    self.constantDOWN_very_highpt = self.weightHistogram_very_highpt.GetBinContent(1)/self.weightHistogram_very_highpt.GetBinContent(9)

    self.weightHistogram_vbf = self.reweightFile.demo.Get("h_nevents_ggH_scale_vbf")
    self.constantUP_vbf = self.weightHistogram_vbf.GetBinContent(1)/self.weightHistogram_vbf.GetBinContent(5)
    self.constantDOWN_vbf = self.weightHistogram_vbf.GetBinContent(1)/self.weightHistogram_vbf.GetBinContent(9)

    self.weightHistogram_ggH_Inclusive = self.reweightFile.demo.Get("h_nevents_ggH")
    self.constantUP_inclusive = self.weightHistogram_ggH_Inclusive.GetBinContent(1)/self.weightHistogram_ggH_Inclusive.GetBinContent(5)
    self.constantDOWN_inclusive = self.weightHistogram_ggH_Inclusive.GetBinContent(1)/self.weightHistogram_ggH_Inclusive.GetBinContent(9)

def CalculateggHStyleWeight(self,theTree):
    self.value[0] = 1.0

def CalculateggHStyleWeight_Inclusive_UP(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2 * self.constantUP_inclusive

def CalculateggHStyleWeight_Inclusive_DOWN(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5 * self.constantDOWN_inclusive

def CalculateggHStyleWeight_ggH_0jet_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 102
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 103):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_0jet
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggHStyleWeight_ggH_0jet_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 102
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 103):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_0jet
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggHStyleWeight_ggH_1jet_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 104
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 105
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 106):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_1jet_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggHStyleWeight_ggH_1jet_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 104
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 105
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 106):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_1jet_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggHStyleWeight_ggH_2jet_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 107
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 108
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 109):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_2jet_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggHStyleWeight_ggH_2jet_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 107
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 108
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 109):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_2jet_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggHStyleWeight_ggH_highpt_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 101 
       and theTree.Rivet_higgsPt > 200 
       and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggHStyleWeight_ggH_highpt_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 101 
       and theTree.Rivet_higgsPt > 200 
       and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggHStyleWeight_ggH_very_highpt_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 101 
       and theTree.Rivet_higgsPt > 450):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_very_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggHStyleWeight_ggH_very_highpt_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 101 
       and theTree.Rivet_higgsPt > 450):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_very_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggHStyleWeight_ggH_vbf_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 110 
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 111
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 112
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 113):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_vbf
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggHStyleWeight_ggH_vbf_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 110 
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 111
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 112
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 113):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_vbf
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

ggHStyleWeight_2016 = Weight()
ggHStyleWeight_2016.name = 'QCDScaleAcceptance_ggH'
ggHStyleWeight_2016.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/GGHTT2016.root')
ggHStyleWeight_2016.hasUpDownUncertainties = True
ggHStyleWeight_2016.CalculateWeight=CalculateggHStyleWeight
ggHStyleWeight_2016.uncertaintyVariationList = [
    "QCDScaleAcceptance_ggH_scale_0jet_UP",
    "QCDScaleAcceptance_ggH_scale_0jet_DOWN",
    "QCDScaleAcceptance_ggH_scale_1jet_lowpt_UP",
    "QCDScaleAcceptance_ggH_scale_1jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggH_scale_2jet_lowpt_UP",
    "QCDScaleAcceptance_ggH_scale_2jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggH_scale_highpt_UP",
    "QCDScaleAcceptance_ggH_scale_highpt_DOWN",
    "QCDScaleAcceptance_ggH_scale_very_highpt_UP",
    "QCDScaleAcceptance_ggH_scale_very_highpt_DOWN",
    "QCDScaleAcceptance_ggH_scale_vbf_UP",
    "QCDScaleAcceptance_ggH_scale_vbf_DOWN",
    "QCDScaleAcceptance_ggH_scale_Inclusive_UP",
    "QCDScaleAcceptance_ggH_scale_Inclusive_DOWN",
]
ggHStyleWeight_2016.InitUncertaintyVariations()
ggHStyleWeight_2016.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_ggH_scale_0jet_UP":CalculateggHStyleWeight_ggH_0jet_UP,
    "QCDScaleAcceptance_ggH_scale_0jet_DOWN":CalculateggHStyleWeight_ggH_0jet_DOWN,
    "QCDScaleAcceptance_ggH_scale_1jet_lowpt_UP":CalculateggHStyleWeight_ggH_1jet_UP,
    "QCDScaleAcceptance_ggH_scale_1jet_lowpt_DOWN":CalculateggHStyleWeight_ggH_1jet_DOWN,
    "QCDScaleAcceptance_ggH_scale_2jet_lowpt_UP":CalculateggHStyleWeight_ggH_2jet_UP,
    "QCDScaleAcceptance_ggH_scale_2jet_lowpt_DOWN":CalculateggHStyleWeight_ggH_2jet_DOWN,
    "QCDScaleAcceptance_ggH_scale_highpt_UP":CalculateggHStyleWeight_ggH_highpt_UP,
    "QCDScaleAcceptance_ggH_scale_highpt_DOWN":CalculateggHStyleWeight_ggH_highpt_DOWN,
    "QCDScaleAcceptance_ggH_scale_very_highpt_UP":CalculateggHStyleWeight_ggH_very_highpt_UP,
    "QCDScaleAcceptance_ggH_scale_very_highpt_DOWN":CalculateggHStyleWeight_ggH_very_highpt_DOWN,
    "QCDScaleAcceptance_ggH_scale_vbf_UP":CalculateggHStyleWeight_ggH_vbf_UP,
    "QCDScaleAcceptance_ggH_scale_vbf_DOWN":CalculateggHStyleWeight_ggH_vbf_DOWN,
    "QCDScaleAcceptance_ggH_scale_Inclusive_UP":CalculateggHStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_ggH_scale_Inclusive_DOWN":CalculateggHStyleWeight_Inclusive_DOWN,
}
ggHStyleWeight_2016.prepUpAndDownConstants = prepUpAndDownConstants
ggHStyleWeight_2016.prepUpAndDownConstants(ggHStyleWeight_2016)

ggHStyleWeight_2017 = Weight()
ggHStyleWeight_2017.name = 'QCDScaleAcceptance_ggH'
ggHStyleWeight_2017.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/GGHTT2017.root')
ggHStyleWeight_2017.hasUpDownUncertainties = True
ggHStyleWeight_2017.CalculateWeight=CalculateggHStyleWeight
ggHStyleWeight_2017.uncertaintyVariationList = [
    "QCDScaleAcceptance_ggH_scale_0jet_UP",
    "QCDScaleAcceptance_ggH_scale_0jet_DOWN",
    "QCDScaleAcceptance_ggH_scale_1jet_lowpt_UP",
    "QCDScaleAcceptance_ggH_scale_1jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggH_scale_2jet_lowpt_UP",
    "QCDScaleAcceptance_ggH_scale_2jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggH_scale_highpt_UP",
    "QCDScaleAcceptance_ggH_scale_highpt_DOWN",
    "QCDScaleAcceptance_ggH_scale_very_highpt_UP",
    "QCDScaleAcceptance_ggH_scale_very_highpt_DOWN",
    "QCDScaleAcceptance_ggH_scale_vbf_UP",
    "QCDScaleAcceptance_ggH_scale_vbf_DOWN",
    "QCDScaleAcceptance_ggH_scale_Inclusive_UP",
    "QCDScaleAcceptance_ggH_scale_Inclusive_DOWN",
]
ggHStyleWeight_2017.InitUncertaintyVariations()
ggHStyleWeight_2017.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_ggH_scale_0jet_UP":CalculateggHStyleWeight_ggH_0jet_UP,
    "QCDScaleAcceptance_ggH_scale_0jet_DOWN":CalculateggHStyleWeight_ggH_0jet_DOWN,
    "QCDScaleAcceptance_ggH_scale_1jet_lowpt_UP":CalculateggHStyleWeight_ggH_1jet_UP,
    "QCDScaleAcceptance_ggH_scale_1jet_lowpt_DOWN":CalculateggHStyleWeight_ggH_1jet_DOWN,
    "QCDScaleAcceptance_ggH_scale_2jet_lowpt_UP":CalculateggHStyleWeight_ggH_2jet_UP,
    "QCDScaleAcceptance_ggH_scale_2jet_lowpt_DOWN":CalculateggHStyleWeight_ggH_2jet_DOWN,
    "QCDScaleAcceptance_ggH_scale_highpt_UP":CalculateggHStyleWeight_ggH_highpt_UP,
    "QCDScaleAcceptance_ggH_scale_highpt_DOWN":CalculateggHStyleWeight_ggH_highpt_DOWN,
    "QCDScaleAcceptance_ggH_scale_very_highpt_UP":CalculateggHStyleWeight_ggH_very_highpt_UP,
    "QCDScaleAcceptance_ggH_scale_very_highpt_DOWN":CalculateggHStyleWeight_ggH_very_highpt_DOWN,
    "QCDScaleAcceptance_ggH_scale_vbf_UP":CalculateggHStyleWeight_ggH_vbf_UP,
    "QCDScaleAcceptance_ggH_scale_vbf_DOWN":CalculateggHStyleWeight_ggH_vbf_DOWN,
    "QCDScaleAcceptance_ggH_scale_Inclusive_UP":CalculateggHStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_ggH_scale_Inclusive_DOWN":CalculateggHStyleWeight_Inclusive_DOWN,
}
ggHStyleWeight_2017.prepUpAndDownConstants = prepUpAndDownConstants
ggHStyleWeight_2017.prepUpAndDownConstants(ggHStyleWeight_2017)

ggHStyleWeight_2018 = Weight()
ggHStyleWeight_2018.name = 'QCDScaleAcceptance_ggH'
ggHStyleWeight_2018.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/GGHTT2018.root')
ggHStyleWeight_2018.hasUpDownUncertainties = True
ggHStyleWeight_2018.CalculateWeight=CalculateggHStyleWeight
ggHStyleWeight_2018.uncertaintyVariationList = [
    "QCDScaleAcceptance_ggH_scale_0jet_UP",
    "QCDScaleAcceptance_ggH_scale_0jet_DOWN",
    "QCDScaleAcceptance_ggH_scale_1jet_lowpt_UP",
    "QCDScaleAcceptance_ggH_scale_1jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggH_scale_2jet_lowpt_UP",
    "QCDScaleAcceptance_ggH_scale_2jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggH_scale_highpt_UP",
    "QCDScaleAcceptance_ggH_scale_highpt_DOWN",
    "QCDScaleAcceptance_ggH_scale_very_highpt_UP",
    "QCDScaleAcceptance_ggH_scale_very_highpt_DOWN",
    "QCDScaleAcceptance_ggH_scale_vbf_UP",
    "QCDScaleAcceptance_ggH_scale_vbf_DOWN",
    "QCDScaleAcceptance_ggH_scale_Inclusive_UP",
    "QCDScaleAcceptance_ggH_scale_Inclusive_DOWN",
]
ggHStyleWeight_2018.InitUncertaintyVariations()
ggHStyleWeight_2018.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_ggH_scale_0jet_UP":CalculateggHStyleWeight_ggH_0jet_UP,
    "QCDScaleAcceptance_ggH_scale_0jet_DOWN":CalculateggHStyleWeight_ggH_0jet_DOWN,
    "QCDScaleAcceptance_ggH_scale_1jet_lowpt_UP":CalculateggHStyleWeight_ggH_1jet_UP,
    "QCDScaleAcceptance_ggH_scale_1jet_lowpt_DOWN":CalculateggHStyleWeight_ggH_1jet_DOWN,
    "QCDScaleAcceptance_ggH_scale_2jet_lowpt_UP":CalculateggHStyleWeight_ggH_2jet_UP,
    "QCDScaleAcceptance_ggH_scale_2jet_lowpt_DOWN":CalculateggHStyleWeight_ggH_2jet_DOWN,
    "QCDScaleAcceptance_ggH_scale_highpt_UP":CalculateggHStyleWeight_ggH_highpt_UP,
    "QCDScaleAcceptance_ggH_scale_highpt_DOWN":CalculateggHStyleWeight_ggH_highpt_DOWN,
    "QCDScaleAcceptance_ggH_scale_very_highpt_UP":CalculateggHStyleWeight_ggH_very_highpt_UP,
    "QCDScaleAcceptance_ggH_scale_very_highpt_DOWN":CalculateggHStyleWeight_ggH_very_highpt_DOWN,
    "QCDScaleAcceptance_ggH_scale_vbf_UP":CalculateggHStyleWeight_ggH_vbf_UP,
    "QCDScaleAcceptance_ggH_scale_vbf_DOWN":CalculateggHStyleWeight_ggH_vbf_DOWN,
    "QCDScaleAcceptance_ggH_scale_Inclusive_UP":CalculateggHStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_ggH_scale_Inclusive_DOWN":CalculateggHStyleWeight_Inclusive_DOWN,
}
ggHStyleWeight_2018.prepUpAndDownConstants = prepUpAndDownConstants
ggHStyleWeight_2018.prepUpAndDownConstants(ggHStyleWeight_2018)
