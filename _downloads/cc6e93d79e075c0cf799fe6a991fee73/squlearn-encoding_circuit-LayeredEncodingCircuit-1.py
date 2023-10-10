from squlearn.encoding_circuit import LayeredEncodingCircuit
encoding_circuit = LayeredEncodingCircuit(num_qubits=4,num_features=2)
encoding_circuit.H()
encoding_circuit.Rz("x")
encoding_circuit.Ry("p")
encoding_circuit.cx_entangling("NN")
encoding_circuit.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()