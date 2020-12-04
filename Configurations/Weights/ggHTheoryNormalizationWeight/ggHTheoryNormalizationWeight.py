import ROOT
from Configurations.Weights.WeightDefinition import Weight
from Configurations.Weights import localWeightDataPath

def prepNormalizationWeights(self):
    self.normalizationHistogram_pth_0_45 = self.reweightFile.Get("h_THUggH_pth0to45")
    self.normalizationWeight_pth_0_45_MuUP = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(2)
    self.normalizationWeight_pth_0_45_MuDOWN = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(3)

    self.normalizationWeight_pth_0_45_ResUP = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(4)
    self.normalizationWeight_pth_0_45_ResDOWN = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(5)

    self.normalizationWeight_pth_0_45_Mig01UP = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(6)
    self.normalizationWeight_pth_0_45_Mig01DOWN = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(7)

    self.normalizationWeight_pth_0_45_Mig12UP = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(8)
    self.normalizationWeight_pth_0_45_Mig12DOWN = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(9)

    self.normalizationWeight_pth_0_45_VBF2jUP = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(10)
    self.normalizationWeight_pth_0_45_VBF2jDOWN = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(11)

    self.normalizationWeight_pth_0_45_VBF3jUP = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(12)
    self.normalizationWeight_pth_0_45_VBF3jDOWN = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(13)
    
    self.normalizationWeight_pth_0_45_PT60UP = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(14)
    self.normalizationWeight_pth_0_45_PT60DOWN = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(15)

    self.normalizationWeight_pth_0_45_PT120UP = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(16)
    self.normalizationWeight_pth_0_45_PT120DOWN = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(17)

    self.normalizationWeight_pth_0_45_qmtopUP = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(18)
    self.normalizationWeight_pth_0_45_qmtopDOWN = self.normalizationHistogram_pth_0_45.GetBinContent(1)/self.normalizationHistogram_pth_0_45.GetBinContent(19)

    self.normalizationHistogram_pth_45_80 = self.reweightFile.Get("h_THUggH_pth45to80")
    self.normalizationWeight_pth_45_80_MuUP = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(2)
    self.normalizationWeight_pth_45_80_MuDOWN = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(3)

    self.normalizationWeight_pth_45_80_ResUP = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(4)
    self.normalizationWeight_pth_45_80_ResDOWN = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(5)

    self.normalizationWeight_pth_45_80_Mig01UP = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(6)
    self.normalizationWeight_pth_45_80_Mig01DOWN = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(7)

    self.normalizationWeight_pth_45_80_Mig12UP = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(8)
    self.normalizationWeight_pth_45_80_Mig12DOWN = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(9)

    self.normalizationWeight_pth_45_80_VBF2jUP = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(10)
    self.normalizationWeight_pth_45_80_VBF2jDOWN = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(11)

    self.normalizationWeight_pth_45_80_VBF3jUP = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(12)
    self.normalizationWeight_pth_45_80_VBF3jDOWN = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(13)
    
    self.normalizationWeight_pth_45_80_PT60UP = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(14)
    self.normalizationWeight_pth_45_80_PT60DOWN = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(15)

    self.normalizationWeight_pth_45_80_PT120UP = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(16)
    self.normalizationWeight_pth_45_80_PT120DOWN = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(17)

    self.normalizationWeight_pth_45_80_qmtopUP = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(18)
    self.normalizationWeight_pth_45_80_qmtopDOWN = self.normalizationHistogram_pth_45_80.GetBinContent(1)/self.normalizationHistogram_pth_45_80.GetBinContent(19)

    self.normalizationHistogram_pth_80_120 = self.reweightFile.Get("h_THUggH_pth80to120")
    self.normalizationWeight_pth_80_120_MuUP = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(2)
    self.normalizationWeight_pth_80_120_MuDOWN = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(3)

    self.normalizationWeight_pth_80_120_ResUP = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(4)
    self.normalizationWeight_pth_80_120_ResDOWN = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(5)

    self.normalizationWeight_pth_80_120_Mig01UP = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(6)
    self.normalizationWeight_pth_80_120_Mig01DOWN = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(7)

    self.normalizationWeight_pth_80_120_Mig12UP = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(8)
    self.normalizationWeight_pth_80_120_Mig12DOWN = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(9)

    self.normalizationWeight_pth_80_120_VBF2jUP = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(10)
    self.normalizationWeight_pth_80_120_VBF2jDOWN = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(11)

    self.normalizationWeight_pth_80_120_VBF3jUP = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(12)
    self.normalizationWeight_pth_80_120_VBF3jDOWN = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(13)
    
    self.normalizationWeight_pth_80_120_PT60UP = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(14)
    self.normalizationWeight_pth_80_120_PT60DOWN = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(15)

    self.normalizationWeight_pth_80_120_PT120UP = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(16)
    self.normalizationWeight_pth_80_120_PT120DOWN = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(17)

    self.normalizationWeight_pth_80_120_qmtopUP = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(18)
    self.normalizationWeight_pth_80_120_qmtopDOWN = self.normalizationHistogram_pth_80_120.GetBinContent(1)/self.normalizationHistogram_pth_80_120.GetBinContent(19)
    
    self.normalizationHistogram_pth_120_200 = self.reweightFile.Get("h_THUggH_pth120to200")
    self.normalizationWeight_pth_120_200_MuUP = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(2)
    self.normalizationWeight_pth_120_200_MuDOWN = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(3)

    self.normalizationWeight_pth_120_200_ResUP = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(4)
    self.normalizationWeight_pth_120_200_ResDOWN = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(5)

    self.normalizationWeight_pth_120_200_Mig01UP = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(6)
    self.normalizationWeight_pth_120_200_Mig01DOWN = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(7)

    self.normalizationWeight_pth_120_200_Mig12UP = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(8)
    self.normalizationWeight_pth_120_200_Mig12DOWN = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(9)

    self.normalizationWeight_pth_120_200_VBF2jUP = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(10)
    self.normalizationWeight_pth_120_200_VBF2jDOWN = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(11)

    self.normalizationWeight_pth_120_200_VBF3jUP = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(12)
    self.normalizationWeight_pth_120_200_VBF3jDOWN = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(13)
    
    self.normalizationWeight_pth_120_200_PT60UP = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(14)
    self.normalizationWeight_pth_120_200_PT60DOWN = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(15)

    self.normalizationWeight_pth_120_200_PT120UP = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(16)
    self.normalizationWeight_pth_120_200_PT120DOWN = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(17)

    self.normalizationWeight_pth_120_200_qmtopUP = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(18)
    self.normalizationWeight_pth_120_200_qmtopDOWN = self.normalizationHistogram_pth_120_200.GetBinContent(1)/self.normalizationHistogram_pth_120_200.GetBinContent(19)

    self.normalizationHistogram_pth_200_350 = self.reweightFile.Get("h_THUggH_pth200to350")
    self.normalizationWeight_pth_200_350_MuUP = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(2)
    self.normalizationWeight_pth_200_350_MuDOWN = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(3)

    self.normalizationWeight_pth_200_350_ResUP = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(4)
    self.normalizationWeight_pth_200_350_ResDOWN = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(5)

    self.normalizationWeight_pth_200_350_Mig01UP = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(6)
    self.normalizationWeight_pth_200_350_Mig01DOWN = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(7)

    self.normalizationWeight_pth_200_350_Mig12UP = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(8)
    self.normalizationWeight_pth_200_350_Mig12DOWN = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(9)

    self.normalizationWeight_pth_200_350_VBF2jUP = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(10)
    self.normalizationWeight_pth_200_350_VBF2jDOWN = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(11)

    self.normalizationWeight_pth_200_350_VBF3jUP = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(12)
    self.normalizationWeight_pth_200_350_VBF3jDOWN = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(13)
    
    self.normalizationWeight_pth_200_350_PT60UP = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(14)
    self.normalizationWeight_pth_200_350_PT60DOWN = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(15)

    self.normalizationWeight_pth_200_350_PT120UP = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(16)
    self.normalizationWeight_pth_200_350_PT120DOWN = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(17)

    self.normalizationWeight_pth_200_350_qmtopUP = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(18)
    self.normalizationWeight_pth_200_350_qmtopDOWN = self.normalizationHistogram_pth_200_350.GetBinContent(1)/self.normalizationHistogram_pth_200_350.GetBinContent(19)

    self.normalizationHistogram_pth_350_450 = self.reweightFile.Get("h_THUggH_pth350to450")
    self.normalizationWeight_pth_350_450_MuUP = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(2)
    self.normalizationWeight_pth_350_450_MuDOWN = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(3)

    self.normalizationWeight_pth_350_450_ResUP = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(4)
    self.normalizationWeight_pth_350_450_ResDOWN = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(5)

    self.normalizationWeight_pth_350_450_Mig01UP = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(6)
    self.normalizationWeight_pth_350_450_Mig01DOWN = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(7)

    self.normalizationWeight_pth_350_450_Mig12UP = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(8)
    self.normalizationWeight_pth_350_450_Mig12DOWN = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(9)

    self.normalizationWeight_pth_350_450_VBF2jUP = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(10)
    self.normalizationWeight_pth_350_450_VBF2jDOWN = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(11)

    self.normalizationWeight_pth_350_450_VBF3jUP = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(12)
    self.normalizationWeight_pth_350_450_VBF3jDOWN = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(13)
    
    self.normalizationWeight_pth_350_450_PT60UP = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(14)
    self.normalizationWeight_pth_350_450_PT60DOWN = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(15)

    self.normalizationWeight_pth_350_450_PT120UP = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(16)
    self.normalizationWeight_pth_350_450_PT120DOWN = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(17)

    self.normalizationWeight_pth_350_450_qmtopUP = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(18)
    self.normalizationWeight_pth_350_450_qmtopDOWN = self.normalizationHistogram_pth_350_450.GetBinContent(1)/self.normalizationHistogram_pth_350_450.GetBinContent(19)

    self.normalizationHistogram_pth_gt450 = self.reweightFile.Get("h_THUggH_pthgt450")
    self.normalizationWeight_pth_gt450_MuUP = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(2)
    self.normalizationWeight_pth_gt450_MuDOWN = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(3)

    self.normalizationWeight_pth_gt450_ResUP = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(4)
    self.normalizationWeight_pth_gt450_ResDOWN = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(5)

    self.normalizationWeight_pth_gt450_Mig01UP = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(6)
    self.normalizationWeight_pth_gt450_Mig01DOWN = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(7)

    self.normalizationWeight_pth_gt450_Mig12UP = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(8)
    self.normalizationWeight_pth_gt450_Mig12DOWN = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(9)

    self.normalizationWeight_pth_gt450_VBF2jUP = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(10)
    self.normalizationWeight_pth_gt450_VBF2jDOWN = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(11)

    self.normalizationWeight_pth_gt450_VBF3jUP = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(12)
    self.normalizationWeight_pth_gt450_VBF3jDOWN = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(13)
    
    self.normalizationWeight_pth_gt450_PT60UP = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(14)
    self.normalizationWeight_pth_gt450_PT60DOWN = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(15)

    self.normalizationWeight_pth_gt450_PT120UP = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(16)
    self.normalizationWeight_pth_gt450_PT120DOWN = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(17)

    self.normalizationWeight_pth_gt450_qmtopUP = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(18)
    self.normalizationWeight_pth_gt450_qmtopDOWN = self.normalizationHistogram_pth_gt450.GetBinContent(1)/self.normalizationHistogram_pth_gt450.GetBinContent(19)

    self.normalizationHistogram_njets_0 = self.reweightFile.Get("h_THUggH_njets0")
    self.normalizationWeight_njets_0_MuUP = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(2)
    self.normalizationWeight_njets_0_MuDOWN = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(3)

    self.normalizationWeight_njets_0_ResUP = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(4)
    self.normalizationWeight_njets_0_ResDOWN = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(5)

    self.normalizationWeight_njets_0_Mig01UP = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(6)
    self.normalizationWeight_njets_0_Mig01DOWN = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(7)

    self.normalizationWeight_njets_0_Mig12UP = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(8)
    self.normalizationWeight_njets_0_Mig12DOWN = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(9)

    self.normalizationWeight_njets_0_VBF2jUP = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(10)
    self.normalizationWeight_njets_0_VBF2jDOWN = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(11)

    self.normalizationWeight_njets_0_VBF3jUP = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(12)
    self.normalizationWeight_njets_0_VBF3jDOWN = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(13)
    
    self.normalizationWeight_njets_0_PT60UP = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(14)
    self.normalizationWeight_njets_0_PT60DOWN = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(15)

    self.normalizationWeight_njets_0_PT120UP = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(16)
    self.normalizationWeight_njets_0_PT120DOWN = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(17)

    self.normalizationWeight_njets_0_qmtopUP = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(18)
    self.normalizationWeight_njets_0_qmtopDOWN = self.normalizationHistogram_njets_0.GetBinContent(1)/self.normalizationHistogram_njets_0.GetBinContent(19)

    self.normalizationHistogram_njets_1 = self.reweightFile.Get("h_THUggH_njets1")
    self.normalizationWeight_njets_1_MuUP = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(2)
    self.normalizationWeight_njets_1_MuDOWN = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(3)

    self.normalizationWeight_njets_1_ResUP = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(4)
    self.normalizationWeight_njets_1_ResDOWN = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(5)

    self.normalizationWeight_njets_1_Mig01UP = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(6)
    self.normalizationWeight_njets_1_Mig01DOWN = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(7)

    self.normalizationWeight_njets_1_Mig12UP = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(8)
    self.normalizationWeight_njets_1_Mig12DOWN = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(9)

    self.normalizationWeight_njets_1_VBF2jUP = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(10)
    self.normalizationWeight_njets_1_VBF2jDOWN = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(11)

    self.normalizationWeight_njets_1_VBF3jUP = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(12)
    self.normalizationWeight_njets_1_VBF3jDOWN = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(13)
    
    self.normalizationWeight_njets_1_PT60UP = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(14)
    self.normalizationWeight_njets_1_PT60DOWN = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(15)

    self.normalizationWeight_njets_1_PT120UP = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(16)
    self.normalizationWeight_njets_1_PT120DOWN = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(17)

    self.normalizationWeight_njets_1_qmtopUP = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(18)
    self.normalizationWeight_njets_1_qmtopDOWN = self.normalizationHistogram_njets_1.GetBinContent(1)/self.normalizationHistogram_njets_1.GetBinContent(19)

    self.normalizationHistogram_njets_2 = self.reweightFile.Get("h_THUggH_njets2")
    self.normalizationWeight_njets_2_MuUP = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(2)
    self.normalizationWeight_njets_2_MuDOWN = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(3)

    self.normalizationWeight_njets_2_ResUP = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(4)
    self.normalizationWeight_njets_2_ResDOWN = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(5)

    self.normalizationWeight_njets_2_Mig01UP = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(6)
    self.normalizationWeight_njets_2_Mig01DOWN = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(7)

    self.normalizationWeight_njets_2_Mig12UP = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(8)
    self.normalizationWeight_njets_2_Mig12DOWN = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(9)

    self.normalizationWeight_njets_2_VBF2jUP = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(10)
    self.normalizationWeight_njets_2_VBF2jDOWN = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(11)

    self.normalizationWeight_njets_2_VBF3jUP = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(12)
    self.normalizationWeight_njets_2_VBF3jDOWN = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(13)
    
    self.normalizationWeight_njets_2_PT60UP = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(14)
    self.normalizationWeight_njets_2_PT60DOWN = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(15)

    self.normalizationWeight_njets_2_PT120UP = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(16)
    self.normalizationWeight_njets_2_PT120DOWN = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(17)

    self.normalizationWeight_njets_2_qmtopUP = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(18)
    self.normalizationWeight_njets_2_qmtopDOWN = self.normalizationHistogram_njets_2.GetBinContent(1)/self.normalizationHistogram_njets_2.GetBinContent(19)

    self.normalizationHistogram_njets_3 = self.reweightFile.Get("h_THUggH_njets3")
    self.normalizationWeight_njets_3_MuUP = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(2)
    self.normalizationWeight_njets_3_MuDOWN = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(3)

    self.normalizationWeight_njets_3_ResUP = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(4)
    self.normalizationWeight_njets_3_ResDOWN = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(5)

    self.normalizationWeight_njets_3_Mig01UP = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(6)
    self.normalizationWeight_njets_3_Mig01DOWN = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(7)

    self.normalizationWeight_njets_3_Mig12UP = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(8)
    self.normalizationWeight_njets_3_Mig12DOWN = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(9)

    self.normalizationWeight_njets_3_VBF2jUP = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(10)
    self.normalizationWeight_njets_3_VBF2jDOWN = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(11)

    self.normalizationWeight_njets_3_VBF3jUP = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(12)
    self.normalizationWeight_njets_3_VBF3jDOWN = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(13)
    
    self.normalizationWeight_njets_3_PT60UP = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(14)
    self.normalizationWeight_njets_3_PT60DOWN = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(15)

    self.normalizationWeight_njets_3_PT120UP = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(16)
    self.normalizationWeight_njets_3_PT120DOWN = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(17)

    self.normalizationWeight_njets_3_qmtopUP = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(18)
    self.normalizationWeight_njets_3_qmtopDOWN = self.normalizationHistogram_njets_3.GetBinContent(1)/self.normalizationHistogram_njets_3.GetBinContent(19)

    self.normalizationHistogram_njets_4 = self.reweightFile.Get("h_THUggH_njets4")
    self.normalizationWeight_njets_4_MuUP = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(2)
    self.normalizationWeight_njets_4_MuDOWN = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(3)

    self.normalizationWeight_njets_4_ResUP = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(4)
    self.normalizationWeight_njets_4_ResDOWN = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(5)

    self.normalizationWeight_njets_4_Mig01UP = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(6)
    self.normalizationWeight_njets_4_Mig01DOWN = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(7)

    self.normalizationWeight_njets_4_Mig12UP = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(8)
    self.normalizationWeight_njets_4_Mig12DOWN = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(9)

    self.normalizationWeight_njets_4_VBF2jUP = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(10)
    self.normalizationWeight_njets_4_VBF2jDOWN = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(11)

    self.normalizationWeight_njets_4_VBF3jUP = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(12)
    self.normalizationWeight_njets_4_VBF3jDOWN = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(13)
    
    self.normalizationWeight_njets_4_PT60UP = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(14)
    self.normalizationWeight_njets_4_PT60DOWN = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(15)

    self.normalizationWeight_njets_4_PT120UP = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(16)
    self.normalizationWeight_njets_4_PT120DOWN = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(17)

    self.normalizationWeight_njets_4_qmtopUP = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(18)
    self.normalizationWeight_njets_4_qmtopDOWN = self.normalizationHistogram_njets_4.GetBinContent(1)/self.normalizationHistogram_njets_4.GetBinContent(19)

    self.normalizationHistogram_j1pt_30_60 = self.reweightFile.Get("h_THUggH_j1pt30to60")
    self.normalizationWeight_j1pt_30_60_MuUP = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(2)
    self.normalizationWeight_j1pt_30_60_MuDOWN = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(3)

    self.normalizationWeight_j1pt_30_60_ResUP = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(4)
    self.normalizationWeight_j1pt_30_60_ResDOWN = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(5)

    self.normalizationWeight_j1pt_30_60_Mig01UP = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(6)
    self.normalizationWeight_j1pt_30_60_Mig01DOWN = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(7)

    self.normalizationWeight_j1pt_30_60_Mig12UP = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(8)
    self.normalizationWeight_j1pt_30_60_Mig12DOWN = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(9)

    self.normalizationWeight_j1pt_30_60_VBF2jUP = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(10)
    self.normalizationWeight_j1pt_30_60_VBF2jDOWN = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(11)

    self.normalizationWeight_j1pt_30_60_VBF3jUP = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(12)
    self.normalizationWeight_j1pt_30_60_VBF3jDOWN = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(13)
    
    self.normalizationWeight_j1pt_30_60_PT60UP = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(14)
    self.normalizationWeight_j1pt_30_60_PT60DOWN = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(15)

    self.normalizationWeight_j1pt_30_60_PT120UP = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(16)
    self.normalizationWeight_j1pt_30_60_PT120DOWN = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(17)

    self.normalizationWeight_j1pt_30_60_qmtopUP = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(18)
    self.normalizationWeight_j1pt_30_60_qmtopDOWN = self.normalizationHistogram_j1pt_30_60.GetBinContent(1)/self.normalizationHistogram_j1pt_30_60.GetBinContent(19)

    self.normalizationHistogram_j1pt_60_120 = self.reweightFile.Get("h_THUggH_j1pt60to120")
    self.normalizationWeight_j1pt_60_120_MuUP = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(2)
    self.normalizationWeight_j1pt_60_120_MuDOWN = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(3)

    self.normalizationWeight_j1pt_60_120_ResUP = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(4)
    self.normalizationWeight_j1pt_60_120_ResDOWN = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(5)

    self.normalizationWeight_j1pt_60_120_Mig01UP = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(6)
    self.normalizationWeight_j1pt_60_120_Mig01DOWN = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(7)

    self.normalizationWeight_j1pt_60_120_Mig12UP = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(8)
    self.normalizationWeight_j1pt_60_120_Mig12DOWN = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(9)

    self.normalizationWeight_j1pt_60_120_VBF2jUP = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(10)
    self.normalizationWeight_j1pt_60_120_VBF2jDOWN = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(11)

    self.normalizationWeight_j1pt_60_120_VBF3jUP = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(12)
    self.normalizationWeight_j1pt_60_120_VBF3jDOWN = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(13)
    
    self.normalizationWeight_j1pt_60_120_PT60UP = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(14)
    self.normalizationWeight_j1pt_60_120_PT60DOWN = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(15)

    self.normalizationWeight_j1pt_60_120_PT120UP = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(16)
    self.normalizationWeight_j1pt_60_120_PT120DOWN = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(17)

    self.normalizationWeight_j1pt_60_120_qmtopUP = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(18)
    self.normalizationWeight_j1pt_60_120_qmtopDOWN = self.normalizationHistogram_j1pt_60_120.GetBinContent(1)/self.normalizationHistogram_j1pt_60_120.GetBinContent(19)

    self.normalizationHistogram_j1pt_120_200 = self.reweightFile.Get("h_THUggH_j1pt120to200")
    self.normalizationWeight_j1pt_120_200_MuUP = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(2)
    self.normalizationWeight_j1pt_120_200_MuDOWN = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(3)

    self.normalizationWeight_j1pt_120_200_ResUP = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(4)
    self.normalizationWeight_j1pt_120_200_ResDOWN = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(5)

    self.normalizationWeight_j1pt_120_200_Mig01UP = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(6)
    self.normalizationWeight_j1pt_120_200_Mig01DOWN = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(7)

    self.normalizationWeight_j1pt_120_200_Mig12UP = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(8)
    self.normalizationWeight_j1pt_120_200_Mig12DOWN = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(9)

    self.normalizationWeight_j1pt_120_200_VBF2jUP = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(10)
    self.normalizationWeight_j1pt_120_200_VBF2jDOWN = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(11)

    self.normalizationWeight_j1pt_120_200_VBF3jUP = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(12)
    self.normalizationWeight_j1pt_120_200_VBF3jDOWN = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(13)
    
    self.normalizationWeight_j1pt_120_200_PT60UP = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(14)
    self.normalizationWeight_j1pt_120_200_PT60DOWN = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(15)

    self.normalizationWeight_j1pt_120_200_PT120UP = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(16)
    self.normalizationWeight_j1pt_120_200_PT120DOWN = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(17)

    self.normalizationWeight_j1pt_120_200_qmtopUP = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(18)
    self.normalizationWeight_j1pt_120_200_qmtopDOWN = self.normalizationHistogram_j1pt_120_200.GetBinContent(1)/self.normalizationHistogram_j1pt_120_200.GetBinContent(19)

    self.normalizationHistogram_j1pt_200_350 = self.reweightFile.Get("h_THUggH_j1pt200to350")
    self.normalizationWeight_j1pt_200_350_MuUP = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(2)
    self.normalizationWeight_j1pt_200_350_MuDOWN = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(3)

    self.normalizationWeight_j1pt_200_350_ResUP = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(4)
    self.normalizationWeight_j1pt_200_350_ResDOWN = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(5)

    self.normalizationWeight_j1pt_200_350_Mig01UP = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(6)
    self.normalizationWeight_j1pt_200_350_Mig01DOWN = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(7)

    self.normalizationWeight_j1pt_200_350_Mig12UP = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(8)
    self.normalizationWeight_j1pt_200_350_Mig12DOWN = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(9)

    self.normalizationWeight_j1pt_200_350_VBF2jUP = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(10)
    self.normalizationWeight_j1pt_200_350_VBF2jDOWN = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(11)

    self.normalizationWeight_j1pt_200_350_VBF3jUP = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(12)
    self.normalizationWeight_j1pt_200_350_VBF3jDOWN = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(13)
    
    self.normalizationWeight_j1pt_200_350_PT60UP = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(14)
    self.normalizationWeight_j1pt_200_350_PT60DOWN = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(15)

    self.normalizationWeight_j1pt_200_350_PT120UP = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(16)
    self.normalizationWeight_j1pt_200_350_PT120DOWN = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(17)

    self.normalizationWeight_j1pt_200_350_qmtopUP = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(18)
    self.normalizationWeight_j1pt_200_350_qmtopDOWN = self.normalizationHistogram_j1pt_200_350.GetBinContent(1)/self.normalizationHistogram_j1pt_200_350.GetBinContent(19)

    self.normalizationHistogram_j1pt_gt350 = self.reweightFile.Get("h_THUggH_j1ptgt350")
    self.normalizationWeight_j1pt_gt350_MuUP = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(2)
    self.normalizationWeight_j1pt_gt350_MuDOWN = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(3)

    self.normalizationWeight_j1pt_gt350_ResUP = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(4)
    self.normalizationWeight_j1pt_gt350_ResDOWN = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(5)

    self.normalizationWeight_j1pt_gt350_Mig01UP = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(6)
    self.normalizationWeight_j1pt_gt350_Mig01DOWN = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(7)

    self.normalizationWeight_j1pt_gt350_Mig12UP = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(8)
    self.normalizationWeight_j1pt_gt350_Mig12DOWN = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(9)

    self.normalizationWeight_j1pt_gt350_VBF2jUP = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(10)
    self.normalizationWeight_j1pt_gt350_VBF2jDOWN = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(11)

    self.normalizationWeight_j1pt_gt350_VBF3jUP = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(12)
    self.normalizationWeight_j1pt_gt350_VBF3jDOWN = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(13)
    
    self.normalizationWeight_j1pt_gt350_PT60UP = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(14)
    self.normalizationWeight_j1pt_gt350_PT60DOWN = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(15)

    self.normalizationWeight_j1pt_gt350_PT120UP = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(16)
    self.normalizationWeight_j1pt_gt350_PT120DOWN = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(17)

    self.normalizationWeight_j1pt_gt350_qmtopUP = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(18)
    self.normalizationWeight_j1pt_gt350_qmtopDOWN = self.normalizationHistogram_j1pt_gt350.GetBinContent(1)/self.normalizationHistogram_j1pt_gt350.GetBinContent(19)

