# Data Reference: Post, W.M., and L. Zobler. 2000. Global Soil Types, 0.5-Degree Grid (Modified Zobler). ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/540

import numpy as np
import pandas as pd

def read_contizob_half(file_path):
    data = np.loadtxt(file_path, dtype=int)
    return data

contizob_half_path = '/content/contizob.half'

contizob_data = read_contizob_half(contizob_half_path)

# Extract continent codes and soil types
continent_codes = contizob_data[:, 0]
soil_types = contizob_data[:, 1]

# Define grid parameters manually since we do not have a header in contizob.half
nrows = 360  # Number of rows in the data (derived from the 0.5-degree grid covering 180 degrees)
ncols = 720  # Number of columns in the data (derived from the 0.5-degree grid covering 360 degrees)
xllcorner = -180.0  # Lower-left corner x-coordinate
yllcorner = -90.0   # Lower-left corner y-coordinate
cellsize = 0.5      # Size of each cell

# Generate latitude and longitude values
latitudes = np.linspace(yllcorner + (nrows - 1) * cellsize, yllcorner, nrows)
longitudes = np.linspace(xllcorner, xllcorner + (ncols - 1) * cellsize, ncols)

# Create a meshgrid for latitude and longitude
lon_grid, lat_grid = np.meshgrid(longitudes, latitudes)

# Flatten the data for easier handling
lat_grid_flat = lat_grid.flatten()
lon_grid_flat = lon_grid.flatten()
continent_codes_flat = continent_codes.flatten()
soil_types_flat = soil_types.flatten()

# Create a DataFrame
df_contizob = pd.DataFrame({
    'latitude': lat_grid_flat,
    'longitude': lon_grid_flat,
    'continent_code': continent_codes_flat,
    'soil_type': soil_types_flat
})

