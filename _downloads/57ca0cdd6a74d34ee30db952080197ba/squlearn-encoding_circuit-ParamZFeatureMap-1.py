from squlearn.encoding_circuit import ParamZFeatureMap
pqc = ParamZFeatureMap(num_qubits=4, num_layers=2, entangling=True)
plt = pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10}, num_features=2)
plt.tight_layout()