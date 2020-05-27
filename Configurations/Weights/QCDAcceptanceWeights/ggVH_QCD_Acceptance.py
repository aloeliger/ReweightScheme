import ROOT
from Configurations.Weights.WeightDefinition import Weight
from Configurations.Weights import localWeightDataPath

def prepUpAndDownConstants(self):
    self.weightHistogram_0jet = self.reweightFile.demo.Get("h_nevents_ggH_scale_0jet")
    try:
        self.constantUP_0jet = self.weightHistogram_0jet.GetBinContent(1)/self.weightHistogram_0jet.GetBinContent(5)
    except ZeroDivisionError:
        self.constantUP_0jet = 0
    try:
        self.constantDOWN_0jet = self.weightHistogram_0jet.GetBinContent(1)/self.weightHistogram_0jet.GetBinContent(9)
    except ZeroDivisionError:
        self.constantDOWN_0jet = 0

    self.weightHistogram_1jet_lowpt = self.reweightFile.demo.Get("h_nevents_ggH_scale_1jet_lowpt")
    try:
        self.constantUP_1jet_lowpt = self.weightHistogram_1jet_lowpt.GetBinContent(1)/self.weightHistogram_1jet_lowpt.GetBinContent(5)
    except ZeroDivisionError:
        self.constantUP_1jet_lowpt = 0
    try:
        self.constantDOWN_1jet_lowpt = self.weightHistogram_1jet_lowpt.GetBinContent(1)/self.weightHistogram_1jet_lowpt.GetBinContent(9)
    except ZeroDivisionError:
        self.constantDOWN_1jet_lowpt = 0
    
    self.weightHistogram_2jet_lowpt = self.reweightFile.demo.Get("h_nevents_ggH_scale_2jet_lowpt")
    try:
        self.constantUP_2jet_lowpt = self.weightHistogram_2jet_lowpt.GetBinContent(1)/self.weightHistogram_2jet_lowpt.GetBinContent(5)
    except ZeroDivisionError:
        self.constantUP_2jet_lowpt = 0
    try:
        self.constantDOWN_2jet_lowpt = self.weightHistogram_2jet_lowpt.GetBinContent(1)/self.weightHistogram_2jet_lowpt.GetBinContent(9)
    except ZeroDivisionError:
        self.constantDOWN_2jet_lowpt = 0
    
    self.weightHistogram_highpt = self.reweightFile.demo.Get("h_nevents_ggH_scale_highpt")
    try:
        self.constantUP_highpt = self.weightHistogram_highpt.GetBinContent(1)/self.weightHistogram_highpt.GetBinContent(5)
    except ZeroDivisionError:
        self.constantUP_highpt = 0
    try:
        self.constantDOWN_highpt = self.weightHistogram_highpt.GetBinContent(1)/self.weightHistogram_highpt.GetBinContent(9)
    except ZeroDivisionError:
        self.constantDOWN_highpt = 0

    self.weightHistogram_very_highpt = self.reweightFile.demo.Get("h_nevents_ggH_scale_very_highpt")
    try:
        self.constantUP_very_highpt = self.weightHistogram_very_highpt.GetBinContent(1)/self.weightHistogram_very_highpt.GetBinContent(5)
    except ZeroDivisionError:
        self.constantUP_very_highpt = 0
    try:
        self.constantDOWN_very_highpt = self.weightHistogram_very_highpt.GetBinContent(1)/self.weightHistogram_very_highpt.GetBinContent(9)
    except ZeroDivisionError:
        self.constantDOWN_very_highpt = 0

    self.weightHistogram_vbf = self.reweightFile.demo.Get("h_nevents_ggH_scale_vbf")
    try:
        self.constantUP_vbf = self.weightHistogram_vbf.GetBinContent(1)/self.weightHistogram_vbf.GetBinContent(5)
    except ZeroDivisionError:
        self.constantUP_vbf = 0
    try:
        self.constantDOWN_vbf = self.weightHistogram_vbf.GetBinContent(1)/self.weightHistogram_vbf.GetBinContent(9)
    except ZeroDivisionError:
        self.constantDOWN_vbf = 0

    self.weightHistogram_lowpt = self.reweightFile.demo.Get("h_nevents_"+self.VHType+"_scale_lowpt")
    try:
        self.constantUP_lowpt = self.weightHistogram_lowpt.GetBinContent(1)/self.weightHistogram_lowpt.GetBinContent(5)
    except ZeroDivisionError:
        self.constantUP_lowpt = 0
    try:
        self.constantDOWN_lowpt = self.weightHistogram_lowpt.GetBinContent(1)/self.weightHistogram_lowpt.GetBinContent(9)
    except ZeroDivisionError:
        self.constantDOWN_lowpt = 0

    self.weightHistogram_highpt = self.reweightFile.demo.Get("h_nevents_"+self.VHType+"_scale_highpt")
    try:
        self.constantUP_highpt = self.weightHistogram_highpt.GetBinContent(1)/self.weightHistogram_highpt.GetBinContent(5)
    except ZeroDivisionError:
        self.constantUP_highpt = 0
    try:
        self.constantDOWN_highpt = self.weightHistogram_highpt.GetBinContent(1)/self.weightHistogram_highpt.GetBinContent(9)
    except ZeroDivisionError:
        self.constantDOWN_highpt = 0
    
    self.weightHistogram_ggH_Inclusive = self.reweightFile.demo.Get("h_nevents_ggH")
    try:
        self.constantUP_ggH_Inclusive = self.weightHistogram_ggH_Inclusive.GetBinContent(1)/self.weightHistogram_ggH_Inclusive.GetBinContent(5)
    except ZeroDivisionError:
        self.constantUP_ggH_Inclusive = 0
    try:
        self.constantDOWN_ggH_Inclusive = self.weightHistogram_ggH_Inclusive.GetBinContent(1)/self.weightHistogram_ggH_Inclusive.GetBinContent(9)
    except ZeroDivisionError:
        self.constantDOWN_ggH_Inclusive = 0

    self.weightHistogram_lep_Inclusive = self.reweightFile.demo.Get("h_nevents_"+self.VHType+"_lep")
    try:
        self.constantUP_lep_Inclusive = self.weightHistogram_lep_Inclusive.GetBinContent(1)/self.weightHistogram_lep_Inclusive.GetBinContent(5)
    except ZeroDivisionError:
        self.constantUP_lep_Inclusive = 0
    try:
        self.constantDOWN_lep_Inclusive = self.weightHistogram_lep_Inclusive.GetBinContent(1)/self.weightHistogram_lep_Inclusive.GetBinContent(9)
    except ZeroDivisionError:
        self.constantDOWN_lep_Inclusive = 0

