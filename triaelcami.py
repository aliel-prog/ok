def clean_iban(raw: str):
    """
    cleans the input IBAN by removing spaces,
    """
    iban = raw.replace("-", "")\
        .replace(" ", "")\
        .strip()\
        .upper()
    if iban[0:2] == "ES" and len(iban) == 24:
        print("IBAN is valid")
        asterisk = (("*"*4)+" ")*4
        print(f"{iban[0:4]} {asterisk} {iban[-4:]}")
    else:
        print("IBAN is not valid")
    clean_iban("ES12 3456 7890 1234 5678 9012")
    clean_iban("es91 2100 - 0418 - 4502 - 0000684534 \n")