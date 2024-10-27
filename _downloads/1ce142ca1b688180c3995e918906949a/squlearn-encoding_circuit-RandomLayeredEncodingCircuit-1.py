from squlearn.encoding_circuit import RandomLayeredEncodingCircuit
pqc = RandomLayeredEncodingCircuit(num_qubits=4, num_features=6)
plt = pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()