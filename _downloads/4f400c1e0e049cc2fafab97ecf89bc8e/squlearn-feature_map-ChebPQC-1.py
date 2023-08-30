from squlearn.feature_map import ChebPQC
pqc = ChebPQC(4, 2, 2)
pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()