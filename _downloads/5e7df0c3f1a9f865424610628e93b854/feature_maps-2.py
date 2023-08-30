from squlearn.feature_map import QEKFeatureMap, ChebPQC
fm1 = QEKFeatureMap(num_qubits=4, num_features=2, num_layers=1, closed=False)
fm2 = ChebPQC(num_qubits=4, num_features=3, num_layers=1)
# Combining both feature maps
fm3 = fm1 + fm2
fm3.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()