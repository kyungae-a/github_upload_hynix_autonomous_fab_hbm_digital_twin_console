* public-model DRAM read path charge-sharing proxy
Vpre bl 0 0.5
Ccell cell 0 30f
Cbl bl 0 260f
Raccess cell bl 2k
.tran 1p 2n
.print tran v(bl) v(cell)
.end
