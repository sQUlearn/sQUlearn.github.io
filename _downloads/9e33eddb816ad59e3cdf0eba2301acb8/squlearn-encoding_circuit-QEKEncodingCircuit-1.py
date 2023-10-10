from squlearn.encoding_circuit import QEKEncodingCircuit
pqc = QEKEncodingCircuit(4, 2, 2)
plt = pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()