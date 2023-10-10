from squlearn.encoding_circuit import QiskitEncodingCircuit
from qiskit.circuit.library import TwoLocal
local = TwoLocal(3, 'ry', 'cx', 'linear', reps=2, insert_barriers=True)
pqc = QiskitEncodingCircuit(local)
pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()