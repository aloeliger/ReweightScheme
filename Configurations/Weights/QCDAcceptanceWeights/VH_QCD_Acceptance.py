import ROOT
from Configurations.Weights.WeightDefinition import Weight
from Configurations.Weights import localWeightDataPath

def prepUpAndDownConstants(self):
    self.weightHistogram_0jet = self.reweightFile.demo.Get("h_nevents_vbf_scale_0jet")
    self.constantUP_0jet = self.weightHistogram_0jet.GetBinContent(1)/self.weightHistogram_0jet.GetBinContent(5)
    self.constantDOWN_0jet = self.weightHistogram_0jet.GetBinContent(1)/self.weightHistogram_0jet.GetBinContent(9)

    self.weightHistogram_1jet = self.reweightFile.demo.Get("h_nevents_vbf_scale_1jet")
    self.constantUP_1jet = self.weightHistogram_1jet.GetBinContent(1)/self.weightHistogram_1jet.GetBinContent(5)
    self.constantDOWN_1jet = self.weightHistogram_1jet.GetBinContent(1)/self.weightHistogram_1jet.GetBinContent(9)

    self.weightHistogram_lowmjj = self.reweightFile.demo.Get("h_nevents_vbf_scale_lowmjj")
    self.constantUP_lowmjj = self.weightHistogram_lowmjj.GetBinContent(1)/self.weightHistogram_lowmjj.GetBinContent(5)
    self.constantDOWN_lowmjj = self.weightHistogram_lowmjj.GetBinContent(1)/self.weightHistogram_lowmjj.GetBinContent(9)

    self.weightHistogram_highmjj_lowpt = self.reweightFile.demo.Get("h_nevents_vbf_scale_highmjj_lowpt")
    self.constantUP_highmjj_lowpt = self.weightHistogram_highmjj_lowpt.GetBinContent(1)/self.weightHistogram_highmjj_lowpt.GetBinContent(5)
    self.constantDOWN_highmjj_lowpt = self.weightHistogram_highmjj_lowpt.GetBinContent(1)/self.weightHistogram_highmjj_lowpt.GetBinContent(9)

    self.weightHistogram_highmjj_highpt = self.reweightFile.demo.Get("h_nevents_vbf_scale_highmjj_highpt")
    self.constantUP_highmjj_highpt = self.weightHistogram_highmjj_highpt.GetBinContent(1)/self.weightHistogram_highmjj_highpt.GetBinContent(5)
    self.constantDOWN_highmjj_highpt = self.weightHistogram_highmjj_highpt.GetBinContent(1)/self.weightHistogram_highmjj_highpt.GetBinContent(9)

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
        
    self.weightHistogram_lep_Inclusive = self.reweightFile.demo.Get("h_nevents_"+self.VHType+"_lep")
    try:
        self.constantUP_lep_Inclusive = self.weightHistogram_lep_Inclusive.GetBinContent(1)/self.weightHistogram_lep_Inclusive.GetBinContent(5)
    except ZeroDivisionError:
        self.constantUP_lep_Inclusive = 0
    try:
        self.constantDOWN_lep_Inclusive = self.weightHistogram_lep_Inclusive.GetBinContent(1)/self.weightHistogram_lep_Inclusive.GetBinContent(9)
    except ZeroDivisionError:
        self.constantDOWN_lep_Inclusive = 0
        
    self.weightHistogram_vbf_Inclusive = self.reweightFile.demo.Get("h_nevents_vbf")
    try:
        self.constantUP_vbf_Inclusive = self.weightHistogram_vbf_Inclusive.GetBinContent(1)/self.weightHistogram_vbf_Inclusive.GetBinContent(5)
    except ZeroDivisionError:
        self.constantUP_vbf_Inclusive = 0
    try:
        self.constantDOWN_vbf_Inclusive = self.weightHistogram_vbf_Inclusive.GetBinContent(1)/self.weightHistogram_vbf_Inclusive.GetBinContent(9)
    except ZeroDivisionError:
        self.constantDOWN_vbf_Inclusive = 0

