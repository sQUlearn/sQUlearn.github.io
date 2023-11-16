from squlearn.encoding_circuit import ChebyshevTower
pqc = ChebyshevTower(4, 2, 2, num_layers=2)
pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()