def CalculateggHNormalizationWeight(self,theTree):
    self.value[0] = 1.0

def CalculateggHTHUMuUpByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_MuUP
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_MuUP
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_MuUP
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_MuUP
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_MuUP
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_MuUP
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_MuUP

def CalculateggHTHUMuDownByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_MuDOWN
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_MuDOWN
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_MuDOWN
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_MuDOWN
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_MuDOWN
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_MuDOWN
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_MuDOWN

def CalculateggHTHUResUpByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_ResUP
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_ResUP
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_ResUP
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_ResUP
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_ResUP
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_ResUP
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_ResUP

def CalculateggHTHUResDownByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_ResDOWN
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_ResDOWN
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_ResDOWN
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_ResDOWN
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_ResDOWN
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_ResDOWN
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_ResDOWN

def CalculateggHTHUMig01UpByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_Mig01UP
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_Mig01UP
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_Mig01UP
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_Mig01UP
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_Mig01UP
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_Mig01UP
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_Mig01UP

def CalculateggHTHUMig01DownByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_Mig01DOWN
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_Mig01DOWN
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_Mig01DOWN
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_Mig01DOWN
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_Mig01DOWN
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_Mig01DOWN
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_Mig01DOWN

def CalculateggHTHUMig12UpByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_Mig12UP
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_Mig12UP
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_Mig12UP
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_Mig12UP
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_Mig12UP
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_Mig12UP
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_Mig12UP