def CalculateVHStyleWeight(self,theTree):
    self.value[0] = 1.0

def CalculateVHStyleWeight_Inclusive_UP(self,theTree,uncert):
    constant = 0
    if (theTree.Rivet_stage1_1_cat_pTjet30GeV < 400):
        constant = self.constantUP_vbf_Inclusive
    else:
        constant = self.constantUP_lep_Inclusive

    self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2 * constant

def CalculateVHStyleWeight_Inclusive_DOWN(self,theTree,uncert):
    constant = 0
    if (theTree.Rivet_stage1_1_cat_pTjet30GeV < 400):
        constant = self.constantDOWN_vbf_Inclusive
    else:
        constant = self.constantDOWN_lep_Inclusive
    self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5 * constant

def CalculateVHStyleWeight_vbf_0jet_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 201):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_0jet
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_vbf_0jet_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 201):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_0jet
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_vbf_1jet_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 202):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_1jet
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_vbf_1jet_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 202):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_1jet
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_vbf_lowmjj_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 203
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 204
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 205):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_lowmjj
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_vbf_lowmjj_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 203
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 204
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 205):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_lowmjj
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_vbf_highmjj_lowpt_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 207
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 208
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 209
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 210):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_highmjj_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_vbf_highmjj_lowpt_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 207
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 208
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 209
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 210):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_highmjj_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_vbf_highmjj_highpt_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 206):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_highmjj_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_vbf_highmjj_highpt_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 206):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_highmjj_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_VH_lowpt_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 401
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 402
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 403
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 404):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_VH_lowpt_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 401
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 402
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 403
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 404):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_highmjj_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_VH_highpt_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 405):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVHStyleWeight_VH_highpt_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 405):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_highmjj_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

WminusHStyleWeight_2016 = Weight()
WminusHStyleWeight_2016.name = 'QCDScaleAcceptance_VH'
WminusHStyleWeight_2016.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/WminusHTT2016.root')
WminusHStyleWeight_2016.hasUpDownUncertainties = True
WminusHStyleWeight_2016.CalculateWeight=CalculateVHStyleWeight
WminusHStyleWeight_2016.uncertaintyVariationList = [
    "QCDScaleAcceptance_VH_scale_0jet_UP",
    "QCDScaleAcceptance_VH_scale_0jet_DOWN",
    "QCDScaleAcceptance_VH_scale_1jet_UP",
    "QCDScaleAcceptance_VH_scale_1jet_DOWN",
    "QCDScaleAcceptance_VH_scale_lowmjj_UP",
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_Inclusive_UP",
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN",
]
WminusHStyleWeight_2016.InitUncertaintyVariations()
WminusHStyleWeight_2016.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_VH_scale_0jet_UP":CalculateVHStyleWeight_vbf_0jet_UP,
    "QCDScaleAcceptance_VH_scale_0jet_DOWN":CalculateVHStyleWeight_vbf_0jet_DOWN,
    "QCDScaleAcceptance_VH_scale_1jet_UP":CalculateVHStyleWeight_vbf_1jet_UP,
    "QCDScaleAcceptance_VH_scale_1jet_DOWN":CalculateVHStyleWeight_vbf_1jet_DOWN,
    "QCDScaleAcceptance_VH_scale_lowmjj_UP":CalculateVHStyleWeight_vbf_lowmjj_UP,
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN":CalculateVHStyleWeight_vbf_lowmjj_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP":CalculateVHStyleWeight_vbf_highmjj_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP":CalculateVHStyleWeight_vbf_highmjj_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_lowpt_UP":CalculateVHStyleWeight_VH_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN":CalculateVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highpt_UP":CalculateVHStyleWeight_VH_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highpt_DOWN":CalculateVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_Inclusive_UP":CalculateVHStyleWeight_Inclusive_UP,
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN":CalculateVHStyleWeight_Inclusive_DOWN,
}
WminusHStyleWeight_2016.VHType='WH'
WminusHStyleWeight_2016.prepUpAndDownConstants = prepUpAndDownConstants
WminusHStyleWeight_2016.prepUpAndDownConstants(WminusHStyleWeight_2016)

