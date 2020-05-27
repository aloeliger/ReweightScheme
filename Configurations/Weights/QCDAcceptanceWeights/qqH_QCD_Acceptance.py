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

    self.weightHistogram_vbf_Inclusive = self.reweightFile.demo.Get("h_nevents_vbf")
    self.constantUP_Inclusive = self.weightHistogram_vbf_Inclusive.GetBinContent(1)/self.weightHistogram_vbf_Inclusive.GetBinContent(5)
    self.constantDOWN_Inclusive = self.weightHistogram_vbf_Inclusive.GetBinContent(1)/self.weightHistogram_vbf_Inclusive.GetBinContent(9)

def CalculateVBFStyleWeight(self,theTree):
    self.value[0] = 1.0

def CalculateVBFStyleWeight_Inclusive_UP(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2 * self.constantUP_Inclusive

def CalculateVBFStyleWeight_Inclusive_DOWN(self,theTree,uncert):
    self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5 * self.constantDOWN_Inclusive

def CalculateVBFStyleWeight_vbf_0jet_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 201):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_0jet
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVBFStyleWeight_vbf_0jet_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 201):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_0jet
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVBFStyleWeight_vbf_1jet_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 202):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_1jet
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVBFStyleWeight_vbf_1jet_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 202):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_1jet
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVBFStyleWeight_vbf_lowmjj_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 203
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 204
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 205):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_lowmjj
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVBFStyleWeight_vbf_lowmjj_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 203
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 204
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 205):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_lowmjj
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVBFStyleWeight_vbf_highmjj_lowpt_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 207
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 208
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 209
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 210):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_highmjj_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVBFStyleWeight_vbf_highmjj_lowpt_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 207
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 208
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 209
       or theTree.Rivet_stage1_1_cat_pTjet30GeV == 210):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_highmjj_lowpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVBFStyleWeight_vbf_highmjj_highpt_UP(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 206):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR2_muF2*self.constantUP_highmjj_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

def CalculateVBFStyleWeight_vbf_highmjj_highpt_DOWN(self,theTree,uncert):    
    if(theTree.Rivet_stage1_1_cat_pTjet30GeV == 206):
        self.uncertaintyVariationArrays[uncert][0] = theTree.lheweight_muR0p5_muF0p5*self.constantDOWN_highmjj_highpt
    else:
        self.uncertaintyVariationArrays[uncert][0] = 1.0

VBFStyleWeight_2016 = Weight()
VBFStyleWeight_2016.name = 'QCDScaleAcceptance_VBF'
VBFStyleWeight_2016.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/VBFHTT2016.root')
VBFStyleWeight_2016.hasUpDownUncertainties = True
VBFStyleWeight_2016.CalculateWeight=CalculateVBFStyleWeight
VBFStyleWeight_2016.uncertaintyVariationList = [
    "QCDScaleAcceptance_VBF_scale_0jet_UP",
    "QCDScaleAcceptance_VBF_scale_0jet_DOWN",
    "QCDScaleAcceptance_VBF_scale_1jet_UP",
    "QCDScaleAcceptance_VBF_scale_1jet_DOWN",
    "QCDScaleAcceptance_VBF_scale_lowmjj_UP",
    "QCDScaleAcceptance_VBF_scale_lowmjj_DOWN",
    "QCDScaleAcceptance_VBF_scale_highmjj_lowpt_UP",
    "QCDScaleAcceptance_VBF_scale_highmjj_lowpt_DOWN",
    "QCDScaleAcceptance_VBF_scale_highmjj_highpt_UP",
    "QCDScaleAcceptance_VBF_scale_highmjj_highpt_DOWN",
    "QCDScaleAcceptance_VBF_scale_Inclusive_UP",
    "QCDScaleAcceptance_VBF_scale_Inclusive_DOWN",
]
VBFStyleWeight_2016.InitUncertaintyVariations()
VBFStyleWeight_2016.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_VBF_scale_0jet_UP":CalculateVBFStyleWeight_vbf_0jet_UP,
    "QCDScaleAcceptance_VBF_scale_0jet_DOWN":CalculateVBFStyleWeight_vbf_0jet_DOWN,
    "QCDScaleAcceptance_VBF_scale_1jet_UP":CalculateVBFStyleWeight_vbf_1jet_UP,
    "QCDScaleAcceptance_VBF_scale_1jet_DOWN":CalculateVBFStyleWeight_vbf_1jet_DOWN,
    "QCDScaleAcceptance_VBF_scale_lowmjj_UP":CalculateVBFStyleWeight_vbf_lowmjj_UP,
    "QCDScaleAcceptance_VBF_scale_lowmjj_DOWN":CalculateVBFStyleWeight_vbf_lowmjj_DOWN,
    "QCDScaleAcceptance_VBF_scale_highmjj_lowpt_UP":CalculateVBFStyleWeight_vbf_highmjj_lowpt_UP,
    "QCDScaleAcceptance_VBF_scale_highmjj_lowpt_DOWN":CalculateVBFStyleWeight_vbf_highmjj_lowpt_DOWN,
    "QCDScaleAcceptance_VBF_scale_highmjj_highpt_UP":CalculateVBFStyleWeight_vbf_highmjj_highpt_UP,
    "QCDScaleAcceptance_VBF_scale_highmjj_highpt_DOWN":CalculateVBFStyleWeight_vbf_highmjj_highpt_DOWN,
    "QCDScaleAcceptance_VBF_scale_Inclusive_UP":CalculateVBFStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_VBF_scale_Inclusive_DOWN":CalculateVBFStyleWeight_Inclusive_DOWN,
}
VBFStyleWeight_2016.prepUpAndDownConstants = prepUpAndDownConstants
VBFStyleWeight_2016.prepUpAndDownConstants(VBFStyleWeight_2016)

