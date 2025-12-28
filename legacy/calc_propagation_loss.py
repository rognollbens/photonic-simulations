#!/usr/bin/env python
"""
Older script to calculate propagation loss in chalcogenide waveguides.
Uses effective index method and material parameters.
"""

import numpy as np
from pylab import *

def calc_loss(wavelength, width, height, n_core, n_clad, L):
    # Compute effective index and loss
    k0 = 2 * np.pi / wavelength
    V = k0 * width * np.sqrt(n_core**2 - n_clad**2)
    # Approximate effective index
    neff = n_clad + (n_core - n_clad) * (1 - np.exp(-V/2))
    # Propagation loss coefficient alpha (dB/cm)
    alpha = 4.34 * k0 * (n_core - neff) / (neff * L)  # rough approximation
    return alpha, neff

def main():
    # Default parameters for As2S3 waveguide
    wavelength = 1.55e-6  # meters
    width = 0.5e-6        # meters
    height = 0.22e-6      # meters
    n_core = 2.4          # chalcogenide refractive index
    n_clad = 1.444        # silica cladding
    lengths = np.linspace(1e-3, 10e-3, 50)  # 1 mm to 10 mm
    
    alphas = []
    neffs = []
    for L in lengths:
        a, neff = calc_loss(wavelength, width, height, n_core, n_clad, L)
        alphas.append(a)
        neffs.append(neff)
    
    # Plotting using old pylab interface
    figure()
    subplot(2,1,1)
    plot(lengths*1e3, alphas, 'b-')
    xlabel('Waveguide Length (mm)')
    ylabel('Propagation Loss (dB/cm)')
    title('Propagation Loss vs Length')
    grid(True)
    
    subplot(2,1,2)
    plot(lengths*1e3, neffs, 'r--')
    xlabel('Waveguide Length (mm)')
    ylabel('Effective Index')
    title('Effective Index vs Length')
    grid(True)
    
    tight_layout()
    show()

if __name__ == '__main__':
    main()