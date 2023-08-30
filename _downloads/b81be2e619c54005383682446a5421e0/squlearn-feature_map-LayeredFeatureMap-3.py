from squlearn.feature_map import LayeredFeatureMap
from squlearn.feature_map.layered_feature_map import Layer
feature_map = LayeredFeatureMap(num_qubits=4,num_features=2)
feature_map.H()
layer = Layer(feature_map)
layer.Rz("x")
layer.Ry("p")
layer.cx_entangling("NN")
feature_map.add_layer(layer,num_layers=3)
feature_map.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()