VBFStyleWeight_2017 = Weight()
VBFStyleWeight_2017.name = 'QCDScaleAcceptance_VBF'
VBFStyleWeight_2017.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/VBFHTT2017.root')
VBFStyleWeight_2017.hasUpDownUncertainties = True
VBFStyleWeight_2017.CalculateWeight=CalculateVBFStyleWeight
VBFStyleWeight_2017.uncertaintyVariationList = [
    "QCDScaleAcceptance_VBF_scale_0jet_UP",
    "QCDScaleAcceptance_VBF_scale_0jet_DOWN",
    "QCDScaleAcceptance_VBF_scale_1jet_UP",
    "QCDScaleAcceptance_VBF_scale_1jet_DOWN",
    "QCDScaleAcceptance_VBF_scale_lowmjj_UP",
    "QCDScaleAcceptance_VBF_scale_lowmjj_DOWN",
    "QCDScaleAcceptance_VBF_scale_highmjj_lowpt_UP",
    "QCDScaleAcceptance_VBF_scale_highmjj_lowpt_DOWN",
    "QCDScaleAcceptance_VBF_scale_highmjj_highpt_UP",
    "QCDScaleAcceptance_VBF_scale_highmjj_highpt_DOWN",
    "QCDScaleAcceptance_VBF_scale_Inclusive_UP",
    "QCDScaleAcceptance_VBF_scale_Inclusive_DOWN",
]
VBFStyleWeight_2017.InitUncertaintyVariations()
VBFStyleWeight_2017.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_VBF_scale_0jet_UP":CalculateVBFStyleWeight_vbf_0jet_UP,
    "QCDScaleAcceptance_VBF_scale_0jet_DOWN":CalculateVBFStyleWeight_vbf_0jet_DOWN,
    "QCDScaleAcceptance_VBF_scale_1jet_UP":CalculateVBFStyleWeight_vbf_1jet_UP,
    "QCDScaleAcceptance_VBF_scale_1jet_DOWN":CalculateVBFStyleWeight_vbf_1jet_DOWN,
    "QCDScaleAcceptance_VBF_scale_lowmjj_UP":CalculateVBFStyleWeight_vbf_lowmjj_UP,
    "QCDScaleAcceptance_VBF_scale_lowmjj_DOWN":CalculateVBFStyleWeight_vbf_lowmjj_DOWN,
    "QCDScaleAcceptance_VBF_scale_highmjj_lowpt_UP":CalculateVBFStyleWeight_vbf_highmjj_lowpt_UP,
    "QCDScaleAcceptance_VBF_scale_highmjj_lowpt_DOWN":CalculateVBFStyleWeight_vbf_highmjj_lowpt_DOWN,
    "QCDScaleAcceptance_VBF_scale_highmjj_highpt_UP":CalculateVBFStyleWeight_vbf_highmjj_highpt_UP,
    "QCDScaleAcceptance_VBF_scale_highmjj_highpt_DOWN":CalculateVBFStyleWeight_vbf_highmjj_highpt_DOWN,
    "QCDScaleAcceptance_VBF_scale_Inclusive_UP":CalculateVBFStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_VBF_scale_Inclusive_DOWN":CalculateVBFStyleWeight_Inclusive_DOWN,
}
VBFStyleWeight_2017.prepUpAndDownConstants = prepUpAndDownConstants
VBFStyleWeight_2017.prepUpAndDownConstants(VBFStyleWeight_2017)

