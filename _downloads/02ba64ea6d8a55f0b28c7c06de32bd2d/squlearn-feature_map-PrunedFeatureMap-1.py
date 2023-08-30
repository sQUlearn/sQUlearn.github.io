from squlearn.feature_map import QEKFeatureMap,PrunedFeatureMap
fm = QEKFeatureMap(4,2,2)
plt = fm.draw(output="mpl")
plt.suptitle("QEK Feature Map", x=0.55, y=0.88, fontsize=14, ha='center', va='center')
plt.tight_layout()
plt2 = PrunedFeatureMap(fm,[4,7,11,15]).draw(output="mpl")
plt2.suptitle("Pruned Feature Map", x=0.55, y=0.88, fontsize=14, ha='center', va='center')
plt2.tight_layout()