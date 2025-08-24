from squlearn.encoding_circuit import ChebyshevRx
pqc = ChebyshevRx(4, 2)
pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10}, num_features=2)
plt.tight_layout()