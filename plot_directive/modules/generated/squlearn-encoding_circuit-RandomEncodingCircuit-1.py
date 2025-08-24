from squlearn.encoding_circuit import RandomEncodingCircuit
pqc = RandomEncodingCircuit(num_qubits=4, seed = 2)
pqc._gen_random_config(num_features=6, seed=2)
plt = pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10}, num_features=6)
plt.tight_layout()