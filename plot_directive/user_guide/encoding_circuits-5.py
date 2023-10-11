from squlearn.encoding_circuit import LayeredEncodingCircuit
encoding_circuit = LayeredEncodingCircuit.from_string(
   "Ry(p)-3[Rx(p,x;=y*np.arccos(x),{y,x})-crz(p)]-Ry(p)", num_qubits=4, num_features=1
)
plt = encoding_circuit.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()