WminusHStyleWeight_2017 = Weight()
WminusHStyleWeight_2017.name = 'QCDScaleAcceptance_VH'
WminusHStyleWeight_2017.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/WminusHTT2017.root')
WminusHStyleWeight_2017.hasUpDownUncertainties = True
WminusHStyleWeight_2017.CalculateWeight=CalculateVHStyleWeight
WminusHStyleWeight_2017.uncertaintyVariationList = [
    "QCDScaleAcceptance_VH_scale_0jet_UP",
    "QCDScaleAcceptance_VH_scale_0jet_DOWN",
    "QCDScaleAcceptance_VH_scale_1jet_UP",
    "QCDScaleAcceptance_VH_scale_1jet_DOWN",
    "QCDScaleAcceptance_VH_scale_lowmjj_UP",
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_Inclusive_UP",
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN",
]
WminusHStyleWeight_2017.InitUncertaintyVariations()
WminusHStyleWeight_2017.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_VH_scale_0jet_UP":CalculateVHStyleWeight_vbf_0jet_UP,
    "QCDScaleAcceptance_VH_scale_0jet_DOWN":CalculateVHStyleWeight_vbf_0jet_DOWN,
    "QCDScaleAcceptance_VH_scale_1jet_UP":CalculateVHStyleWeight_vbf_1jet_UP,
    "QCDScaleAcceptance_VH_scale_1jet_DOWN":CalculateVHStyleWeight_vbf_1jet_DOWN,
    "QCDScaleAcceptance_VH_scale_lowmjj_UP":CalculateVHStyleWeight_vbf_lowmjj_UP,
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN":CalculateVHStyleWeight_vbf_lowmjj_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP":CalculateVHStyleWeight_vbf_highmjj_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP":CalculateVHStyleWeight_vbf_highmjj_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_lowpt_UP":CalculateVHStyleWeight_VH_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN":CalculateVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highpt_UP":CalculateVHStyleWeight_VH_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highpt_DOWN":CalculateVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_Inclusive_UP":CalculateVHStyleWeight_Inclusive_UP,
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN":CalculateVHStyleWeight_Inclusive_DOWN,
}
WminusHStyleWeight_2017.VHType='WH'
WminusHStyleWeight_2017.prepUpAndDownConstants = prepUpAndDownConstants
WminusHStyleWeight_2017.prepUpAndDownConstants(WminusHStyleWeight_2017)

WminusHStyleWeight_2018 = Weight()
WminusHStyleWeight_2018.name = 'QCDScaleAcceptance_VH'
WminusHStyleWeight_2018.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/WminusHTT2018.root')
WminusHStyleWeight_2018.hasUpDownUncertainties = True
WminusHStyleWeight_2018.CalculateWeight=CalculateVHStyleWeight
WminusHStyleWeight_2018.uncertaintyVariationList = [
    "QCDScaleAcceptance_VH_scale_0jet_UP",
    "QCDScaleAcceptance_VH_scale_0jet_DOWN",
    "QCDScaleAcceptance_VH_scale_1jet_UP",
    "QCDScaleAcceptance_VH_scale_1jet_DOWN",
    "QCDScaleAcceptance_VH_scale_lowmjj_UP",
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_Inclusive_UP",
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN",
]
WminusHStyleWeight_2018.InitUncertaintyVariations()
WminusHStyleWeight_2018.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_VH_scale_0jet_UP":CalculateVHStyleWeight_vbf_0jet_UP,
    "QCDScaleAcceptance_VH_scale_0jet_DOWN":CalculateVHStyleWeight_vbf_0jet_DOWN,
    "QCDScaleAcceptance_VH_scale_1jet_UP":CalculateVHStyleWeight_vbf_1jet_UP,
    "QCDScaleAcceptance_VH_scale_1jet_DOWN":CalculateVHStyleWeight_vbf_1jet_DOWN,
    "QCDScaleAcceptance_VH_scale_lowmjj_UP":CalculateVHStyleWeight_vbf_lowmjj_UP,
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN":CalculateVHStyleWeight_vbf_lowmjj_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP":CalculateVHStyleWeight_vbf_highmjj_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP":CalculateVHStyleWeight_vbf_highmjj_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_lowpt_UP":CalculateVHStyleWeight_VH_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN":CalculateVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highpt_UP":CalculateVHStyleWeight_VH_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highpt_DOWN":CalculateVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_Inclusive_UP":CalculateVHStyleWeight_Inclusive_UP,
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN":CalculateVHStyleWeight_Inclusive_DOWN,
}
WminusHStyleWeight_2018.VHType='WH'
WminusHStyleWeight_2018.prepUpAndDownConstants = prepUpAndDownConstants
WminusHStyleWeight_2018.prepUpAndDownConstants(WminusHStyleWeight_2018)

