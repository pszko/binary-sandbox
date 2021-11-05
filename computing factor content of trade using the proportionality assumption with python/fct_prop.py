import json
import pandas as pd
import numpy as np

script_dir = os.path.dirname(__file__)
rel_path = "data/"
path = os.path.join(script_dir, rel_path)

# ---Reading VDFM dataset
VDFM = pd.read_excel(path + 'VDFM.xlsx')

# ---Lowercasing output sector values
VDFM['dim1'] = VDFM['dim1'].str.lower()
VDFM['dim2'] = VDFM['dim2'].str.lower()

# ---Uppercasing country values
VDFM['dim3'] = VDFM['dim3'].str.upper()

# ---Extracting unique values from dimensions
VDFM_dim1 = VDFM['dim1'].unique()
VDFM_dim1.sort()
output_sector = VDFM_dim1.tolist()

VDFM_dim2 = VDFM['dim2'].unique()
VDFM_dim2.sort()
input_sector = VDFM_dim2.tolist()

VDFM_dim3 = VDFM['dim3'].unique()
VDFM_dim3.sort()
output_input_country = VDFM_dim3.tolist()

# ---Removing final demand
final_demand = {'c', 'g', 'i'}
input_sector = [sector for sector in input_sector if sector not in final_demand]

# ---Creating a list of ig and jh
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

# ---Renaming Values in dim3 - dim1 and dim3 - dim2
VDFM['ig'] = VDFM['dim3'] + "-" + VDFM['dim1']
VDFM['jh'] = VDFM['dim3'] + "-" + VDFM['dim2']
VDFM = VDFM[['ig', 'jh', 'Value']]
VDFM = VDFM.sort_values(by=['ig', 'jh'])

# ---Creating null matrix of size ig*jh
blank_VDFM_igjh = np.zeros((len(outputCountry_outputSector), len(inputCountry_inputSector)))

# ---Creating null dataframe VDFM_igjh
VDFM_igjh = pd.DataFrame(data=blank_VDFM_igjh, index = outputCountry_outputSector, columns = inputCountry_inputSector)
VDFM_igjh.apply(pd.to_numeric)

# ---Populating VDFM_igjh matrix with VXMD table values
for index, row in VDFM.iterrows():
    VDFM_igjh.loc[row['ig'], row['jh']] = row['Value']

# ---Lowercasing output sector values
VXMD['dim1'] = VXMD['dim1'].str.lower()

# ---Uppercasing country values
VXMD['dim2'] = VXMD['dim2'].str.upper()
VXMD['dim3'] = VXMD['dim3'].str.upper()

# ---Renaming Values in dim1 - dim2 and dim 3
VXMD['ig'] = VXMD['dim2'] + "-" + VXMD['dim1']
VXMD['j'] = VXMD['dim3']
VXMD = VXMD[['ig', 'j', 'Value']]
VXMD = VXMD.sort_values(by=['ig', 'j'])

# ---Creating null matrix of size ig*jh
blank_VXMD_igj = np.zeros((len(list_ig), len(list_j)))

# ---Creating null dataframe VXMD_igj
VXMD_igj = pd.DataFrame(data=blank_VXMD_igj, index=list_ig, columns=list_j)
VXMD_igj.apply(pd.to_numeric)

# ---Populating VXMD_igj matrix with VXMD table values
for index, row in VXMD.iterrows():
    VXMD_igj.loc[row['ig'], row['j']] = row['Value']

# ---Lowercasing sector values
VIFM['dim1'] = VIFM['dim1'].str.lower()
VIFM['dim2'] = VIFM['dim2'].str.lower()

# ---Uppercasing country values
VIFM['dim3'] = VIFM['dim3'].str.upper()

# ---Renaming Values in dim1 and dim3 - dim 2
VIFM['g'] = VIFM['dim1']
VIFM['jh'] = VIFM['dim3'] + "-" + VIFM['dim2']

# ---Outputting VIFM_2d
VIFM_gjh= VIFM[['g', 'jh', 'Value']]
VIFM_gjh= VIFM_gjh.sort_values(by=['g', 'jh'])

# ---Lowercasing sector values
VFM['dim2'] = VFM['dim2'].str.lower()

# ---Uppercasing country values
VFM['dim3'] = VFM['dim3'].str.upper()

# ---Renaming Values in dim1 and dim3 - dim 2
VFM['f'] = VFM['dim1']
VFM['jh'] = VFM['dim3'] + "-" + VFM['dim2']
VFM = VFM[['f', 'jh', 'Value']]
VFM = VFM.sort_values(by=['f', 'jh'])

# ---Creating null matrix of size f*jh
blank_VFM_fjh = np.zeros((len(list_f), len(list_jh)))

