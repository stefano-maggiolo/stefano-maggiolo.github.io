---
title: Quanti sono i laureati, tra eletti ed elettori
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2013/02/quanti-sono-i-laureati-tra-eletti-ed-elettori/
categories:
  - Politics
  - Statistics
---
In uno dei [suoi post post-elettorali][1], Beppe Grillo presenta alcuni numeri per indicare il miglioramento del livello dei parlamentari tra la scorsa legislatura e la presente. Tra questi numeri, la percentuale di donne, l'età media e la percentuale di laureati. Il problema è che queste distribuzioni (sesso, età, educazione) sono correlate nella popolazione italiana; in particolare, non è un mistero che ci siano più laureati tra i giovani che non tra gli anziani. Quindi sorge la domanda: il primato del Movimento 5 Stelle per percentuale di laureati è un effettivo merito o è possibile giustificarlo semplicemente grazie alla distribuzione delle età dei loro eletti?

 [1]: http://www.beppegrillo.it/2013/02/i_numeri_della_speranza.html

<!--more-->

Un paio di **disclaimer** prima di cominciare: non ho alcun interesse a supportare una causa o l'altra, questo è solo un esercizio; inoltre, in molti punti ho dovuto accontentarmi di dati incompleti, e in altri molteplici approcci erano possibili; nonostante questo, ne ho portato avanti solo uno senza confrontarlo con altri, come dovrebbe fare uno studio serio.

Partiamo con un po' di **dati**. Il più autorevole è la percentuale di laureati per fascia di età, che viene direttamente dagli [studi OCSE del 2012][2] (pag. 13). Questa la distribuzione in Italia.

 [2]: http://www.keepeek.com/Digital-Asset-Management/oecd/education/education-at-a-glance-2012/indicator-a1-to-what-level-have-adults-studied_eag-2012-5-en

| < 25 | < 35 | < 45 | < 55 | < 65 | < &infin; |
| ---- | ---- | ---- | ---- | ---- | --------- |
| ?    | 21%  | 16%  | 12%  | 11%  | ?         |

Poiché l'età minima tra i neo-eletti è proprio 25 anni, nel seguito **assumeremo** che la prima percentuale (per i minori di 25 anni) sia ancora il 21%, e con un po' di generosità, in assenza di dati assumeremo che 11% degli ultra-sessantacinquenni siano laureati.

Ora dobbiamo sapere qualcosa dei **neo-eletti**. Dal [Secolo XIX][3] abbiamo la percentuale di parlamentari laureati per partito. Il numero dei parlamentari eletti per partito viene da [Wikipedia][4]. Infine, l'età media dallo studio di [Coldiretti][5]. In questa analisi ci limitiamo ai partiti con un numero di eletti statisticamente rilevante.

 [3]: https://www.facebook.com/photo.php?fbid=10151293001407215&#038;set=pb.36493277214.-2207520000.1362042679&#038;type=3&#038;theater
 [4]: http://it.wikipedia.org/wiki/Elezioni_politiche_italiane_del_2013
 [5]: http://www2.coldiretti.it/News/Pagine/141---26-Febbraio-2013.aspx

| Partito |        | Eletti |        |        | Età media |        | Laureati     |
|         | Camera | Senato | Totale | Camera | Senato    | Totale |              |
| ------- | ------ | ------ | ------ | ------ | --------- | ------ | ------ | --- |
| M5S     | 109    |  54    | 163    | 33     | 46        | 37     | 88.00% | 143 |
| PD      | 297    | 113    | 410    | 47     | 54        | 49     | 67.00% | 275 |
| SEL     |  37    |   7    |  44    | 46     | 50        | 47     | 80.00% |  35 |
| PdL     |  98    |  98    | 196    | 50     | 57        | 54     | 76.00% | 149 |
| LN      |  18    |  18    |  36    | 42     | 48        | 45     | 40.00% |  14 |
| M       |  39    |  19    |  58    | 55     | 56        | 55     | 81.00% |  47 |