WplusHStyleWeight_2016 = Weight()
WplusHStyleWeight_2016.name = 'QCDScaleAcceptance_VH'
WplusHStyleWeight_2016.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/WplusHTT2016.root')
WplusHStyleWeight_2016.hasUpDownUncertainties = True
WplusHStyleWeight_2016.CalculateWeight=CalculateVHStyleWeight
WplusHStyleWeight_2016.uncertaintyVariationList = [
    "QCDScaleAcceptance_VH_scale_0jet_UP",
    "QCDScaleAcceptance_VH_scale_0jet_DOWN",
    "QCDScaleAcceptance_VH_scale_1jet_UP",
    "QCDScaleAcceptance_VH_scale_1jet_DOWN",
    "QCDScaleAcceptance_VH_scale_lowmjj_UP",
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_Inclusive_UP",
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN",
]
WplusHStyleWeight_2016.InitUncertaintyVariations()
WplusHStyleWeight_2016.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_VH_scale_0jet_UP":CalculateVHStyleWeight_vbf_0jet_UP,
    "QCDScaleAcceptance_VH_scale_0jet_DOWN":CalculateVHStyleWeight_vbf_0jet_DOWN,
    "QCDScaleAcceptance_VH_scale_1jet_UP":CalculateVHStyleWeight_vbf_1jet_UP,
    "QCDScaleAcceptance_VH_scale_1jet_DOWN":CalculateVHStyleWeight_vbf_1jet_DOWN,
    "QCDScaleAcceptance_VH_scale_lowmjj_UP":CalculateVHStyleWeight_vbf_lowmjj_UP,
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN":CalculateVHStyleWeight_vbf_lowmjj_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP":CalculateVHStyleWeight_vbf_highmjj_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP":CalculateVHStyleWeight_vbf_highmjj_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_lowpt_UP":CalculateVHStyleWeight_VH_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN":CalculateVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highpt_UP":CalculateVHStyleWeight_VH_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highpt_DOWN":CalculateVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_Inclusive_UP":CalculateVHStyleWeight_Inclusive_UP,
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN":CalculateVHStyleWeight_Inclusive_DOWN,
}
WplusHStyleWeight_2016.VHType='WH'
WplusHStyleWeight_2016.prepUpAndDownConstants = prepUpAndDownConstants
WplusHStyleWeight_2016.prepUpAndDownConstants(WplusHStyleWeight_2016)

