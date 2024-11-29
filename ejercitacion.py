from data.frutas import frutas
from tabulate import tabulate

print(tabulate(frutas, headers="keys", tablefmt="github"))

