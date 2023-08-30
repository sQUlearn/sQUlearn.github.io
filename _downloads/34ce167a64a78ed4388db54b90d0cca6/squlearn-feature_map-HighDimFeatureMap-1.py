from squlearn.feature_map import HighDimFeatureMap
pqc = HighDimFeatureMap(5, 23, num_layers=2)
pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()