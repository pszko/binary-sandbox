import numpy as np

tot_output = np.array([5000, 10000])
flow_tbl = np.array([[350, 400], [275, 100]])
mx_a = flow_tbl.dot(np.linalg.inv(tot_output * np.identity(2)))
print(mx_a)

mx_b = np.linalg.inv(np.identity(2) - mx_A)
print(mx_b)