WplusHStyleWeight_2017 = Weight()
WplusHStyleWeight_2017.name = 'QCDScaleAcceptance_VH'
WplusHStyleWeight_2017.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/WplusHTT2017.root')
WplusHStyleWeight_2017.hasUpDownUncertainties = True
WplusHStyleWeight_2017.CalculateWeight=CalculateVHStyleWeight
WplusHStyleWeight_2017.uncertaintyVariationList = [
    "QCDScaleAcceptance_VH_scale_0jet_UP",
    "QCDScaleAcceptance_VH_scale_0jet_DOWN",
    "QCDScaleAcceptance_VH_scale_1jet_UP",
    "QCDScaleAcceptance_VH_scale_1jet_DOWN",
    "QCDScaleAcceptance_VH_scale_lowmjj_UP",
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_Inclusive_UP",
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN",
]
WplusHStyleWeight_2017.InitUncertaintyVariations()
WplusHStyleWeight_2017.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_VH_scale_0jet_UP":CalculateVHStyleWeight_vbf_0jet_UP,
    "QCDScaleAcceptance_VH_scale_0jet_DOWN":CalculateVHStyleWeight_vbf_0jet_DOWN,
    "QCDScaleAcceptance_VH_scale_1jet_UP":CalculateVHStyleWeight_vbf_1jet_UP,
    "QCDScaleAcceptance_VH_scale_1jet_DOWN":CalculateVHStyleWeight_vbf_1jet_DOWN,
    "QCDScaleAcceptance_VH_scale_lowmjj_UP":CalculateVHStyleWeight_vbf_lowmjj_UP,
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN":CalculateVHStyleWeight_vbf_lowmjj_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP":CalculateVHStyleWeight_vbf_highmjj_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP":CalculateVHStyleWeight_vbf_highmjj_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_lowpt_UP":CalculateVHStyleWeight_VH_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN":CalculateVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highpt_UP":CalculateVHStyleWeight_VH_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highpt_DOWN":CalculateVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_Inclusive_UP":CalculateVHStyleWeight_Inclusive_UP,
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN":CalculateVHStyleWeight_Inclusive_DOWN,
}
WplusHStyleWeight_2017.VHType='WH'
WplusHStyleWeight_2017.prepUpAndDownConstants = prepUpAndDownConstants
WplusHStyleWeight_2017.prepUpAndDownConstants(WplusHStyleWeight_2017)

WplusHStyleWeight_2018 = Weight()
WplusHStyleWeight_2018.name = 'QCDScaleAcceptance_VH'
WplusHStyleWeight_2018.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/WplusHTT2018.root')
WplusHStyleWeight_2018.hasUpDownUncertainties = True
WplusHStyleWeight_2018.CalculateWeight=CalculateVHStyleWeight
WplusHStyleWeight_2018.uncertaintyVariationList = [
    "QCDScaleAcceptance_VH_scale_0jet_UP",
    "QCDScaleAcceptance_VH_scale_0jet_DOWN",
    "QCDScaleAcceptance_VH_scale_1jet_UP",
    "QCDScaleAcceptance_VH_scale_1jet_DOWN",
    "QCDScaleAcceptance_VH_scale_lowmjj_UP",
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_Inclusive_UP",
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN",
]
WplusHStyleWeight_2018.InitUncertaintyVariations()
WplusHStyleWeight_2018.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_VH_scale_0jet_UP":CalculateVHStyleWeight_vbf_0jet_UP,
    "QCDScaleAcceptance_VH_scale_0jet_DOWN":CalculateVHStyleWeight_vbf_0jet_DOWN,
    "QCDScaleAcceptance_VH_scale_1jet_UP":CalculateVHStyleWeight_vbf_1jet_UP,
    "QCDScaleAcceptance_VH_scale_1jet_DOWN":CalculateVHStyleWeight_vbf_1jet_DOWN,
    "QCDScaleAcceptance_VH_scale_lowmjj_UP":CalculateVHStyleWeight_vbf_lowmjj_UP,
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN":CalculateVHStyleWeight_vbf_lowmjj_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP":CalculateVHStyleWeight_vbf_highmjj_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP":CalculateVHStyleWeight_vbf_highmjj_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_lowpt_UP":CalculateVHStyleWeight_VH_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN":CalculateVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highpt_UP":CalculateVHStyleWeight_VH_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highpt_DOWN":CalculateVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_Inclusive_UP":CalculateVHStyleWeight_Inclusive_UP,
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN":CalculateVHStyleWeight_Inclusive_DOWN,
}
WplusHStyleWeight_2018.VHType='WH'
WplusHStyleWeight_2018.prepUpAndDownConstants = prepUpAndDownConstants
WplusHStyleWeight_2018.prepUpAndDownConstants(WplusHStyleWeight_2018)

