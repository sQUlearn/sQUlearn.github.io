from squlearn.encoding_circuit import KyriienkoEncodingCircuit
pqc = KyriienkoEncodingCircuit(4, num_encoding_layers=1, num_variational_layers=2,
                               variational_arrangement="ABA")
pqc.draw(output="mpl", style={'fontsize':15,'subfontsize': 10}, num_features=1)