def CalculateggVHStyleWeight(self,theTree):
    self.value[0] = 1.0

def CalculateggVHStyleWeight_Inclusive_UP(self,theTree,uncert):
    constant = 0
    if (theTree.Rivet_stage1_1_cat_pTjet30GeV < 500):
        constant = self.constantUP_ggH_Inclusive
    else:
        constant = self.constantUP_lep_Inclusive
    self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2 * constant
def CalculateggVHStyleWeight_Inclusive_DOWN(self,theTree,uncert):
    constant = 0
    if (theTree.Rivet_stage1_1_cat_pTjet30GeV < 500):
        constant = self.constantDOWN_ggH_Inclusive
    else:
        constant = self.constantDOWN_lep_Inclusive
    self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5 * constant

def CalculateggVHStyleWeight_ggH_0jet_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 102
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 103):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_0jet
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_ggH_0jet_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 102
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 103):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_0jet
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_ggH_1jet_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 104
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 105
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 106):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_1jet_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_ggH_1jet_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 104
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 105
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 106):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_1jet_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_ggH_2jet_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 107
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 108
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 109):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_2jet_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_ggH_2jet_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 107
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 108
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 109):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_2jet_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_ggH_highpt_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 101 
       and theTree.Rivet_higgsPt > 200 
       and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_ggH_highpt_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 101 
       and theTree.Rivet_higgsPt > 200 
       and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_ggH_very_highpt_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 101 
       and theTree.Rivet_higgsPt > 450):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_very_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_ggH_very_highpt_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 101 
       and theTree.Rivet_higgsPt > 450):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_very_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_ggH_vbf_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 110 
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 111
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 112
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 113):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_vbf
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_ggH_vbf_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 110 
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 111
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 112
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 113):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_vbf
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_VH_lowpt_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 501
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 502
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 503
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 504):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_VH_lowpt_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 501
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 502
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 503
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 504):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_VH_highpt_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 505):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateggVHStyleWeight_VH_highpt_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 505):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

