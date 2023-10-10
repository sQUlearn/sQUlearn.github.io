from squlearn.encoding_circuit import LayeredEncodingCircuit
from squlearn.encoding_circuit.layered_encoding_circuit import Layer
encoding_circuit = LayeredEncodingCircuit(num_qubits=4,num_features=2)
encoding_circuit.H()
layer = Layer(encoding_circuit)
layer.Rz("x")
layer.Ry("p")
layer.cx_entangling("NN")
encoding_circuit.add_layer(layer,num_layers=3)
encoding_circuit.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()