from squlearn.encoding_circuit import ParamZEncodingCircuit
pqc = ParamZEncodingCircuit(4, 2, num_layers=2, entangling=True)
plt = pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()