ggZHLLTTStyleWeight_2016 = Weight()
ggZHLLTTStyleWeight_2016.name = 'QCDScaleAcceptance_ggVH'
ggZHLLTTStyleWeight_2016.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/GGZHLLTT2016.root')
ggZHLLTTStyleWeight_2016.hasUpDownUncertainties = True
ggZHLLTTStyleWeight_2016.CalculateWeight=CalculateggVHStyleWeight
ggZHLLTTStyleWeight_2016.uncertaintyVariationList = [
    "QCDScaleAcceptance_ggVH_scale_0jet_UP",
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_vbf_UP",
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN",
]
ggZHLLTTStyleWeight_2016.InitUncertaintyVariations()
ggZHLLTTStyleWeight_2016.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_ggVH_scale_0jet_UP":CalculateggVHStyleWeight_ggH_0jet_UP,
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN":CalculateggVHStyleWeight_ggH_0jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP":CalculateggVHStyleWeight_ggH_1jet_UP,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_1jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP":CalculateggVHStyleWeight_ggH_2jet_UP,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_2jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_highpt_UP":CalculateggVHStyleWeight_ggH_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN":CalculateggVHStyleWeight_ggH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP":CalculateggVHStyleWeight_ggH_very_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN":CalculateggVHStyleWeight_ggH_very_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_vbf_UP":CalculateggVHStyleWeight_ggH_vbf_UP,
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN":CalculateggVHStyleWeight_ggH_vbf_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP":CalculateggVHStyleWeight_VH_lowpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN":CalculateggVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP":CalculateggVHStyleWeight_VH_highpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN":CalculateggVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP":CalculateggVHStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN":CalculateggVHStyleWeight_Inclusive_DOWN,
}
ggZHLLTTStyleWeight_2016.VHType = 'ZH'
ggZHLLTTStyleWeight_2016.prepUpAndDownConstants = prepUpAndDownConstants
ggZHLLTTStyleWeight_2016.prepUpAndDownConstants(ggZHLLTTStyleWeight_2016)

ggZHLLTTStyleWeight_2017 = Weight()
ggZHLLTTStyleWeight_2017.name = 'QCDScaleAcceptance_ggVH'
ggZHLLTTStyleWeight_2017.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/GGZHLLTT2017.root')
ggZHLLTTStyleWeight_2017.hasUpDownUncertainties = True
ggZHLLTTStyleWeight_2017.CalculateWeight=CalculateggVHStyleWeight
ggZHLLTTStyleWeight_2017.uncertaintyVariationList = [
    "QCDScaleAcceptance_ggVH_scale_0jet_UP",
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_vbf_UP",
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN",
]
ggZHLLTTStyleWeight_2017.InitUncertaintyVariations()
ggZHLLTTStyleWeight_2017.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_ggVH_scale_0jet_UP":CalculateggVHStyleWeight_ggH_0jet_UP,
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN":CalculateggVHStyleWeight_ggH_0jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP":CalculateggVHStyleWeight_ggH_1jet_UP,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_1jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP":CalculateggVHStyleWeight_ggH_2jet_UP,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_2jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_highpt_UP":CalculateggVHStyleWeight_ggH_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN":CalculateggVHStyleWeight_ggH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP":CalculateggVHStyleWeight_ggH_very_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN":CalculateggVHStyleWeight_ggH_very_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_vbf_UP":CalculateggVHStyleWeight_ggH_vbf_UP,
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN":CalculateggVHStyleWeight_ggH_vbf_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP":CalculateggVHStyleWeight_VH_lowpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN":CalculateggVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP":CalculateggVHStyleWeight_VH_highpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN":CalculateggVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP":CalculateggVHStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN":CalculateggVHStyleWeight_Inclusive_DOWN,
}
ggZHLLTTStyleWeight_2017.VHType = 'ZH'
ggZHLLTTStyleWeight_2017.prepUpAndDownConstants = prepUpAndDownConstants
ggZHLLTTStyleWeight_2017.prepUpAndDownConstants(ggZHLLTTStyleWeight_2017)

