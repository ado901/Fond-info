a = int(input("inserire n < 10: "))
while a >= 10: #semplice controllo, finchè l'utente non mi dà un numero minore di 10 continuo a chiederlo
    print("numero > 10")
    a = int(input("inserire n < 10: "))
for i in range(1, a + 1): #in che riga ci troviamo?
    contatore = ''
    for k in range(1, i + 1): #quante cifre devo scrivere per ogni riga?
        contatore += str(k) #uso una sorta di contatore di stringhe, ricordo che "pinco" + "pallino" = "pincopallino"
    print(contatore)
'''
l'esercizio vuole che usi due for uno dentro l'altro, il primo for rappresenta le righe ad ogni iterazione,
di conseguenza va da 1 al numero che passa l'utente, ovvero il numero di righe
Il secondo for invece rappresenta la cifra che devo scrivere ad ogni iterazione
essendo che per ogni riga devo scrivere un numero di cifre pari al numero della riga
il for andrà da 1 alla riga in cui ci troviamo (ovvero a che punto siamo nel primo for)
'''
