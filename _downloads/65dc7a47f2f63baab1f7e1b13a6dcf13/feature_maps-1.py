from squlearn.feature_map import QEKFeatureMap
pqc = QEKFeatureMap(num_qubits=4, num_features=2, num_layers=2)
pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()