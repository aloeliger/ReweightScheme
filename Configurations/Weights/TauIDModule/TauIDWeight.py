import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from TauPOG.TauIDSFs.TauIDSFTool import TauIDSFTool
import TauIDFunctions

tauIDWeight_2016 = Weight()
tauIDWeight_2016.name = 'TauIDWeight'
tauIDWeight_2016.SFTool = TauIDSFTool("2016Legacy","DeepTau2017v2p1VSjet",'Medium')
tauIDWeight_2016.CalculateWeight = TauIDFunctions.CalculateTauIDWeight
tauIDWeight_2016.hasUpDownUncertainties = True
tauIDWeight_2016.uncertaintyVariationList = [
    "TauID_pT0to35_UP",
    "TauID_pT0to35_DOWN",
    "TauID_pT35to40_UP",
    "TauID_pT35to40_DOWN",
    "TauID_pTgt40_UP",
    "TauID_pTgt40_DOWN",
    ]
tauIDWeight_2016.InitUncertaintyVariations()
tauIDWeight_2016.uncertaintyVariationFunctions = {
    "TauID_pT0to35_UP": TauIDFunctions.CalculateTauIDWeight_pT0to35_UP,
    "TauID_pT0to35_DOWN": TauIDFunctions.CalculateTauIDWeight_pT0to35_DOWN,
    "TauID_pT35to40_UP": TauIDFunctions.CalculateTauIDWeight_pT35to40_UP,
    "TauID_pT35to40_DOWN": TauIDFunctions.CalculateTauIDWeight_pT35to40_DOWN,
    "TauID_pTgt40_UP": TauIDFunctions.CalculateTauIDWeight_pTgt40_UP,
    "TauID_pTgt40_DOWN": TauIDFunctions.CalculateTauIDWeight_pTgt40_DOWN,
    }

tauIDWeight_2017 = Weight()
tauIDWeight_2017.name = 'TauIDWeight'
tauIDWeight_2017.SFTool = TauIDSFTool("2017ReReco",'DeepTau2017v2p1VSjet','Medium')
tauIDWeight_2017.CalculateWeight = TauIDFunctions.CalculateTauIDWeight
tauIDWeight_2017.hasUpDownUncertainties = True
tauIDWeight_2017.uncertaintyVariationList = [
    "TauID_pT0to35_UP",
    "TauID_pT0to35_DOWN",
    "TauID_pT35to40_UP",
    "TauID_pT35to40_DOWN",
    "TauID_pTgt40_UP",
    "TauID_pTgt40_DOWN",
    ]
tauIDWeight_2017.InitUncertaintyVariations()
tauIDWeight_2017.uncertaintyVariationFunctions = {
    "TauID_pT0to35_UP": TauIDFunctions.CalculateTauIDWeight_pT0to35_UP,
    "TauID_pT0to35_DOWN": TauIDFunctions.CalculateTauIDWeight_pT0to35_DOWN,
    "TauID_pT35to40_UP": TauIDFunctions.CalculateTauIDWeight_pT35to40_UP,
    "TauID_pT35to40_DOWN": TauIDFunctions.CalculateTauIDWeight_pT35to40_DOWN,
    "TauID_pTgt40_UP": TauIDFunctions.CalculateTauIDWeight_pTgt40_UP,
    "TauID_pTgt40_DOWN": TauIDFunctions.CalculateTauIDWeight_pTgt40_DOWN,
    }

tauIDWeight_2018 = Weight()
tauIDWeight_2018.name = 'TauIDWeight'
tauIDWeight_2018.SFTool = TauIDSFTool("2018ReReco",'DeepTau2017v2p1VSjet','Medium')
tauIDWeight_2018.CalculateWeight = TauIDFunctions.CalculateTauIDWeight
tauIDWeight_2018.hasUpDownUncertainties = True
tauIDWeight_2018.uncertaintyVariationList = [
    "TauID_pT0to35_UP",
    "TauID_pT0to35_DOWN",
    "TauID_pT35to40_UP",
    "TauID_pT35to40_DOWN",
    "TauID_pTgt40_UP",
    "TauID_pTgt40_DOWN",
    ]
tauIDWeight_2018.InitUncertaintyVariations()
tauIDWeight_2018.uncertaintyVariationFunctions = {
    "TauID_pT0to35_UP": TauIDFunctions.CalculateTauIDWeight_pT0to35_UP,
    "TauID_pT0to35_DOWN": TauIDFunctions.CalculateTauIDWeight_pT0to35_DOWN,
    "TauID_pT35to40_UP": TauIDFunctions.CalculateTauIDWeight_pT35to40_UP,
    "TauID_pT35to40_DOWN": TauIDFunctions.CalculateTauIDWeight_pT35to40_DOWN,
    "TauID_pTgt40_UP": TauIDFunctions.CalculateTauIDWeight_pTgt40_UP,
    "TauID_pTgt40_DOWN": TauIDFunctions.CalculateTauIDWeight_pTgt40_DOWN,
    }
