from squlearn.encoding_circuit import QEKEncodingCircuit
pqc = QEKEncodingCircuit(num_qubits=4, num_features=2, num_layers=2)
pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()