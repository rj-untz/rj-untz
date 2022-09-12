import numpy as np

upstart = [21000, 610, 50]
lightstream = [13000, 331, 24]
jeep_loan = [23000, 440, 55]

np_upstart = np.array(upstart)
np_lightstream = np.array(lightstream)
np_jeep = np.array(jeep_loan)

np_loans = np.vstack((np_upstart,np_lightstream,np_jeep))

