import numpy as np
import matplotlib.pyplot as plt
from squlearn import Executor
from squlearn.encoding_circuit import ChebRx
from squlearn.observables import IsingHamiltonian
from squlearn.qnn import QNNRegressor, SquaredLoss
from squlearn.optimizers import SLSQP
nqubits = 4
number_of_layers = 2
pqc = ChebRx(nqubits, 1, num_layers=number_of_layers)
qasm = Executor("qasm_simulator")
qasm.set_shots(5000)
ising_op = IsingHamiltonian(nqubits, I="S", Z="S", ZZ="S")
param = np.array([ 3.41062806,  0.63125445,  4.40119971,  1.25919873, -2.35420942, -0.04354262,
-4.22612537, -0.19520602,  0.21838745,  0.78754811,  3.05189136,  0.59189901,
-0.52783347, -1.55477309, -2.08338942, -0.29088459])
param_op = np.array([-1.57350653,  0.87778247, -0.26884315])
qnn_qasm = QNNRegressor(pqc, ising_op, qasm, SquaredLoss, SLSQP(), param, param_op, precomputed=True)
x = np.arange(np.min(0.1), np.max(0.8), 0.005)
y = qnn_qasm.predict(x)
plt.plot(x, np.log(x))
plt.plot(x, y)
plt.title("QNN inference with variance regularization")
plt.legend([r"$\log(x)$", r"$f(\theta, x)$"])
plt