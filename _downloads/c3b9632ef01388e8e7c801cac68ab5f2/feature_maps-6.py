from squlearn.feature_map import LayeredFeatureMap, automated_pruning
from squlearn.util import Executor
feature_map = LayeredFeatureMap.from_string("Rz(p)-Ry(p)-Z-Ry(p)-Rz(p)", num_qubits=2, num_features=0)
pruned_feature_map = automated_pruning(feature_map, Executor("statevector_simulator"))
pruned_feature_map.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()