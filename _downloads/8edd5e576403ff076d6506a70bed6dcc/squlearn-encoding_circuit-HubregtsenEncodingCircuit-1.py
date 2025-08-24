from squlearn.encoding_circuit import HubregtsenEncodingCircuit
pqc = HubregtsenEncodingCircuit(4, 2)
plt = pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10}, num_features=2)
plt.tight_layout()