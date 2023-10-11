from squlearn.encoding_circuit import QEKEncodingCircuit,PrunedEncodingCircuit
fm = QEKEncodingCircuit(4,2,2)
plt = fm.draw(output="mpl")
plt.suptitle("QEK Encoding Circuit", x=0.55, y=0.88, fontsize=14, ha='center', va='center')
plt.tight_layout()
plt2 = PrunedEncodingCircuit(fm,[4,7,11,15]).draw(output="mpl")
plt2.suptitle("Pruned Encoding Circuit", x=0.55, y=0.88, fontsize=14, ha='center', va='center')
plt2.tight_layout()