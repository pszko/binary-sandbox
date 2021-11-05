import os
import pandas as pd
import numpy as np


script_dir = os.path.dirname(__file__)
rel_path = ""
path = os.path.join(script_dir, rel_path)

VDFM = pd.read_excel (path + 'VDFM.xlsx')

VDFM['dim1'] = VDFM['dim1'].str.lower()
VDFM['dim2'] = VDFM['dim2'].str.lower()
VDFM['dim3'] = VDFM['dim3'].str.upper()

VDFM_dim1 = VDFM['dim1'].unique()
VDFM_dim1.sort()
output_sector = VDFM_dim1.tolist()
# ---
VDFM_dim2 = VDFM['dim2'].unique()
VDFM_dim2.sort()
input_sector = VDFM_dim2.tolist()
# ---
VDFM_dim3 = VDFM['dim3'].unique()
VDFM_dim3.sort()
output_input_country = VDFM_dim3.tolist()

final_demand = {'c', 'g', 'i'}
input_sector = [sector for sector in input_sector if sector not in final_demand]

outputCountry_outputSector = []
for i in output_input_country:
    for g in output_sector:
        x = i + '-'+ g
        outputCountry_outputSector.append(x)

inputCountry_inputSector = []
for j in output_input_country:
    for h in input_sector:
        x = j + '-'+ h
        inputCountry_inputSector.append(x)

VDFM['ig'] = VDFM['dim3'] + "-" + VDFM['dim1']
VDFM['jh'] = VDFM['dim3'] + "-" + VDFM['dim2']

VDFM = VDFM[['ig', 'jh', 'Value']]

VDFM = VDFM.sort_values(by=['ig', 'jh'])

blank_VDFM_igjh = np.zeros((len(outputCountry_outputSector), len(inputCountry_inputSector)))

VDFM_igjh = pd.DataFrame(data=blank_VDFM_igjh, index = outputCountry_outputSector, columns = inputCountry_inputSector)

VDFM_igjh.apply(pd.to_numeric)

for index, row in VDFM.iterrows():
    VDFM_igjh.loc[row['ig'], row['jh']] = row['Value']

VDFM_mx = VDFM_igjh.to_numpy()
