import statistics
 
wyniki = [4.5, 3.0, 5.0, 4.0, 3.5]
 
print("Liczba ocen:", len(wyniki))
print("Średnia:", statistics.mean(wyniki))
print("Maksymalna ocena:", max(wyniki))
print("Minimalna ocena:", min(wyniki))
print("Mediana:", statistics.median(wyniki))