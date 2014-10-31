#!/usr/bin/env python
# =============================================================================

import sys
import os.path
import optparse
import time
import math

import ROOT
import rootlogon
import metaroot

# =============================================================================
x_min = 0
x_max = 15

y_min = 0
y_max = 0.35

sig_mean = 6
sig_sigma = 2
sig_norm = 1./(math.sqrt(2*3.14) * sig_sigma)

bkg_mean = 10
bkg_sigma = 1.5
bkg_norm = 1./(math.sqrt(2*3.14) * bkg_sigma)

cut_value = 7

# =============================================================================
def main():
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    c = ROOT.TCanvas()

    frame = ROOT.TH2F( 'dummy_frame'
                     , 'Likelihood ratio ; Test statistic ; Probability density'
                     , 1, x_min, x_max
                     , 1, y_min, y_max
                     )
    frame.Draw()

    p_bkg = ROOT.TF1('g1', 'gaus', x_min, cut_value)
    p_bkg.SetParameters(bkg_norm, bkg_mean, bkg_sigma);

    p_sig = ROOT.TF1('g2', 'gaus', cut_value, x_max)
    p_sig.SetParameters(sig_norm, sig_mean, sig_sigma);

    g_bkg = ROOT.TF1('g1', 'gaus', x_min, x_max)
    g_bkg.SetParameters(bkg_norm, bkg_mean, bkg_sigma);

    g_sig = ROOT.TF1('g2', 'gaus', x_min, x_max)
    g_sig.SetParameters(sig_norm, sig_mean, sig_sigma);

    line = ROOT.TLine(cut_value, y_min, cut_value, 0.7*y_max)

    p_sig.SetFillStyle(1111)
    p_bkg.SetFillStyle(1111)
    p_sig.SetFillColor(ROOT.kGreen)
    p_bkg.SetFillColor(ROOT.kYellow)

    p_sig.SetLineColor(ROOT.kWhite)
    p_bkg.SetLineColor(ROOT.kWhite)
    g_sig.SetLineColor(ROOT.kBlack)
    g_bkg.SetLineColor(ROOT.kBlue)
    line.SetLineColor(ROOT.kRed)

    g_sig.SetLineWidth(2)
    g_bkg.SetLineWidth(2)
    line.SetLineWidth(2)

    g_sig.SetLineStyle(ROOT.kDashed)
    g_bkg.SetLineStyle(ROOT.kDashed)

    p_sig.Draw('FCSAME')
    p_bkg.Draw('FCSAME')
    g_sig.Draw('LSAME')
    g_bkg.Draw('LSAME')
    line.Draw('LSAME')

    leg = metaroot.hist.make_legend( [line, g_bkg, g_sig]
                                   , ['Observed'
                                     , 'Expected for background'
                                     , 'Expected for signal+background'
                                     ]
                                   , ['L']*3
                                   , x1 = 0.2
                                   , x2 = 0.65
                                   , y1 = 0.7
                                   , y2 = 0.95
                                   )
    leg.Draw()

    c.Print('CLs.png')

# =============================================================================
if __name__ == '__main__':
    main()
