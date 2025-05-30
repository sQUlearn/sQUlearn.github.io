import numpy as np
import matplotlib.pyplot as plt
from squlearn import Executor
from squlearn.encoding_circuit import ChebyshevRx
from squlearn.observables import IsingHamiltonian
from squlearn.qnn import QNNRegressor, SquaredLoss
from squlearn.optimizers import SLSQP
nqubits = 4
number_of_layers = 2
pqc = ChebyshevRx(nqubits, 1, num_layers=number_of_layers)
exe = Executor("pennylane", seed=0)
exe.set_shots(5000)
ising_op = IsingHamiltonian(nqubits, I="S", Z="S", ZZ="S")
param = np.array([ 0.91858145, -1.1163345,   0.38467092,  1.39597102,  1.10224011,  2.41369111,
1.64968778, -0.81903595,  0.4867727,   0.38505193,  1.10635672,  0.72867129,
-1.74881862, -0.64411871,  0.86344117, -0.91471452])
param_op = np.array([-0.47157523,  5.10755673,  2.63075629])
qnn = QNNRegressor(pqc, ising_op, exe, SquaredLoss, SLSQP(), param, param_op, pretrained=True)
x = np.arange(np.min(0.1), np.max(0.8), 0.005).reshape(-1, 1)
y = qnn.predict(x)
plt.plot(x, np.log(x))
plt.plot(x, y)
plt.title("QNN inference without variance regularization")
plt.legend([r"$\log(x)$", r"$f(\theta, x)$"])
plt