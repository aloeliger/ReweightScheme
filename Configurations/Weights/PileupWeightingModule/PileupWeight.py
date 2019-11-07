import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from Configurations.Weights import localWeightDataPath

#unfortunately this is also going to need a "year", "sample" variable intialization
#also has it's own Init function that will have to be called in configuration to open up files
# and make the overall pileup weighting histograms

def InitPileupWeightings(self):
    if self.year == "2017":
        if self.sample == "VBF":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#VBFHToTauTau_M125_13TeV_powheg_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1#MINIAODSIM")
        elif self.sample == "W1":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3#MINIAODSIM")
        elif self.sample == "W2":
            self.MCHsito = self.Pileup_MC_File.Get("pua/#W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v5#MINIAODSIM")
        elif self.sample == "ST_t_antitop":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM")
        elif self.sample == "DY4":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_v2_94X_mc2017_realistic_v14-v2#MINIAODSIM")
        elif self.sample == "W":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3#MINIAODSIM")
        elif self.sample == "DY":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8#RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM")
        elif self.sample == "WW":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#WW_TuneCP5_13TeV-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM")
        elif self.sample == "WZ":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#WZ_TuneCP5_13TeV-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM")
        elif self.sample == "ST_tW_top":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2#MINIAODSIM")
        elif self.sample == "WHMinus":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#WminusHToTauTau_M125_13TeV_powheg_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM")
        elif self.sample == "WHPlus":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#WplusHToTauTau_M125_13TeV_powheg_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM")
        elif self.sample == "ST_tW_antitop":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2#MINIAODSIM")
        elif self.sample == "W3":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM")
        elif self.sample == "ZH125":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#ZHToTauTau_M125_13TeV_powheg_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM")        
        elif self.sample == "TTTo2L2Nu":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1#MINIAODSIM")
        elif self.sample == "TTToHadronic":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#TTToHadronic_TuneCP5_13TeV-powheg-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2#MINIAODSIM")
        elif self.sample == "TTToSemiLeptonic":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1#MINIAODSIM")
        elif self.sample == "EWK":
            self.MCHisto = self.Pileup_MC_File.Get("pua/#EWKZ2Jets_ZToLL_M-50_TuneCP5_13TeV-madgraph-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2#MINIAODSIM")
        self.DataHisto = self.Pileup_Data_File.Get("pileup")
    elif self.year == "2016" or self.year == "2018":
        self.MCHisto = self.Pileup_MC_File.Get("pileup")
        self.DataHisto = self.Pileup_Data_File.Get("pileup")
    self.theWeightsHisto = self.DataHisto.Clone()
    self.theWeightsHisto.Scale(1.0/self.theWeightsHisto.Integral())
    self.MCHisto.Scale(1.0/self.MCHisto.Integral())

    self.theWeightsHisto.Divide(self.MCHisto)
    

def CalculatePileupWeighting(self,theTree):
    self.value[0] = self.theWeightsHisto.GetBinContent(self.theWeightsHisto.FindBin(theTree.npu))

pileupWeight_2016 = Weight()
pileupWeight_2016.name = 'PileupWeighting'
pileupWeight_2016.Pileup_MC_File = ROOT.TFile.Open(localWeightDataPath+"MC_Moriond17_PU25ns_V1.root")
pileupWeight_2016.Pileup_Data_File = ROOT.TFile.Open(localWeightDataPath+"Data_Pileup_2016_271036-284044_80bins.root")
pileupWeight_2016.InitPileupWeightings = InitPileupWeightings
pileupWeight_2016.CalculateWeight = CalculatePileupWeighting

pileupWeight_2017 = Weight()
pileupWeight_2017.name = 'PileupWeighting'
pileupWeight_2017.Pileup_MC_File = ROOT.TFile.Open(localWeightDataPath+"pu_distributions_mc_2017.root")
pileupWeight_2017.Pileup_Data_File = ROOT.TFile.Open(localWeightDataPath+"pu_distributions_data_2017.root")
pileupWeight_2017.InitPileupWeightings = InitPileupWeightings
pileupWeight_2017.CalculateWeight = CalculatePileupWeighting

pileupWeight_2018 = Weight()
pileupWeight_2018.name = 'PileupWeighting'
pileupWeight_2018.Pileup_MC_File = ROOT.TFile.Open(localWeightDataPath+"pu_distributions_mc_2018.root")
pileupWeight_2018.Pileup_Data_File = ROOT.TFile.Open(localWeightDataPath+"pu_distributions_data_2018.root")
pileupWeight_2018.InitPileupWeightings = InitPileupWeightings
pileupWeight_2018.CalculateWeight = CalculatePileupWeighting
