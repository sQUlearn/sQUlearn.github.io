import numpy as np
from squlearn.encoding_circuit import LayeredEncodingCircuit

def func(a,b):
    return a*np.arccos(b)

encoding_circuit = LayeredEncodingCircuit(num_qubits=4,num_features=2)
encoding_circuit.H()
encoding_circuit.Rz("p","x",encoding=func)
encoding_circuit.cx_entangling("NN")
encoding_circuit.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()