VBFStyleWeight_2018 = Weight()
VBFStyleWeight_2018.name = 'QCDScaleAcceptance_VBF'
VBFStyleWeight_2018.reweightFile = ROOT.TFile(localWeightDataPath+'/QCDScaleAcceptance/VBFHTT2018.root')
VBFStyleWeight_2018.hasUpDownUncertainties = True
VBFStyleWeight_2018.CalculateWeight=CalculateVBFStyleWeight
VBFStyleWeight_2018.uncertaintyVariationList = [
    "QCDScaleAcceptance_VBF_scale_0jet_UP",
    "QCDScaleAcceptance_VBF_scale_0jet_DOWN",
    "QCDScaleAcceptance_VBF_scale_1jet_UP",
    "QCDScaleAcceptance_VBF_scale_1jet_DOWN",
    "QCDScaleAcceptance_VBF_scale_lowmjj_UP",
    "QCDScaleAcceptance_VBF_scale_lowmjj_DOWN",
    "QCDScaleAcceptance_VBF_scale_highmjj_lowpt_UP",
    "QCDScaleAcceptance_VBF_scale_highmjj_lowpt_DOWN",
    "QCDScaleAcceptance_VBF_scale_highmjj_highpt_UP",
    "QCDScaleAcceptance_VBF_scale_highmjj_highpt_DOWN",
    "QCDScaleAcceptance_VBF_scale_Inclusive_UP",
    "QCDScaleAcceptance_VBF_scale_Inclusive_DOWN",
]
VBFStyleWeight_2018.InitUncertaintyVariations()
VBFStyleWeight_2018.uncertaintyVariationFunctions={
    "QCDScaleAcceptance_VBF_scale_0jet_UP":CalculateVBFStyleWeight_vbf_0jet_UP,
    "QCDScaleAcceptance_VBF_scale_0jet_DOWN":CalculateVBFStyleWeight_vbf_0jet_DOWN,
    "QCDScaleAcceptance_VBF_scale_1jet_UP":CalculateVBFStyleWeight_vbf_1jet_UP,
    "QCDScaleAcceptance_VBF_scale_1jet_DOWN":CalculateVBFStyleWeight_vbf_1jet_DOWN,
    "QCDScaleAcceptance_VBF_scale_lowmjj_UP":CalculateVBFStyleWeight_vbf_lowmjj_UP,
    "QCDScaleAcceptance_VBF_scale_lowmjj_DOWN":CalculateVBFStyleWeight_vbf_lowmjj_DOWN,
    "QCDScaleAcceptance_VBF_scale_highmjj_lowpt_UP":CalculateVBFStyleWeight_vbf_highmjj_lowpt_UP,
    "QCDScaleAcceptance_VBF_scale_highmjj_lowpt_DOWN":CalculateVBFStyleWeight_vbf_highmjj_lowpt_DOWN,
    "QCDScaleAcceptance_VBF_scale_highmjj_highpt_UP":CalculateVBFStyleWeight_vbf_highmjj_highpt_UP,
    "QCDScaleAcceptance_VBF_scale_highmjj_highpt_DOWN":CalculateVBFStyleWeight_vbf_highmjj_highpt_DOWN,
    "QCDScaleAcceptance_VBF_scale_Inclusive_UP":CalculateVBFStyleWeight_Inclusive_UP,
    "QCDScaleAcceptance_VBF_scale_Inclusive_DOWN":CalculateVBFStyleWeight_Inclusive_DOWN,
}
VBFStyleWeight_2018.prepUpAndDownConstants = prepUpAndDownConstants
VBFStyleWeight_2018.prepUpAndDownConstants(VBFStyleWeight_2018)