def CalculateggHTHUMig12DownByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_Mig12DOWN
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_Mig12DOWN
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_Mig12DOWN
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_Mig12DOWN
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_Mig12DOWN
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_Mig12DOWN
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_Mig12DOWN

def CalculateggHTHUVBF2jUpByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_VBF2jUP
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_VBF2jUP
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_VBF2jUP
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_VBF2jUP
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_VBF2jUP
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_VBF2jUP
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_VBF2jUP

def CalculateggHTHUVBF2jDownByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_VBF2jDOWN
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_VBF2jDOWN
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_VBF2jDOWN
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_VBF2jDOWN
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_VBF2jDOWN
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_VBF2jDOWN
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_VBF2jDOWN

def CalculateggHTHUVBF3jUpByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_VBF3jUP
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_VBF3jUP
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_VBF3jUP
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_VBF3jUP
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_VBF3jUP
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_VBF3jUP
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_VBF3jUP

def CalculateggHTHUVBF3jDownByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_VBF3jDOWN
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_VBF3jDOWN
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_VBF3jDOWN
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_VBF3jDOWN
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_VBF3jDOWN
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_VBF3jDOWN
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_VBF3jDOWN

def CalculateggHTHUPT60UpByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_PT60UP
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_PT60UP
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_PT60UP
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_PT60UP
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_PT60UP
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_PT60UP
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_PT60UP

