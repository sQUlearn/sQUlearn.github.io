from squlearn.feature_map import QiskitZFeatureMap
pqc = QiskitZFeatureMap(4, reps=2)
plt = pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()