ZHStyleWeight_2016 = Weight()
ZHStyleWeight_2016.name = 'QCDScaleAcceptance_VH'
ZHStyleWeight_2016.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/ZHTT2016.root')
ZHStyleWeight_2016.hasUpDownUncertainties = True
ZHStyleWeight_2016.CalculateWeight=CalculateVHStyleWeight
ZHStyleWeight_2016.uncertaintyVariationList = [
    "QCDScaleAcceptance_VH_scale_0jet_UP",
    "QCDScaleAcceptance_VH_scale_0jet_DOWN",
    "QCDScaleAcceptance_VH_scale_1jet_UP",
    "QCDScaleAcceptance_VH_scale_1jet_DOWN",
    "QCDScaleAcceptance_VH_scale_lowmjj_UP",
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_Inclusive_UP",
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN",
]
ZHStyleWeight_2016.InitUncertaintyVariations()
ZHStyleWeight_2016.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_VH_scale_0jet_UP":CalculateVHStyleWeight_vbf_0jet_UP,
    "QCDScaleAcceptance_VH_scale_0jet_DOWN":CalculateVHStyleWeight_vbf_0jet_DOWN,
    "QCDScaleAcceptance_VH_scale_1jet_UP":CalculateVHStyleWeight_vbf_1jet_UP,
    "QCDScaleAcceptance_VH_scale_1jet_DOWN":CalculateVHStyleWeight_vbf_1jet_DOWN,
    "QCDScaleAcceptance_VH_scale_lowmjj_UP":CalculateVHStyleWeight_vbf_lowmjj_UP,
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN":CalculateVHStyleWeight_vbf_lowmjj_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP":CalculateVHStyleWeight_vbf_highmjj_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP":CalculateVHStyleWeight_vbf_highmjj_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_lowpt_UP":CalculateVHStyleWeight_VH_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN":CalculateVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highpt_UP":CalculateVHStyleWeight_VH_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highpt_DOWN":CalculateVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_Inclusive_UP":CalculateVHStyleWeight_Inclusive_UP,
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN":CalculateVHStyleWeight_Inclusive_DOWN,
}
ZHStyleWeight_2016.VHType='ZH'
ZHStyleWeight_2016.prepUpAndDownConstants = prepUpAndDownConstants
ZHStyleWeight_2016.prepUpAndDownConstants(ZHStyleWeight_2016)

ZHStyleWeight_2017 = Weight()
ZHStyleWeight_2017.name = 'QCDScaleAcceptance_VH'
ZHStyleWeight_2017.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/ZHTT2017.root')
ZHStyleWeight_2017.hasUpDownUncertainties = True
ZHStyleWeight_2017.CalculateWeight=CalculateVHStyleWeight
ZHStyleWeight_2017.uncertaintyVariationList = [
    "QCDScaleAcceptance_VH_scale_0jet_UP",
    "QCDScaleAcceptance_VH_scale_0jet_DOWN",
    "QCDScaleAcceptance_VH_scale_1jet_UP",
    "QCDScaleAcceptance_VH_scale_1jet_DOWN",
    "QCDScaleAcceptance_VH_scale_lowmjj_UP",
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_Inclusive_UP",
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN",
]
ZHStyleWeight_2017.InitUncertaintyVariations()
ZHStyleWeight_2017.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_VH_scale_0jet_UP":CalculateVHStyleWeight_vbf_0jet_UP,
    "QCDScaleAcceptance_VH_scale_0jet_DOWN":CalculateVHStyleWeight_vbf_0jet_DOWN,
    "QCDScaleAcceptance_VH_scale_1jet_UP":CalculateVHStyleWeight_vbf_1jet_UP,
    "QCDScaleAcceptance_VH_scale_1jet_DOWN":CalculateVHStyleWeight_vbf_1jet_DOWN,
    "QCDScaleAcceptance_VH_scale_lowmjj_UP":CalculateVHStyleWeight_vbf_lowmjj_UP,
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN":CalculateVHStyleWeight_vbf_lowmjj_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP":CalculateVHStyleWeight_vbf_highmjj_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP":CalculateVHStyleWeight_vbf_highmjj_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_lowpt_UP":CalculateVHStyleWeight_VH_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN":CalculateVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highpt_UP":CalculateVHStyleWeight_VH_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highpt_DOWN":CalculateVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_Inclusive_UP":CalculateVHStyleWeight_Inclusive_UP,
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN":CalculateVHStyleWeight_Inclusive_DOWN,
}
ZHStyleWeight_2017.VHType='ZH'
ZHStyleWeight_2017.prepUpAndDownConstants = prepUpAndDownConstants
ZHStyleWeight_2017.prepUpAndDownConstants(ZHStyleWeight_2017)