ggZHLLTTStyleWeight_2018 = Weight()
ggZHLLTTStyleWeight_2018.name = 'QCDScaleAcceptance_ggVH'
ggZHLLTTStyleWeight_2018.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/GGZHLLTT2018.root')
ggZHLLTTStyleWeight_2018.hasUpDownUncertainties = True
ggZHLLTTStyleWeight_2018.CalculateWeight=CalculateggVHStyleWeight
ggZHLLTTStyleWeight_2018.uncertaintyVariationList = [
    "QCDScaleAcceptance_ggVH_scale_0jet_UP",
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_vbf_UP",
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN",
]
ggZHLLTTStyleWeight_2018.InitUncertaintyVariations()
ggZHLLTTStyleWeight_2018.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_ggVH_scale_0jet_UP":CalculateggVHStyleWeight_ggH_0jet_UP,
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN":CalculateggVHStyleWeight_ggH_0jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP":CalculateggVHStyleWeight_ggH_1jet_UP,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_1jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP":CalculateggVHStyleWeight_ggH_2jet_UP,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_2jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_highpt_UP":CalculateggVHStyleWeight_ggH_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN":CalculateggVHStyleWeight_ggH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP":CalculateggVHStyleWeight_ggH_very_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN":CalculateggVHStyleWeight_ggH_very_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_vbf_UP":CalculateggVHStyleWeight_ggH_vbf_UP,
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN":CalculateggVHStyleWeight_ggH_vbf_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP":CalculateggVHStyleWeight_VH_lowpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN":CalculateggVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP":CalculateggVHStyleWeight_VH_highpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN":CalculateggVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP":CalculateggVHStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN":CalculateggVHStyleWeight_Inclusive_DOWN,
}
ggZHLLTTStyleWeight_2018.VHType = 'ZH'
ggZHLLTTStyleWeight_2018.prepUpAndDownConstants = prepUpAndDownConstants
ggZHLLTTStyleWeight_2018.prepUpAndDownConstants(ggZHLLTTStyleWeight_2018)

