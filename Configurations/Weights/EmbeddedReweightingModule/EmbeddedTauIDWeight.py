import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from TauPOG.TauIDSFs.TauIDSFTool import TauIDSFTool
import Configurations.Weights.TauIDModule.TauIDFunctions as TauIDFunctions

embeddedTauIDWeight_2016 = Weight()
embeddedTauIDWeight_2016.name = "EmbeddedTauIDWeight"
embeddedTauIDWeight_2016.CalculateWeight = TauIDFunctions.CalculateTauIDWeight
embeddedTauIDWeight_2016.SFTool = TauIDSFTool("2016Legacy","DeepTau2017v2p1VSjet",'Medium',embedding=True)
embeddedTauIDWeight_2016.hasUpDownUncertainties = True
embeddedTauIDWeight_2016.uncertaintyVariationList = [
    "TauID_pT0to35_UP",
    "TauID_pT0to35_DOWN",
    "TauID_pT35to40_UP",
    "TauID_pT35to40_DOWN",
    "TauID_pTgt40_UP",
    "TauID_pTgt40_DOWN",
    ]
embeddedTauIDWeight_2016.InitUncertaintyVariations()
embeddedTauIDWeight_2016.uncertaintyVariationFunctions = {
    "TauID_pT0to35_UP": TauIDFunctions.CalculateTauIDWeight_pT0to35_UP,
    "TauID_pT0to35_DOWN": TauIDFunctions.CalculateTauIDWeight_pT0to35_DOWN,
    "TauID_pT35to40_UP": TauIDFunctions.CalculateTauIDWeight_pT35to40_UP,
    "TauID_pT35to40_DOWN": TauIDFunctions.CalculateTauIDWeight_pT35to40_DOWN,
    "TauID_pTgt40_UP": TauIDFunctions.CalculateTauIDWeight_pTgt40_UP,
    "TauID_pTgt40_DOWN": TauIDFunctions.CalculateTauIDWeight_pTgt40_DOWN,
    }

embeddedTauIDWeight_2017 = Weight()
embeddedTauIDWeight_2017.name = "EmbeddedTauIDWeight"
embeddedTauIDWeight_2017.CalculateWeight = TauIDFunctions.CalculateTauIDWeight
embeddedTauIDWeight_2017.SFTool = TauIDSFTool("2017ReReco","DeepTau2017v2p1VSjet",'Medium',embedding=True)
embeddedTauIDWeight_2017.hasUpDownUncertainties = True
embeddedTauIDWeight_2017.uncertaintyVariationList = [
    "TauID_pT0to35_UP",
    "TauID_pT0to35_DOWN",
    "TauID_pT35to40_UP",
    "TauID_pT35to40_DOWN",
    "TauID_pTgt40_UP",
    "TauID_pTgt40_DOWN",
    ]
embeddedTauIDWeight_2017.InitUncertaintyVariations()
embeddedTauIDWeight_2017.uncertaintyVariationFunctions = {
    "TauID_pT0to35_UP": TauIDFunctions.CalculateTauIDWeight_pT0to35_UP,
    "TauID_pT0to35_DOWN": TauIDFunctions.CalculateTauIDWeight_pT0to35_DOWN,
    "TauID_pT35to40_UP": TauIDFunctions.CalculateTauIDWeight_pT35to40_UP,
    "TauID_pT35to40_DOWN": TauIDFunctions.CalculateTauIDWeight_pT35to40_DOWN,
    "TauID_pTgt40_UP": TauIDFunctions.CalculateTauIDWeight_pTgt40_UP,
    "TauID_pTgt40_DOWN": TauIDFunctions.CalculateTauIDWeight_pTgt40_DOWN,
    }

embeddedTauIDWeight_2018 = Weight()
embeddedTauIDWeight_2018.name = "EmbeddedTauIDWeight"
embeddedTauIDWeight_2018.CalculateWeight = TauIDFunctions.CalculateTauIDWeight
embeddedTauIDWeight_2018.SFTool = TauIDSFTool("2018ReReco","DeepTau2017v2p1VSjet",'Medium',embedding=True)
embeddedTauIDWeight_2018.hasUpDownUncertainties = True
embeddedTauIDWeight_2018.uncertaintyVariationList = [
    "TauID_pT0to35_UP",
    "TauID_pT0to35_DOWN",
    "TauID_pT35to40_UP",
    "TauID_pT35to40_DOWN",
    "TauID_pTgt40_UP",
    "TauID_pTgt40_DOWN",
    ]
embeddedTauIDWeight_2018.InitUncertaintyVariations()
embeddedTauIDWeight_2018.uncertaintyVariationFunctions = {
    "TauID_pT0to35_UP": TauIDFunctions.CalculateTauIDWeight_pT0to35_UP,
    "TauID_pT0to35_DOWN": TauIDFunctions.CalculateTauIDWeight_pT0to35_DOWN,
    "TauID_pT35to40_UP": TauIDFunctions.CalculateTauIDWeight_pT35to40_UP,
    "TauID_pT35to40_DOWN": TauIDFunctions.CalculateTauIDWeight_pT35to40_DOWN,
    "TauID_pTgt40_UP": TauIDFunctions.CalculateTauIDWeight_pTgt40_UP,
    "TauID_pTgt40_DOWN": TauIDFunctions.CalculateTauIDWeight_pTgt40_DOWN,
    }
