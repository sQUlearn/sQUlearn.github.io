from squlearn.encoding_circuit import ChebyshevTower
pqc = ChebyshevTower(4, 2, num_layers=2)
pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10}, num_features=2)
plt.tight_layout()