ggZHNNTTStyleWeight_2016 = Weight()
ggZHNNTTStyleWeight_2016.name = 'QCDScaleAcceptance_ggVH'
ggZHNNTTStyleWeight_2016.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/GGZHNNTT2016.root')
ggZHNNTTStyleWeight_2016.hasUpDownUncertainties = True
ggZHNNTTStyleWeight_2016.CalculateWeight=CalculateggVHStyleWeight
ggZHNNTTStyleWeight_2016.uncertaintyVariationList = [
    "QCDScaleAcceptance_ggVH_scale_0jet_UP",
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_vbf_UP",
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN",
]
ggZHNNTTStyleWeight_2016.InitUncertaintyVariations()
ggZHNNTTStyleWeight_2016.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_ggVH_scale_0jet_UP":CalculateggVHStyleWeight_ggH_0jet_UP,
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN":CalculateggVHStyleWeight_ggH_0jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP":CalculateggVHStyleWeight_ggH_1jet_UP,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_1jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP":CalculateggVHStyleWeight_ggH_2jet_UP,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_2jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_highpt_UP":CalculateggVHStyleWeight_ggH_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN":CalculateggVHStyleWeight_ggH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP":CalculateggVHStyleWeight_ggH_very_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN":CalculateggVHStyleWeight_ggH_very_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_vbf_UP":CalculateggVHStyleWeight_ggH_vbf_UP,
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN":CalculateggVHStyleWeight_ggH_vbf_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP":CalculateggVHStyleWeight_VH_lowpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN":CalculateggVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP":CalculateggVHStyleWeight_VH_highpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN":CalculateggVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP":CalculateggVHStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN":CalculateggVHStyleWeight_Inclusive_DOWN,
}
ggZHNNTTStyleWeight_2016.VHType = 'ZH'
ggZHNNTTStyleWeight_2016.prepUpAndDownConstants = prepUpAndDownConstants
ggZHNNTTStyleWeight_2016.prepUpAndDownConstants(ggZHNNTTStyleWeight_2016)

ggZHNNTTStyleWeight_2017 = Weight()
ggZHNNTTStyleWeight_2017.name = 'QCDScaleAcceptance_ggVH'
ggZHNNTTStyleWeight_2017.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/GGZHNNTT2017.root')
ggZHNNTTStyleWeight_2017.hasUpDownUncertainties = True
ggZHNNTTStyleWeight_2017.CalculateWeight=CalculateggVHStyleWeight
ggZHNNTTStyleWeight_2017.uncertaintyVariationList = [
    "QCDScaleAcceptance_ggVH_scale_0jet_UP",
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_vbf_UP",
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN",
]
ggZHNNTTStyleWeight_2017.InitUncertaintyVariations()
ggZHNNTTStyleWeight_2017.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_ggVH_scale_0jet_UP":CalculateggVHStyleWeight_ggH_0jet_UP,
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN":CalculateggVHStyleWeight_ggH_0jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP":CalculateggVHStyleWeight_ggH_1jet_UP,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_1jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP":CalculateggVHStyleWeight_ggH_2jet_UP,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_2jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_highpt_UP":CalculateggVHStyleWeight_ggH_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN":CalculateggVHStyleWeight_ggH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP":CalculateggVHStyleWeight_ggH_very_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN":CalculateggVHStyleWeight_ggH_very_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_vbf_UP":CalculateggVHStyleWeight_ggH_vbf_UP,
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN":CalculateggVHStyleWeight_ggH_vbf_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP":CalculateggVHStyleWeight_VH_lowpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN":CalculateggVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP":CalculateggVHStyleWeight_VH_highpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN":CalculateggVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP":CalculateggVHStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN":CalculateggVHStyleWeight_Inclusive_DOWN,
}
ggZHNNTTStyleWeight_2017.VHType = 'ZH'
ggZHNNTTStyleWeight_2017.prepUpAndDownConstants = prepUpAndDownConstants
ggZHNNTTStyleWeight_2017.prepUpAndDownConstants(ggZHNNTTStyleWeight_2017)

