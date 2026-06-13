import yfinance as yf

salario = float(input("Qual o seu salário? R$"))
gastos = float(input("Qual o valor dos seus gastos? R$"))

saldo = salario - gastos

print(f"Seu saldo para as ações {saldo}")

tickers_ibov = ["ABEV3.SA", "PETR4.SA","VALE3.SA"]

dados = yf.download(tickers_ibov, period="1d")
fechamento = dados['Close']

print("\nIsto é para seja comprada apenas uma ação de cada\n")
print(100 * "=")

for ticker in tickers_ibov:
    preco = fechamento[ticker].iloc[-1]
    saldo = saldo - preco
    
    if saldo <= 0:
        print("Saldo insuficiente")
        break
    
    print(f"{ticker}")
    print(f"Preço de cada ação: R${preco:.2f}")
    print(f"Saldo restante após a compra: R${saldo:.2f}")

    