def CalculateggHTHUPT60DownByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_PT60DOWN
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_PT60DOWN
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_PT60DOWN
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_PT60DOWN
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_PT60DOWN
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_PT60DOWN
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_PT60DOWN
    
def CalculateggHTHUPT120UpByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_PT120UP
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_PT120UP
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_PT120UP
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_PT120UP
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_PT120UP
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_PT120UP
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_PT120UP

def CalculateggHTHUPT120DownByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_PT120DOWN
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_PT120DOWN
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_PT120DOWN
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_PT120DOWN
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_PT120DOWN
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_PT120DOWN
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_PT120DOWN

def CalculateggHTHUqmtopUpByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_qmtopUP
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_qmtopUP
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_qmtopUP
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_qmtopUP
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_qmtopUP
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_qmtopUP
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_qmtopUP

def CalculateggHTHUqmtopDownByPTH(self,theTree,uncert):
    if (theTree.Rivet_higgsPt >= 0 and theTree.Rivet_higgsPt < 45):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_0_45_qmtopDOWN
    elif (theTree.Rivet_higgsPt >= 45 and theTree.Rivet_higgsPt < 80):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_45_80_qmtopDOWN
    elif (theTree.Rivet_higgsPt >= 80 and theTree.Rivet_higgsPt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_80_120_qmtopDOWN
    elif (theTree.Rivet_higgsPt >= 120 and theTree.Rivet_higgsPt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_120_200_qmtopDOWN
    elif (theTree.Rivet_higgsPt >= 200 and theTree.Rivet_higgsPt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_200_350_qmtopDOWN
    elif (theTree.Rivet_higgsPt >= 350 and theTree.Rivet_higgsPt < 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_350_450_qmtopDOWN
    elif (theTree.Rivet_higgsPt >= 450):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_pth_gt450_qmtopDOWN

def CalculateggHTHUMuUpByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_MuUP
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_MuUP
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_MuUP
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_MuUP
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_MuUP    

def CalculateggHTHUMuDownByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_MuDOWN
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_MuDOWN
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_MuDOWN
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_MuDOWN
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_MuDOWN    

def CalculateggHTHUResUpByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_ResUP
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_ResUP
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_ResUP
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_ResUP
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_ResUP    

def CalculateggHTHUResDownByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_ResDOWN
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_ResDOWN
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_ResDOWN
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_ResDOWN
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_ResDOWN    

def CalculateggHTHUMig01UpByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_Mig01UP
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_Mig01UP
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_Mig01UP
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_Mig01UP
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_Mig01UP    

def CalculateggHTHUMig01DownByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_Mig01DOWN
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_Mig01DOWN
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_Mig01DOWN
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_Mig01DOWN
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_Mig01DOWN    

def CalculateggHTHUMig12UpByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_Mig12UP
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_Mig12UP
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_Mig12UP
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_Mig12UP
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_Mig12UP    

def CalculateggHTHUMig12DownByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_Mig12DOWN
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_Mig12DOWN
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_Mig12DOWN
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_Mig12DOWN
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_Mig12DOWN    

def CalculateggHTHUVBF2jUpByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_VBF2jUP
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_VBF2jUP
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_VBF2jUP
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_VBF2jUP
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_VBF2jUP    

def CalculateggHTHUVBF2jDownByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_VBF2jDOWN
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_VBF2jDOWN
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_VBF2jDOWN
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_VBF2jDOWN
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_VBF2jDOWN    

def CalculateggHTHUVBF3jUpByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_VBF3jUP
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_VBF3jUP
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_VBF3jUP
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_VBF3jUP
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_VBF3jUP    

def CalculateggHTHUVBF3jDownByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_VBF3jDOWN
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_VBF3jDOWN
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_VBF3jDOWN
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_VBF3jDOWN
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_VBF3jDOWN    

def CalculateggHTHUPT60UpByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_PT60UP
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_PT60UP
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_PT60UP
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_PT60UP
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_PT60UP    

def CalculateggHTHUPT60DownByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_PT60DOWN
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_PT60DOWN
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_PT60DOWN
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_PT60DOWN
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_PT60DOWN    

def CalculateggHTHUPT120UpByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_PT120UP
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_PT120UP
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_PT120UP
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_PT120UP
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_PT120UP    

def CalculateggHTHUPT120DownByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_PT120DOWN
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_PT120DOWN
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_PT120DOWN
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_PT120DOWN
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_PT120DOWN    

def CalculateggHTHUqmtopUpByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_qmtopUP
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_qmtopUP
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_qmtopUP
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_qmtopUP
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_qmtopUP    

def CalculateggHTHUqmtopDownByNJETS(self,theTree,uncert):
    if (theTree.Rivet_nJets30 == 0):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_0_qmtopDOWN
    elif (theTree.Rivet_nJets30 == 1):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_1_qmtopDOWN
    elif (theTree.Rivet_nJets30 == 2):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_2_qmtopDOWN
    elif (theTree.Rivet_nJets30 == 3):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_3_qmtopDOWN
    elif (theTree.Rivet_nJets30 >= 4):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_njets_4_qmtopDOWN    

def CalculateggHTHUMuUpByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_MuUP
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_MuUP
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_MuUP
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_MuUP
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_MuUP    

def CalculateggHTHUMuDownByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_MuDOWN
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_MuDOWN
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_MuDOWN
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_MuDOWN
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_MuDOWN    

def CalculateggHTHUResUpByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_ResUP
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_ResUP
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_ResUP
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_ResUP
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_ResUP    

def CalculateggHTHUResDownByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_ResDOWN
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_ResDOWN
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_ResDOWN
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_ResDOWN
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_ResDOWN    

def CalculateggHTHUMig01UpByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_Mig01UP
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_Mig01UP
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_Mig01UP
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_Mig01UP
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_Mig01UP    

def CalculateggHTHUMig01DownByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_Mig01DOWN
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_Mig01DOWN
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_Mig01DOWN
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_Mig01DOWN
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_Mig01DOWN    
def CalculateggHTHUMig12UpByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_Mig12UP
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_Mig12UP
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_Mig12UP
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_Mig12UP
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_Mig12UP    

def CalculateggHTHUMig12DownByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_Mig12DOWN
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_Mig12DOWN
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_Mig12DOWN
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_Mig12DOWN
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_Mig12DOWN

def CalculateggHTHUVBF2jUpByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_VBF2jUP
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_VBF2jUP
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_VBF2jUP
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_VBF2jUP
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_VBF2jUP    

def CalculateggHTHUVBF2jDownByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_VBF2jDOWN
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_VBF2jDOWN
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_VBF2jDOWN
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_VBF2jDOWN
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_VBF2jDOWN

def CalculateggHTHUVBF3jUpByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_VBF3jUP
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_VBF3jUP
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_VBF3jUP
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_VBF3jUP
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_VBF3jUP    

def CalculateggHTHUVBF3jDownByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_VBF3jDOWN
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_VBF3jDOWN
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_VBF3jDOWN
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_VBF3jDOWN
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_VBF3jDOWN

def CalculateggHTHUPT60UpByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_PT60UP
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_PT60UP
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_PT60UP
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_PT60UP
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_PT60UP    

def CalculateggHTHUPT60DownByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_PT60DOWN
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_PT60DOWN
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_PT60DOWN
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_PT60DOWN
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_PT60DOWN
 
def CalculateggHTHUPT120UpByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_PT120UP
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_PT120UP
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_PT120UP
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_PT120UP
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_PT120UP    

def CalculateggHTHUPT120DownByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_PT120DOWN
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_PT120DOWN
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_PT120DOWN
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_PT120DOWN
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_PT120DOWN

def CalculateggHTHUqmtopUpByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_qmtopUP
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_qmtopUP
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_qmtopUP
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_qmtopUP
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_qmtopUP    

def CalculateggHTHUqmtopDownByJ1PT(self,theTree,uncert):
    if (theTree.Rivet_j1pt >= 30 and theTree.Rivet_j1pt < 60):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_30_60_qmtopDOWN
    elif (theTree.Rivet_j1pt >= 60 and theTree.Rivet_j1pt < 120):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_60_120_qmtopDOWN
    elif (theTree.Rivet_j1pt >= 120 and theTree.Rivet_j1pt < 200):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_120_200_qmtopDOWN
    elif (theTree.Rivet_j1pt >= 200 and theTree.Rivet_j1pt < 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_200_350_qmtopDOWN
    elif (theTree.Rivet_j1pt >= 350):
        self.uncertaintyVariationArrays[uncert][0] = self.normalizationWeight_j1pt_gt350_qmtopDOWN    

ggHTheoryNormalizationWeight = Weight()
ggHTheoryNormalizationWeight.name = 'ggHTheoryNormalization'
ggHTheoryNormalizationWeight.reweightFile = ROOT.TFile(localWeightDataPath+'/theory_uncertainties_differential/ggH_htt125.root')
ggHTheoryNormalizationWeight.hasUpDownUncertainties = True
ggHTheoryNormalizationWeight.CalculateWeight = CalculateggHNormalizationWeight
ggHTheoryNormalizationWeight.uncertaintyVariationList = [
    "ggHTheoryNormalization_Mu_pth_UP",
    "ggHTheoryNormalization_Mu_pth_DOWN",
    "ggHTheoryNormalization_Res_pth_UP",
    "ggHTheoryNormalization_Res_pth_DOWN",
    "ggHTheoryNormalization_Mig01_pth_UP",
    "ggHTheoryNormalization_Mig01_pth_DOWN",
    "ggHTheoryNormalization_Mig12_pth_UP",
    "ggHTheoryNormalization_Mig12_pth_DOWN",
    "ggHTheoryNormalization_VBF2j_pth_UP",
    "ggHTheoryNormalization_VBF2j_pth_DOWN",
    "ggHTheoryNormalization_VBF3j_pth_UP",
    "ggHTheoryNormalization_VBF3j_pth_DOWN",
    "ggHTheoryNormalization_PT60_pth_UP",
    "ggHTheoryNormalization_PT60_pth_DOWN",
    "ggHTheoryNormalization_PT120_pth_UP",
    "ggHTheoryNormalization_PT120_pth_DOWN",
    "ggHTheoryNormalization_qmtop_pth_UP",
    "ggHTheoryNormalization_qmtop_pth_DOWN",
    "ggHTheoryNormalization_Mu_njets_UP",
    "ggHTheoryNormalization_Mu_njets_DOWN",
    "ggHTheoryNormalization_Res_njets_UP",
    "ggHTheoryNormalization_Res_njets_DOWN",
    "ggHTheoryNormalization_Mig01_njets_UP",
    "ggHTheoryNormalization_Mig01_njets_DOWN",
    "ggHTheoryNormalization_Mig12_njets_UP",
    "ggHTheoryNormalization_Mig12_njets_DOWN",
    "ggHTheoryNormalization_VBF2j_njets_UP",
    "ggHTheoryNormalization_VBF2j_njets_DOWN",
    "ggHTheoryNormalization_VBF3j_njets_UP",
    "ggHTheoryNormalization_VBF3j_njets_DOWN",
    "ggHTheoryNormalization_PT60_njets_UP",
    "ggHTheoryNormalization_PT60_njets_DOWN",
    "ggHTheoryNormalization_PT120_njets_UP",
    "ggHTheoryNormalization_PT120_njets_DOWN",
    "ggHTheoryNormalization_qmtop_njets_UP",
    "ggHTheoryNormalization_qmtop_njets_DOWN",
    "ggHTheoryNormalization_Mu_j1pt_UP",
    "ggHTheoryNormalization_Mu_j1pt_DOWN",
    "ggHTheoryNormalization_Res_j1pt_UP",
    "ggHTheoryNormalization_Res_j1pt_DOWN",
    "ggHTheoryNormalization_Mig01_j1pt_UP",
    "ggHTheoryNormalization_Mig01_j1pt_DOWN",
    "ggHTheoryNormalization_Mig12_j1pt_UP",
    "ggHTheoryNormalization_Mig12_j1pt_DOWN",
    "ggHTheoryNormalization_VBF2j_j1pt_UP",
    "ggHTheoryNormalization_VBF2j_j1pt_DOWN",
    "ggHTheoryNormalization_VBF3j_j1pt_UP",
    "ggHTheoryNormalization_VBF3j_j1pt_DOWN",
    "ggHTheoryNormalization_PT60_j1pt_UP",
    "ggHTheoryNormalization_PT60_j1pt_DOWN",
    "ggHTheoryNormalization_PT120_j1pt_UP",
    "ggHTheoryNormalization_PT120_j1pt_DOWN",
    "ggHTheoryNormalization_qmtop_j1pt_UP",
    "ggHTheoryNormalization_qmtop_j1pt_DOWN",
]
ggHTheoryNormalizationWeight.InitUncertaintyVariations()
ggHTheoryNormalizationWeight.uncertaintyVariationFunctions={
    "ggHTheoryNormalization_Mu_pth_UP":CalculateggHTHUMuUpByPTH,
    "ggHTheoryNormalization_Mu_pth_DOWN":CalculateggHTHUMuDownByPTH,
    "ggHTheoryNormalization_Res_pth_UP":CalculateggHTHUResUpByPTH,
    "ggHTheoryNormalization_Res_pth_DOWN":CalculateggHTHUResDownByPTH,
    "ggHTheoryNormalization_Mig01_pth_UP":CalculateggHTHUMig01UpByPTH,
    "ggHTheoryNormalization_Mig01_pth_DOWN":CalculateggHTHUMig01DownByPTH,
    "ggHTheoryNormalization_Mig12_pth_UP":CalculateggHTHUMig12UpByPTH,
    "ggHTheoryNormalization_Mig12_pth_DOWN":CalculateggHTHUMig12DownByPTH,
    "ggHTheoryNormalization_VBF2j_pth_UP":CalculateggHTHUVBF2jUpByPTH,
    "ggHTheoryNormalization_VBF2j_pth_DOWN":CalculateggHTHUVBF2jDownByPTH,
    "ggHTheoryNormalization_VBF3j_pth_UP":CalculateggHTHUVBF3jUpByPTH,
    "ggHTheoryNormalization_VBF3j_pth_DOWN":CalculateggHTHUVBF3jDownByPTH,
    "ggHTheoryNormalization_PT60_pth_UP":CalculateggHTHUPT60UpByPTH,
    "ggHTheoryNormalization_PT60_pth_DOWN":CalculateggHTHUPT60DownByPTH,
    "ggHTheoryNormalization_PT120_pth_UP":CalculateggHTHUPT120UpByPTH,
    "ggHTheoryNormalization_PT120_pth_DOWN":CalculateggHTHUPT120DownByPTH,
    "ggHTheoryNormalization_qmtop_pth_UP":CalculateggHTHUqmtopUpByPTH,
    "ggHTheoryNormalization_qmtop_pth_DOWN":CalculateggHTHUqmtopDownByPTH,
    "ggHTheoryNormalization_Mu_njets_UP":CalculateggHTHUMuUpByNJETS,
    "ggHTheoryNormalization_Mu_njets_DOWN":CalculateggHTHUMuDownByNJETS,
    "ggHTheoryNormalization_Res_njets_UP":CalculateggHTHUResUpByNJETS,
    "ggHTheoryNormalization_Res_njets_DOWN":CalculateggHTHUResDownByNJETS,
    "ggHTheoryNormalization_Mig01_njets_UP":CalculateggHTHUMig01UpByNJETS,
    "ggHTheoryNormalization_Mig01_njets_DOWN":CalculateggHTHUMig01DownByNJETS,
    "ggHTheoryNormalization_Mig12_njets_UP":CalculateggHTHUMig12UpByNJETS,
    "ggHTheoryNormalization_Mig12_njets_DOWN":CalculateggHTHUMig12DownByNJETS,
    "ggHTheoryNormalization_VBF2j_njets_UP":CalculateggHTHUVBF2jUpByNJETS,
    "ggHTheoryNormalization_VBF2j_njets_DOWN":CalculateggHTHUVBF2jDownByNJETS,
    "ggHTheoryNormalization_VBF3j_njets_UP":CalculateggHTHUVBF3jUpByNJETS,
    "ggHTheoryNormalization_VBF3j_njets_DOWN":CalculateggHTHUVBF3jDownByNJETS,
    "ggHTheoryNormalization_PT60_njets_UP":CalculateggHTHUPT60UpByNJETS,
    "ggHTheoryNormalization_PT60_njets_DOWN":CalculateggHTHUPT60DownByNJETS,
    "ggHTheoryNormalization_PT120_njets_UP":CalculateggHTHUPT120UpByNJETS,
    "ggHTheoryNormalization_PT120_njets_DOWN":CalculateggHTHUPT120DownByNJETS,
    "ggHTheoryNormalization_qmtop_njets_UP":CalculateggHTHUqmtopUpByNJETS,
    "ggHTheoryNormalization_qmtop_njets_DOWN":CalculateggHTHUqmtopDownByNJETS,
    "ggHTheoryNormalization_Mu_j1pt_UP":CalculateggHTHUMuUpByJ1PT,
    "ggHTheoryNormalization_Mu_j1pt_DOWN":CalculateggHTHUMuDownByJ1PT,
    "ggHTheoryNormalization_Res_j1pt_UP":CalculateggHTHUResUpByJ1PT,
    "ggHTheoryNormalization_Res_j1pt_DOWN":CalculateggHTHUResDownByJ1PT,
    "ggHTheoryNormalization_Mig01_j1pt_UP":CalculateggHTHUMig01UpByJ1PT,
    "ggHTheoryNormalization_Mig01_j1pt_DOWN":CalculateggHTHUMig01DownByJ1PT,
    "ggHTheoryNormalization_Mig12_j1pt_UP":CalculateggHTHUMig12UpByJ1PT,
    "ggHTheoryNormalization_Mig12_j1pt_DOWN":CalculateggHTHUMig12DownByJ1PT,
    "ggHTheoryNormalization_VBF2j_j1pt_UP":CalculateggHTHUVBF2jUpByJ1PT,
    "ggHTheoryNormalization_VBF2j_j1pt_DOWN":CalculateggHTHUVBF2jDownByJ1PT,
    "ggHTheoryNormalization_VBF3j_j1pt_UP":CalculateggHTHUVBF3jUpByJ1PT,
    "ggHTheoryNormalization_VBF3j_j1pt_DOWN":CalculateggHTHUVBF3jDownByJ1PT,
    "ggHTheoryNormalization_PT60_j1pt_UP":CalculateggHTHUPT60UpByJ1PT,
    "ggHTheoryNormalization_PT60_j1pt_DOWN":CalculateggHTHUPT60DownByJ1PT,
    "ggHTheoryNormalization_PT120_j1pt_UP":CalculateggHTHUPT120UpByJ1PT,
    "ggHTheoryNormalization_PT120_j1pt_DOWN":CalculateggHTHUPT120DownByJ1PT,
    "ggHTheoryNormalization_qmtop_j1pt_UP":CalculateggHTHUqmtopUpByJ1PT,
    "ggHTheoryNormalization_qmtop_j1pt_DOWN":CalculateggHTHUqmtopDownByJ1PT,
}
ggHTheoryNormalizationWeight.prepNormalizationWeights = prepNormalizationWeights
ggHTheoryNormalizationWeight.prepNormalizationWeights(ggHTheoryNormalizationWeight)
