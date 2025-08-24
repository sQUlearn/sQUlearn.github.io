from squlearn.encoding_circuit import HighDimEncodingCircuit
pqc = HighDimEncodingCircuit(5, num_layers=2)
pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10}, num_features=23)
plt.tight_layout()