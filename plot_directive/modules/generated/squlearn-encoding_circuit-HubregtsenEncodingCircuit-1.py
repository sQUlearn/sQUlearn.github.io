from squlearn.encoding_circuit import HubregtsenEncodingCircuit
pqc = HubregtsenEncodingCircuit(4, 2, 2)
plt = pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()