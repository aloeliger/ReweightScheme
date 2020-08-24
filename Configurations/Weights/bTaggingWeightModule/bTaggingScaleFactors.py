import ROOT

scaleFactorFunction = lambda a,b,c,d,pt: a + b*pt + c*pt*pt + d*pt*pt*pt

def GetbTaggingScaleFactor(year='2016',jetWP=0, jetPt=30, jetEta=0, fsaJetFlavor=0):
    scaleFactor = 0

    if year == '2016':
        if jetWP==1:
            if fsaJetFlavor == 4 or fsaJetFlavor == 5:
                if jetPt > 30 and jetPt < 120:
                    scaleFactor = scaleFactorFunction(0.95718,0,0,0,jetPt)
                elif jetPt > 120 and jetPt < 180:
                    scaleFactor = scaleFactorFunction(0.98196,0,0,0,jetPt)
                elif jetPt > 180 and jetPt < 240:
                    scaleFactor = scaleFactorFunction(0.98847,0,0,0,jetPt)
                elif jetPt > 240 and jetPt < 450:
                    scaleFactor = scaleFactorFunction(0.96509,0,0,0,jetPt)            
            elif fsaJetFlavor > 0:
                scaleFactor = scaleFactorFunction(0.98942,0.000846199,-4.38993e-07,0,jetPt)
            else:
                return 0
        elif jetWP==0:
            if fsaJetFlavor == 4 or fsaJetFlavor == 5:
                if jetPt > 30 and jetPt < 120:
                    scaleFactor = scaleFactorFunction(0.98635,0,0,0,jetPt)
                elif jetPt > 120 and jetPt < 180:
                    scaleFactor = scaleFactorFunction(0.99556,0,0,0,jetPt)
                elif jetPt > 180 and jetPt < 240:
                    scaleFactor = scaleFactorFunction(0.98453,0,0,0,jetPt)
                elif jetPt > 240 and jetPt < 450:
                    scaleFactor = scaleFactorFunction(0.97532,0,0,0,jetPt)            
            elif fsaJetFlavor > 0:
                scaleFactor = scaleFactorFunction(1.01035,0.000716785,-8.62314e-07,4.61617e-10,jetPt)
            else:
                return 0
        else:
            return 0

    elif year == '2017':
        if jetWP==1:
            if fsaJetFlavor == 4 or fsaJetFlavor == 5:
                if jetPt > 30 and jetPt < 120:
                    scaleFactor = scaleFactorFunction(0.88846,0,0,0,jetPt)
                elif jetPt > 120 and jetPt < 180:
                    scaleFactor = scaleFactorFunction(0.84588,0,0,0,jetPt)
                elif jetPt > 180 and jetPt < 240:
                    scaleFactor = scaleFactorFunction(0.96052,0,0,0,jetPt)
                elif jetPt > 240 and jetPt < 450:
                    scaleFactor = scaleFactorFunction(0.90151,0,0,0,jetPt)            
            elif fsaJetFlavor > 0:
                scaleFactor = scaleFactorFunction(0.853286,0.000801883,-1.00211e-06,0,jetPt)
            else:
                return 0
        elif jetWP==0:
            if fsaJetFlavor == 4 or fsaJetFlavor == 5:
                if jetPt > 30 and jetPt < 120:
                    scaleFactor = scaleFactorFunction(0.90419,0,0,0,jetPt)
                elif jetPt > 120 and jetPt < 180:
                    scaleFactor = scaleFactorFunction(0.95258,0,0,0,jetPt)
                elif jetPt > 180 and jetPt < 240:
                    scaleFactor = scaleFactorFunction(0.9673,0,0,0,jetPt)
                elif jetPt > 240 and jetPt < 450:
                    scaleFactor = scaleFactorFunction(0.97097,0,0,0,jetPt)            
            elif fsaJetFlavor > 0:
                scaleFactor = scaleFactorFunction(0.991997,0.000585324,-2.8941e-07,-6.52532e-11,jetPt)
            else:
                return 0
        else:
            return 0
            
    elif year == '2018':
        if jetWP==1:
            if fsaJetFlavor == 4 or fsaJetFlavor == 5:
                if jetPt > 30 and jetPt < 120:
                    scaleFactor = scaleFactorFunction(0.87815,0,0,0,jetPt)
                elif jetPt > 120 and jetPt < 180:
                    scaleFactor = scaleFactorFunction(0.99259,0,0,0,jetPt)
                elif jetPt > 180 and jetPt < 240:
                    scaleFactor = scaleFactorFunction(0.9665,0,0,0,jetPt)
                elif jetPt > 240 and jetPt < 450:
                    scaleFactor = scaleFactorFunction(0.93914,0,0,0,jetPt)            
            elif fsaJetFlavor > 0:
                scaleFactor = scaleFactorFunction(1.36065,-0.00080014,9.06839e-07,0,jetPt)
            else:
                return 0
        elif jetWP==0:
            if fsaJetFlavor == 4 or fsaJetFlavor == 5:
                if jetPt > 30 and jetPt < 120:
                    scaleFactor = scaleFactorFunction(0.9293,0,0,0,jetPt)
                elif jetPt > 120 and jetPt < 180:
                    scaleFactor = scaleFactorFunction(0.98566,0,0,0,jetPt)
                elif jetPt > 180 and jetPt < 240:
                    scaleFactor = scaleFactorFunction(0.95986,0,0,0,jetPt)
                elif jetPt > 240 and jetPt < 450:
                    scaleFactor = scaleFactorFunction(0.96968,0,0,0,jetPt)            
            elif fsaJetFlavor > 0:
                scaleFactor = scaleFactorFunction(1.40572,-0.00106955,+2.22422e-06,-1.39402e-09,jetPt)
            else:
                return 0
        else:
            return 0

    return scaleFactor
