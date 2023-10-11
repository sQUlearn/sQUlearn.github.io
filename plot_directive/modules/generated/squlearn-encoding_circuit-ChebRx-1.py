from squlearn.encoding_circuit import ChebRx
pqc = ChebRx(4, 2, 2)
pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10})
plt.tight_layout()