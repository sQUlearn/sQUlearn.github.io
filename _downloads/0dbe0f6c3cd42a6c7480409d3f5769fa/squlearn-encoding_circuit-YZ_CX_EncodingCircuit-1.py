from squlearn.encoding_circuit import YZ_CX_EncodingCircuit
pqc = YZ_CX_EncodingCircuit(4, 4, 2, c=2.0)
plt = pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()