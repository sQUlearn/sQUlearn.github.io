from squlearn.encoding_circuit import TranspiledEncodingCircuit,ChebRx
from qiskit.providers.fake_provider import FakeManilaV2
fm = TranspiledEncodingCircuit(ChebRx(3,1),backend=FakeManilaV2(),initial_layout=[0,1,4])
plt = fm.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()