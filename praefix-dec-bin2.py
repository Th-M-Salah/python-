""" Dezimale und Bnärepräfixe im Vergleich """
"""Decimals and Binary prefixes compared"""
praefix_SI = ("Kilo","Mega","Gige","Tera","Peta","Exa","Zetta","Yotta") #Tupel list
for i,praefix_dec in enumerate (praefix_SI,1):
    praefix_bin= praefix_dec [:2] +"bi"
    dec_pow_str = f"10 ^ {i*3:2}" # ^ is just Text
    bin_pow_str= f"2 ^ {i * 10}"
    dec_pow = 10**(i*3) # rechnen
    bin_pow = 2**(i*10)
    diff_bin_dec = (bin_pow - dec_pow)/dec_pow * 100
    print(f"{praefix_dec:7}{dec_pow_str}{dec_pow:35_d} | "
          f"{praefix_bin:7}{bin_pow_str}{bin_pow:35_d} | "
          f"{diff_bin_dec:5.2f}%")