Purtroppo non sono riuscito a trovare una lista di età dei parlamentari eletti, ma solo l'età media. Assumendo che la distribuzione di età sia normale, rimane da trovare la deviazione standard. Ci vengono in aiuto **due dati**: il primo è che il deputato più giovane ha 25 anni ed è del M5S mentre quello più vecchio è del PD e ha 89 anni (ancora dal blog di Grillo); il secondo sono le [distribuzioni][6] [per età][7] della legislatura precedente, che possono dare un'idea di come cambi la deviazione standard al variare dell'età media.

 [6]: http://www.senato.it/leg/16/BGT/Schede_v3/Statistiche/Composizione/SenatoriPerEta.html
 [7]: http://www.camera.it/564?tiposezione=C&#038;sezione=1&#038;tabella=C_1_7

Facendo una **regressione** per ricavare la deviazione standard dai dati della legislatura precedente, si ottengono i dati seguenti (per diversi campioni rappresentativi al variare del partito e della camera di appartenenza).

| Età media | Deviazione standard |
| --------- | ------------------- |
| 60.0      | 8.0                 |
| 59.0      | 8.0                 |
| 54.0      | 9.0                 |
| 53.5      | 8.5                 |
| 49.0      | 10.0                |

Come prevedibile, la deviazione standard **diminuisce** all'aumentare dell'età media. Purtroppo nelle legislazioni precedenti non c'erano campioni rappresentativi con età medie confrontabili con le attuali, per cui assumeremo che la deviazione standard **ritorni a diminuire** sotto i 45 anni di età media, e cercheremo di fare in modo che concordi con l'avere un eletto di 25 anni.

Il passo successivo è quindi quello di **stimare** per ogni partito una deviazione standard adatta, grazie alle osservazioni fatte in precedenza. Otteniamo queste tabelle che contengono per ogni partito e ogni fascia di età una stima del **numero di parlamentari** nella legislatura corrente. La tabella seguente è per la Camera (contiene anche la stima della deviazione standard).

| Partito | < 25 | < 35  | < 45  | < 55   | < 65  | < &infin; | Std  |
| ------- | ---- | ----- | ----- | ------ | ----- | --------- | ---- |
| M5S     | 1.21 | 76.85 | 30.91 |   0.03 |  0.00 | 0.00      |  3.5 |
| PD      | 0.88 | 18.96 | 99.34 | 130.70 | 43.49 | 3.63      |  8.0 |
| SEL     | 0.16 |  2.97 | 13.53 |  15.52 |  4.50 | 0.32      |  8.0 |
| PdL     | 0.61 |  5.94 | 23.69 |  37.53 | 23.69 | 6.55      | 10.0 |
| LN      | 0.14 |  2.72 |  9.13 |   5.44 |  0.56 | 0.01      |  7.0 |
| M       | 0.02 |  0.50 |  4.68 |  14.30 | 14.30 | 5.20      |  9.0 |

Per il Senato a seguire. Tutte le colonne si intendono "esclusi quelli indicati nelle colonne precedenti".

| Partito | < 25 | < 35 | < 45  | < 55  | < 65  | < &infin; | Std  |
| ------- | ---- | ---- | ----- | ----- | ----- | --------- | ---- |
| M5S     | 0.23 | 4.33 | 19.75 | 22.65 |  6.56 |  0.47     |  8.0 |
| PD      | 0.07 | 1.89 | 15.96 | 43.57 | 38.98 | 12.52     |  9.0 |
| SEL     | 0.04 | 0.42 |  1.69 |  2.68 |  1.69 |  0.47     | 10.0 |
| PdL     | 0.01 | 0.46 |  7.27 | 32.14 | 41.13 | 16.98     |  8.5 |
| LN      | 0.10 | 1.24 |  5.31 |  7.42 |  3.40 |  0.53     |  9.0 |
| M       | 0.01 | 0.18 |  1.92 |  6.55 |  7.33 |  3.01     |  9.0 |

Questo è un ottimo punto in cui fermarsi e dichiarare: questi dati **potrebbero essere completamente sbagliati**, ma non dovrebbe essere molto difficile ottenere quelli reali, una volta che i nuovi parlamentari avranno la loro scheda ufficiale sul sito di Camera e Senato.

