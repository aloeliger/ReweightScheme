import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from Configurations.Weights import localWeightDataPath

def CalculateHiggsReweighting(self,theTree):
    g_NNLOPS_0jet = self.HiggsPtWeightingFile.Get('gr_NNLOPSratio_pt_powheg_0jet')
    g_NNLOPS_1jet = self.HiggsPtWeightingFile.Get('gr_NNLOPSratio_pt_powheg_1jet')
    g_NNLOPS_2jet = self.HiggsPtWeightingFile.Get('gr_NNLOPSratio_pt_powheg_2jet')
    g_NNLOPS_3jet = self.HiggsPtWeightingFile.Get('gr_NNLOPSratio_pt_powheg_3jet')
    
    if theTree.Rivet_nJets30 == 0:
        self.value[0] = g_NNLOPS_0jet.Eval(min(theTree.Rivet_higgsPt,125.0))
    elif theTree.Rivet_nJets30 == 1:
        self.value[0] = g_NNLOPS_1jet.Eval(min(theTree.Rivet_higgsPt,625.0))
    elif theTree.Rivet_nJets30 == 2:
        self.value[0] = g_NNLOPS_1jet.Eval(min(theTree.Rivet_higgsPt,800.0))
    elif theTree.Rivet_nJets30 == 3:
        self.value[0] = g_NNLOPS_1jet.Eval(min(theTree.Rivet_higgsPt,925.0))
    

HiggsPtReweighting = Weight()
HiggsPtReweighting.name = 'HiggsPtReweighting'
HiggsPtReweighting.HiggsPtWeightingFile = ROOT.TFile.Open(localWeightDataPath+'NNLOPS_reweight.root')
HiggsPtReweighting.CalculateWeight = CalculateHiggsReweighting
