from squlearn.encoding_circuit import LayeredEncodingCircuit, automated_pruning
from squlearn.util import Executor
encoding_circuit = LayeredEncodingCircuit.from_string("Rz(p)-Ry(p)-Z-Ry(p)-Rz(p)", num_qubits=2, num_features=0)
pruned_encoding_circuit = automated_pruning(encoding_circuit, Executor("statevector_simulator"))
pruned_encoding_circuit.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()