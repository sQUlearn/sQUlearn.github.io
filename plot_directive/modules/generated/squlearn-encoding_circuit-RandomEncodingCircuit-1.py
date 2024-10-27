from squlearn.encoding_circuit import RandomEncodingCircuit
pqc = RandomEncodingCircuit(num_qubits=4, num_features=6, seed = 2)
plt = pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()