ggZHNNTTStyleWeight_2018 = Weight()
ggZHNNTTStyleWeight_2018.name = 'QCDScaleAcceptance_ggVH'
ggZHNNTTStyleWeight_2018.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/GGZHNNTT2018.root')
ggZHNNTTStyleWeight_2018.hasUpDownUncertainties = True
ggZHNNTTStyleWeight_2018.CalculateWeight=CalculateggVHStyleWeight
ggZHNNTTStyleWeight_2018.uncertaintyVariationList = [
    "QCDScaleAcceptance_ggVH_scale_0jet_UP",
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_vbf_UP",
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN",
]
ggZHNNTTStyleWeight_2018.InitUncertaintyVariations()
ggZHNNTTStyleWeight_2018.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_ggVH_scale_0jet_UP":CalculateggVHStyleWeight_ggH_0jet_UP,
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN":CalculateggVHStyleWeight_ggH_0jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP":CalculateggVHStyleWeight_ggH_1jet_UP,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_1jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP":CalculateggVHStyleWeight_ggH_2jet_UP,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_2jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_highpt_UP":CalculateggVHStyleWeight_ggH_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN":CalculateggVHStyleWeight_ggH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP":CalculateggVHStyleWeight_ggH_very_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN":CalculateggVHStyleWeight_ggH_very_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_vbf_UP":CalculateggVHStyleWeight_ggH_vbf_UP,
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN":CalculateggVHStyleWeight_ggH_vbf_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP":CalculateggVHStyleWeight_VH_lowpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN":CalculateggVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP":CalculateggVHStyleWeight_VH_highpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN":CalculateggVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP":CalculateggVHStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN":CalculateggVHStyleWeight_Inclusive_DOWN,
}
ggZHNNTTStyleWeight_2018.VHType = 'ZH'
ggZHNNTTStyleWeight_2018.prepUpAndDownConstants = prepUpAndDownConstants
ggZHNNTTStyleWeight_2018.prepUpAndDownConstants(ggZHNNTTStyleWeight_2018)

ggZHQQTTStyleWeight_2016 = Weight()
ggZHQQTTStyleWeight_2016.name = 'QCDScaleAcceptance_ggVH'
ggZHQQTTStyleWeight_2016.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/GGZHQQTT2016.root')
ggZHQQTTStyleWeight_2016.hasUpDownUncertainties = True
ggZHQQTTStyleWeight_2016.CalculateWeight=CalculateggVHStyleWeight
ggZHQQTTStyleWeight_2016.uncertaintyVariationList = [
    "QCDScaleAcceptance_ggVH_scale_0jet_UP",
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_vbf_UP",
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN",
]
ggZHQQTTStyleWeight_2016.InitUncertaintyVariations()
ggZHQQTTStyleWeight_2016.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_ggVH_scale_0jet_UP":CalculateggVHStyleWeight_ggH_0jet_UP,
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN":CalculateggVHStyleWeight_ggH_0jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP":CalculateggVHStyleWeight_ggH_1jet_UP,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_1jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP":CalculateggVHStyleWeight_ggH_2jet_UP,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_2jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_highpt_UP":CalculateggVHStyleWeight_ggH_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN":CalculateggVHStyleWeight_ggH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP":CalculateggVHStyleWeight_ggH_very_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN":CalculateggVHStyleWeight_ggH_very_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_vbf_UP":CalculateggVHStyleWeight_ggH_vbf_UP,
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN":CalculateggVHStyleWeight_ggH_vbf_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP":CalculateggVHStyleWeight_VH_lowpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN":CalculateggVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP":CalculateggVHStyleWeight_VH_highpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN":CalculateggVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP":CalculateggVHStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN":CalculateggVHStyleWeight_Inclusive_DOWN,
}
ggZHQQTTStyleWeight_2016.VHType = 'ZH'
ggZHQQTTStyleWeight_2016.prepUpAndDownConstants = prepUpAndDownConstants
ggZHQQTTStyleWeight_2016.prepUpAndDownConstants(ggZHQQTTStyleWeight_2016)

