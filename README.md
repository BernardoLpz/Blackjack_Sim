# Blackjack_Sim

## 1. Regras Tradicionais
Segue as regras padrão do Blackjack:
- Objetivo: somar 21 ou o mais próximo disso sem ultrapassar.
- A = 1 ou 11, J/Q/K = 10, demais cartas com seu valor de face.
- Blackjack (A + 10) paga 1.5x.
- Dealer para em 17.

---

# 🃏 Blackjack++ - Regras Especiais

### 🃓 Inclusão de Jokers
- O baralho contará com **2 cartas Joker**.
- Cada Joker tem valor **0** e pode ser usado para alongar a mão sem aumentar a pontuação.

#### Golden Ticket 🎫
- Carta especial que **divide pela metade o valor da sua carta de maior valor na mão**.
- O resultado da divisão é **arredondado para cima**.
- Exemplo: Se sua maior carta vale 9, com o Golden Ticket ela passa a valer 5.

#### Carta da Caveira 💀
- Carta especial que **dobra o valor da sua carta de menor valor na mão**.
- Exemplo: Se sua menor carta vale 3, com a Caveira ela passa a valer 6.
- Cuidado: pode aumentar o risco de estourar!

---

### 🎯 Bônus por Número de Cartas
- Se o jogador **vencer com mais de 3 cartas**, ele receberá um **bônus de 25% por carta adicional a partir da 3ª**.
  
**Exemplo de multiplicadores:**
| Nº de Cartas | Multiplicador |
|--------------|---------------|
| 2            | 2.0×          |
| 3            | 2.0×          |
| 4            | 2.5×          |
| 5            | 3.15×         |
| 6            | 3.95×         |
| 7            | 5.0×          |

---

### ♥️🏁 Prêmio por Naipe
- Se **todas as cartas da mão forem do mesmo naipe** e a pontuação for **20**, ela será considerada um **Blackjack** (mesmo sem somar 21).

---

### ⚖️ Critério de Desempate
- Em caso de empate na pontuação entre jogador e dealer:
  - **Vence quem tiver mais cartas na mão.**
  - Se o número de cartas também for igual, é considerado empate.

---

### 🎭 Carta Oculta (Carta Virada)
- Existe uma **chance de 2.5%** de que qualquer carta comprada venha **virada para baixo**.
- A carta só será **revelada no final da rodada**, após a decisão de parar ou estourar.