ZHStyleWeight_2018 = Weight()
ZHStyleWeight_2018.name = 'QCDScaleAcceptance_VH'
ZHStyleWeight_2018.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/ZHTT2018.root')
ZHStyleWeight_2018.hasUpDownUncertainties = True
ZHStyleWeight_2018.CalculateWeight=CalculateVHStyleWeight
ZHStyleWeight_2018.uncertaintyVariationList = [
    "QCDScaleAcceptance_VH_scale_0jet_UP",
    "QCDScaleAcceptance_VH_scale_0jet_DOWN",
    "QCDScaleAcceptance_VH_scale_1jet_UP",
    "QCDScaleAcceptance_VH_scale_1jet_DOWN",
    "QCDScaleAcceptance_VH_scale_lowmjj_UP",
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_lowpt_UP",
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN",
    "QCDScaleAcceptance_VH_scale_highpt_UP",
    "QCDScaleAcceptance_VH_scale_highpt_DOWN",
    "QCDScaleAcceptance_VH_scale_Inclusive_UP",
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN",
]
ZHStyleWeight_2018.InitUncertaintyVariations()
ZHStyleWeight_2018.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_VH_scale_0jet_UP":CalculateVHStyleWeight_vbf_0jet_UP,
    "QCDScaleAcceptance_VH_scale_0jet_DOWN":CalculateVHStyleWeight_vbf_0jet_DOWN,
    "QCDScaleAcceptance_VH_scale_1jet_UP":CalculateVHStyleWeight_vbf_1jet_UP,
    "QCDScaleAcceptance_VH_scale_1jet_DOWN":CalculateVHStyleWeight_vbf_1jet_DOWN,
    "QCDScaleAcceptance_VH_scale_lowmjj_UP":CalculateVHStyleWeight_vbf_lowmjj_UP,
    "QCDScaleAcceptance_VH_scale_lowmjj_DOWN":CalculateVHStyleWeight_vbf_lowmjj_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP":CalculateVHStyleWeight_vbf_highmjj_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_UP":CalculateVHStyleWeight_vbf_highmjj_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN":CalculateVHStyleWeight_vbf_highmjj_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_lowpt_UP":CalculateVHStyleWeight_VH_lowpt_UP,
    "QCDScaleAcceptance_VH_scale_lowpt_DOWN":CalculateVHStyleWeight_VH_lowpt_DOWN,
    "QCDScaleAcceptance_VH_scale_highpt_UP":CalculateVHStyleWeight_VH_highpt_UP,
    "QCDScaleAcceptance_VH_scale_highpt_DOWN":CalculateVHStyleWeight_VH_highpt_DOWN,
    "QCDScaleAcceptance_VH_scale_Inclusive_UP":CalculateVHStyleWeight_Inclusive_UP,
    "QCDScaleacceptance_VH_scale_Inclusive_DOWN":CalculateVHStyleWeight_Inclusive_DOWN,
}
ZHStyleWeight_2018.VHType='ZH'
ZHStyleWeight_2018.prepUpAndDownConstants = prepUpAndDownConstants
ZHStyleWeight_2018.prepUpAndDownConstants(ZHStyleWeight_2018)