Proviamo a continuare. Se moltiplichiamo queste stime di parlamentari per fascia di età con le percentuali di laureati per quella fascia, otteniamo una **percentuale attesa di laureati per partito**. In altre parole, se ogni partito avesse scelto i suoi parlamentari a caso, avendo solo fissato quanti debbano essere per ogni fascia di età, questa sarebbe la percentuale di laureati che ci aspettiamo. Nella tabella ricordo anche la percentuale reale di laureati.

| Partito | Attesa | Reale |
| ------- | ------ | ----- |
| M5S     | 17.76% | 88%   |
| PD      | 13.36% | 67%   |
| SEL     | 13.96% | 80%   |
| PdL     | 12.50% | 76%   |
| LN      | 14.53% | 40%   |
| M       | 12.05% | 81%   |

Come previsto, il Movimento 5 Stelle a causa della sua minore età media ha una percentuale attesa di laureati molto più alta di tutti gli altri partiti. Ma ancora non siamo arrivati in fondo: è sufficiente per **giustificare** il maggior numero di laureati?

Una possibile **misura** è la seguente: la mia **sorpresa** (positiva) nel sapere che il partito X, con una percentuale attesa di laureati pari a P, abbia nella realtà una percentuale di laureati maggiore o uguale a Q. Voglio infatti sapere se mi sorprende di più il Movimento 5 Stelle col suo 88% di laureati, o, per esempio, la lista di Monti con il suo 81%.

Facciamo l'esempio di **come calcolare** questa misura per il M5S. Abbiamo un'urna con 100 palline, (circa) 18 bianche, e il resto nere. Estraiamo 163 palline (tante quante il numero di eletti), una alla volta, annotando il loro colore e reinserendole ogni volta nell'urna. Qual è la probabilità che abbia estratto almeno 143 palline bianche (tante quante il numero di laureati eletti)? Per fare ciò, possiamo usare l'approssimazione con una distribuzione normale della distribuzione binomiale (possibile perché abbiamo come minimo 36 estrazioni).

E qui ci scontriamo con la triste realtà per i detrattori della politica (che era possibile prevedere molto tempo fa): questo calcolo è **perfettamente inutile**. Per ogni forza politica la "sorpresa", cioè la misura di quanto è sorprendente avere almeno quel numero di laureati, è altissima, tanto da essere approssimata al massimo valore, 100%, o **sopresa totale**, per tutte i partiti tranne che per la Lega Nord, per cui la sorpresa non è del 100% ma comunque un sorprendente (al second'ordine) 99,998%. 

Per non sprecare questo tempo, cerchiamo di arrivare comunque a una **stima migliore**. Per fare ciò, assumiamo che il confronto non sia con una scelta a caso tra tutta la popolazione italiana, ma tra un n-esimo della popolazione che comprende tutti i laureati. Per esempio, se n = 2, il confronto è con una scelta a caso tra una popolazione che ha il doppio delle lauree (in media) della vera popolazione italiana. Ovviamente dobbiamo stare attenti che le percentuali di laureati non possono superare il 100%!

Purtroppo, n = 2 **non è sufficiente**. Ancora la sorpresa è troppo grande per essere confrontata. Anche con un terzo e con un quarto non tutti i partiti ottengono un valore minore di 1 per la misura di sorpresa. Per n = 5 finalmente otteniamo questi valori:

| M5S |  70.524% |
| PD  |  58.893% |
| SEL |  92.800% |
| PdL |  99.996% |
| LN  |   0.000% |
| M   |  99.941% |

Ancora una delusione! Nel nuovo parlamento, il partito che sorprende di più è il Pdl, seguito a poca distanza dalla lista Monti e poi da Sinistra e Libertà. Il Movimento 5 Stelle si piazza a mezza classifica, seguito dal Partito Democratico e, ma non avevamo dubbi, dalla Lega Nord.

**Qual è la vostra sorpresa per questi dati?**
