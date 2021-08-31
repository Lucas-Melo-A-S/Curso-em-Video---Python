city=str(input('Digite o nome de uma cidade: ').upper().strip())
citysplt=city.split()
city1=citysplt[0]
print(f'A primeria palavra da cidade cidade escrita tem "Santos" nela ? {"SANTOS" in city1} ')