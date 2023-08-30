import numpy as np
from squlearn.feature_map import LayeredFeatureMap

def func(a,b):
    return a*np.arccos(b)

feature_map = LayeredFeatureMap(num_qubits=4,num_features=2)
feature_map.H()
feature_map.Rz("p","x",encoding=func)
feature_map.cx_entangling("NN")
feature_map.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()