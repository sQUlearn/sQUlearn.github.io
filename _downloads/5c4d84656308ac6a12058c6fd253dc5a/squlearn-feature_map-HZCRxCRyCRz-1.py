from squlearn.feature_map import HZCRxCRyCRz
pqc = HZCRxCRyCRz(4, 2, 1)
pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()