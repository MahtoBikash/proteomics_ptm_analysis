# ptm_analysis.py
from pyteomics import mzml
import pandas as pd
import matplotlib.pyplot as plt

# Load a sample mzML file (mass spec data)
file = "sample.mzML"   # replace with actual path

spectra = mzml.read(file)

mz_values = []
intensities = []

# Extract first 500 spectra for testing
for i, spec in enumerate(spectra):
    if i > 500:
        break
    if 'm/z array' in spec and 'intensity array' in spec:
        mz_values.extend(spec['m/z array'])
        intensities.extend(spec['intensity array'])

# Convert to dataframe
df = pd.DataFrame({
    "m/z": mz_values,
    "intensity": intensities
})

# Plot spectrum
plt.figure(figsize=(10,6))
plt.stem(df["m/z"], df["intensity"], linefmt="C0-", markerfmt=" ", basefmt=" ")
plt.xlabel("m/z")
plt.ylabel("Intensity")
plt.title("Mass Spectrum (first 500 scans)")
plt.show()