ggZHQQTTStyleWeight_2017 = Weight()
ggZHQQTTStyleWeight_2017.name = 'QCDScaleAcceptance_ggVH'
ggZHQQTTStyleWeight_2017.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/GGZHQQTT2017.root')
ggZHQQTTStyleWeight_2017.hasUpDownUncertainties = True
ggZHQQTTStyleWeight_2017.CalculateWeight=CalculateggVHStyleWeight
ggZHQQTTStyleWeight_2017.uncertaintyVariationList = [
    "QCDScaleAcceptance_ggVH_scale_0jet_UP",
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_vbf_UP",
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN",
]
ggZHQQTTStyleWeight_2017.InitUncertaintyVariations()
ggZHQQTTStyleWeight_2017.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_ggVH_scale_0jet_UP":CalculateggVHStyleWeight_ggH_0jet_UP,
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN":CalculateggVHStyleWeight_ggH_0jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP":CalculateggVHStyleWeight_ggH_1jet_UP,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_1jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP":CalculateggVHStyleWeight_ggH_2jet_UP,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_2jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_highpt_UP":CalculateggVHStyleWeight_ggH_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN":CalculateggVHStyleWeight_ggH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP":CalculateggVHStyleWeight_ggH_very_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN":CalculateggVHStyleWeight_ggH_very_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_vbf_UP":CalculateggVHStyleWeight_ggH_vbf_UP,
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN":CalculateggVHStyleWeight_ggH_vbf_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP":CalculateggVHStyleWeight_VH_lowpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN":CalculateggVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP":CalculateggVHStyleWeight_VH_highpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN":CalculateggVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP":CalculateggVHStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN":CalculateggVHStyleWeight_Inclusive_DOWN,
}
ggZHQQTTStyleWeight_2017.VHType = 'ZH'
ggZHQQTTStyleWeight_2017.prepUpAndDownConstants = prepUpAndDownConstants
ggZHQQTTStyleWeight_2017.prepUpAndDownConstants(ggZHQQTTStyleWeight_2017)

ggZHQQTTStyleWeight_2018 = Weight()
ggZHQQTTStyleWeight_2018.name = 'QCDScaleAcceptance_ggVH'
ggZHQQTTStyleWeight_2018.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/GGZHQQTT2018.root')
ggZHQQTTStyleWeight_2018.hasUpDownUncertainties = True
ggZHQQTTStyleWeight_2018.CalculateWeight=CalculateggVHStyleWeight
ggZHQQTTStyleWeight_2018.uncertaintyVariationList = [
    "QCDScaleAcceptance_ggVH_scale_0jet_UP",
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP",
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP",
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_vbf_UP",
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP",
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP",
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN",
]
ggZHQQTTStyleWeight_2018.InitUncertaintyVariations()
ggZHQQTTStyleWeight_2018.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_ggVH_scale_0jet_UP":CalculateggVHStyleWeight_ggH_0jet_UP,
    "QCDScaleAcceptance_ggVH_scale_0jet_DOWN":CalculateggVHStyleWeight_ggH_0jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP":CalculateggVHStyleWeight_ggH_1jet_UP,
    "QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_1jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_UP":CalculateggVHStyleWeight_ggH_2jet_UP,
    "QCDScaleAcceptance_ggVH_scale_2jet_lowpt_DOWN":CalculateggVHStyleWeight_ggH_2jet_DOWN,
    "QCDScaleAcceptance_ggVH_scale_highpt_UP":CalculateggVHStyleWeight_ggH_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_highpt_DOWN":CalculateggVHStyleWeight_ggH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_UP":CalculateggVHStyleWeight_ggH_very_highpt_UP,
    "QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN":CalculateggVHStyleWeight_ggH_very_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_vbf_UP":CalculateggVHStyleWeight_ggH_vbf_UP,
    "QCDScaleAcceptance_ggVH_scale_vbf_DOWN":CalculateggVHStyleWeight_ggH_vbf_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_UP":CalculateggVHStyleWeight_VH_lowpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN":CalculateggVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_UP":CalculateggVHStyleWeight_VH_highpt_UP,
    "QCDScaleacceptance_ggVH_scale_VH_highpt_DOWN":CalculateggVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_UP":CalculateggVHStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN":CalculateggVHStyleWeight_Inclusive_DOWN,
}
ggZHQQTTStyleWeight_2018.VHType = 'ZH'
ggZHQQTTStyleWeight_2018.prepUpAndDownConstants = prepUpAndDownConstants
ggZHQQTTStyleWeight_2018.prepUpAndDownConstants(ggZHQQTTStyleWeight_2018)

