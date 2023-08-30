from squlearn.feature_map import YZ_CX_FeatureMap
pqc = YZ_CX_FeatureMap(4, 4, 2, c=2.0)
plt = pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()