# Dictionaries for soil type and continent codes
soil_type_dict = {
    0: "WATER", 1: "AF FERRIC ACRISOL", 2: "AG GLEYIC ACRISOL", 3: "AH HUMIC ACRISOL",
    4: "AO ORTHIC ACRISOL", 5: "AP PLINTHIC ACRISOL", 6: "BC CHROMIC CAMBISOL",
    7: "BD DYSTRIC CAMBISOL", 8: "BE EUTRIC CAMBISOL", 9: "BF FERRALIC CAMBISOL",
    10: "BG GLEYIC CAMBISOL", 11: "BH HUMIC CAMBISOL", 12: "BK CALCIC CAMBISOL",
    13: "BV VERTIC CAMBISOL", 14: "BX GELIC CAMBISOL", 15: "CG GLOSSIC CHERNOZEM",
    16: "CH HAPLIC CHERNOZEM", 17: "CK CALCIC CHERNOZEM", 18: "CL LUVIC CHERNOZEM",
    19: "DD DYSTRIC PODZOLUVISOL", 20: "DE EUTRIC PODZOLUVISOL", 21: "DG GLEYIC PODZOLUVISOL",
    22: "E RENDZINA", 23: "FA ACRIC FERRALSOL", 24: "FH HUMIC FERRALSOL", 25: "FO ORTHIC FERRALSOL",
    26: "FP PLINTHIC FERRALSOL", 27: "FR RHODIC FERRALSOL", 28: "FX XANTHIC FERRALSOL",
    29: "GC CALCARIC GLEYSOL", 30: "GD DYSTRIC GLEYSOL", 31: "GE EUTRIC GLEYSOL",
    32: "GH HUMIC GLEYSOL", 33: "GM MOLLIC GLEYSOL", 34: "GP PLINTHIC GLEYSOL",
    35: "GX GELIC GLEYSOL", 36: "HC CALCARIC PHAEOZEM", 37: "HG GLEYIC PHAEOZEM",
    38: "HH HAPLIC PHAEOZEM", 39: "HL LUVIC PHAEOZEM", 40: "I LITHOSOL",
    41: "JC CALCARIC FLUVISOL", 42: "JD DYSTRIC FLUVISOL", 43: "JE EUTRIC FLUVISOL",
    44: "JT THIONIC FLUVISOL", 45: "KH HAPLIC KASTANOZEM", 46: "KK CALCIC KASTANOZEM",
    47: "KL LUVIC KASTANOZEM", 48: "LA ALBIC LUVISOL", 49: "LC CHROMIC LUVISOL",
    50: "LF FERRIC LUVISOL", 51: "LG GLEYIC LUVISOL", 52: "LK CALCIC LUVISOL",
    53: "LO ORTHIC LUVISOL", 54: "LP PLINTHIC LUVISOL", 55: "LV VERTIC LUVISOL",
    56: "MG GLEYIC GREYZEM", 57: "MO ORTHIC GREYZEM", 58: "ND DYSTRIC NITOSOL",
    59: "NE EUTRIC NITOSOL", 60: "NH HUMIC NITOSOL", 61: "OD DYSTRIC HISTOSOL",
    62: "OE EUTRIC HISTOSOL", 63: "OX GELIC HISTOSOL", 64: "PF FERRIC PODZOL",
    65: "PG GLEYIC PODZOL", 66: "PH HUMIC PODZOL", 67: "PL LEPTIC PODZOL",
    68: "PO ORTHIC PODZOL", 69: "PP PLACIC PODZOL", 70: "QA ALBIC ARENOSOL",
    71: "QC CAMBIC ARENOSOL", 72: "QF FERRALIC ARENOSOL", 73: "QL LUVIC ARENOSOL",
    74: "RC CALCARIC REGOSOL", 75: "RD DYSTRIC REGOSOL", 76: "RE EUTRIC REGOSOL",
    77: "RX GELIC REGOSOL", 78: "SG GLEYIC SOLONETZ", 79: "SM MOLLIC SOLONETZ",
    80: "SO ORTHIC SOLONETZ", 81: "TH HUMIC ANDOSOL", 82: "TM MOLLIC ANDOSOL",
    83: "TO OCHRIC ANDOSOL", 84: "TV VITRIC ANDOSOL", 85: "U RANKER",
    86: "VC CHROMIC VERTISOL", 87: "VP PELLIC VERTISOL", 88: "WD DYSTRIC PLANOSOL",
    89: "WE EUTRIC PLANOSOL", 90: "WH HUMIC PLANOSOL", 91: "WM MOLLIC PLANOSOL",
    92: "WS SOLODIC PLANOSOL", 93: "WX GELIC PLANOSOL", 94: "XH HAPLIC XEROSOL",
    95: "XK CALCIC XEROSOL", 96: "XL LUVIC XEROSOL", 97: "XY GYPSIC XEROSOL",
    98: "YH HAPLIC YERMOSOL", 99: "YK CALCIC YERMOSOL", 100: "YL LUVIC YERMOSOL",
    101: "YT TAKYRIC YERMOSOL", 102: "YY GYPSIC YERMOSOL", 103: "ZG GLEYIC SOLONCHAK",
    104: "ZM MOLLIC SOLONCHAK", 105: "ZO ORTHIC SOLONCHAK", 106: "ZT TAKYRIC SOLONCHAK",
    107: "ICE GLACIER/ICE"
}

continent_code_dict = {
    0: "OCEAN",
    1: "not used",
    2: "NAMERICA",
    3: "MEXICEAM",
    4: "SAMERICA",
    5: "EUROPE",
    6: "AFRICA",
    7: "SCASIA",
    8: "NCASIA",
    9: "SEASIA",
    10: "AUSTRALI"
}

#Map the codes to names

df_contizob['soil_type_name'] = df_contizob['soil_type'].map(soil_type_dict)
df_contizob['continent_name'] = df_contizob['continent_code'].map(continent_code_dict)

#Display the DataFrame

print(df_contizob.tail(150))

csv_output_path = 'soil_data_with_names.csv'
df_contizob.to_csv(csv_output_path, index=False)