# ---Creating null dataframe VFM_fjh
VFM_fjh = pd.DataFrame(data=blank_VFM_fjh, index=list_f, columns=list_jh)
VFM_fjh.apply(pd.to_numeric)

# ---Populating VFM_fjh matrix with VFM table values
for index, row in VFM.iterrows():
    VFM_fjh.loc[row['f'], row['jh']] = row['Value']

# ---Outputting output sector (g) values
VDFM['dim1'] = VDFM['dim1'].str.lower()
VDFM_dim1 = VDFM['dim1'].unique()
VDFM_dim1.sort()
list_g = VDFM_dim1.tolist()

# ---Outputting output/input country (j) values
VDFM['dim3'] = VDFM['dim3'].str.upper()
VDFM_dim3 = VDFM['dim3'].unique()
VDFM_dim3.sort()
list_j = VDFM__c_dim3.tolist()

# ---Creating combinations of ouput country (i) / output sector (g)
list_ig = []
for i in VDFM__c_dim3:
    for g in VDFM__c_dim1:
        x = i + '-'+ g
        list_ig.append(x)

# ---Creating combinations of input country (j) / input sector (h)
list_jh = []
for j in VDFM__c_dim3:
    for h in VDFM__c_dim2:
        x = j + '-'+ h
        list_jh.append(x)

# ---Outputting unique factor (f) values
VFM['dim1'] = VFM['dim1'].str.upper()
VFM_dim1 = VFM['dim1'].unique()
VFM_dim1.sort()
list_f = VFM_dim1.tolist()

# ---Determining bilateral trade constraints
VXMD_dict = {}
VXMD = {}
for sector in list_g:
    VXMD_dict[sector] = VXMD_igj.loc[np.where(VXMD_igj['Unnamed: 0'].str.contains(sector))]
    VXMD_dict[sector] = VXMD_dict[sector].set_index('Unnamed: 0')
    for country in list_j:
        a = sector + "-" + country
        VXMD[a] = VXMD_dict[sector].filter(regex=country)

# ---Determining input-output constraints
VIFM = {}
VIFM_sum = {}
for sector in list_g:
    VIFM_sec = VIFM_gjh.loc[np.where(VIFM_gjh['g'].str.contains(sector))]
    VIFM_sec = VIFM_sec.reset_index(drop=True)
    for country in list_j:
        a = sector + "-" + country
        VIFM[a] = VIFM_sec.loc[np.where(VIFM_sec['jh'].str.contains(country))]
        VIFM_sum[a] = sum(VIFM[a]["Value"])

# ---Imputing imported input-output matrices
tz_b = VDFM_igjh.copy()
for sector in list_g:
    for country in list_j:
        a = sector + "-" + country
        try:
            for index_io, row_io in VIFM[a].iterrows():
                calc = row_io[2] / VIFM_sum[a]
                if calc == 0:
                    continue
                else:
                    try:
                        y = VXMD[a]
                        for index_trade, row_trade in VXMD[a].iterrows():
                            if row_trade[0] == 0:
                                continue
                            else:
                                val = calc * row_trade[0]
                                tz_b.loc[index_trade, row_io[1]] = val
                    except:
                            print("VXMD[",a,"] not in scope")
        except:
            print("VIFM[",a,"] not in scope")
tz_b = tz_b[list_jh].values

# ---Transforming required data
VDFM_igjh = VDFM_igjh.values
VXMD_igj = VXMD_igj.set_index('Unnamed: 0')
VXMD_igj = VXMD_igj.values

# ---Removing domestic input-outputs
prop_tech = tz_b - VDFM_igjh

# ---Summing imports over j
imports_dict = {}
for j in range(len(list_j)):
    imports_dict[j] = prop_tech[j*57: j*57+56, :].sum(0)
imports = imports_dict[0]
for x in range(1, len(list_j)):
    imports = np.vstack((imports, imports_dict[x]))

# ---Transposing imports
imports = imports.transpose()

# ---Removing imports from exports
trade = VXMD_igj - imports

# ---Defining {F_i  = D〖(I-B)〗^(-1) T_i}
def leontief(VFM, box, trade):
    c = VFM.sum(axis = 0) + box.sum(axis = 0)
    io_mx = np.divide(1, c, out=np.zeros_like(c), where=c!=0)
    factors = VFM * io_mx
    io = box * io_mx
    I = np.identity(io.shape[0], dtype = float)
    B = I - io
    return np.matmul(factors, np.linalg.solve(B,trade))

# ---Calculating proportionality factor content of trade
fct = leontief(VFM, tz_b, trade)

# ---Outputting factor content of trade
fct_prop = pd.DataFrame(data=fct, index = list_f, columns = list_j)
fct_prop.to_csv(path + 'FCT_prop.csv')
