
tempo = 0
gol_1 = 0
gol_2 = 0

nome_time_1 = input("Digite o nome do Primeiro Time: ")
ataque_time_1 = int(input("De 0 a 30, insira Força de Ataque do primeiro time: "))
defesa_time_1 = int(input("De 0 a 30, insira a Consistência de Defesa do primeiro time: "))
folego_time_1 = int(input("De 0 a 5, insira o Fôlego do primeiro time: "))

nome_time_2 = input("Digite o nome do Segundo Time: ")
ataque_time_2 = int(input("De 0 a 30, insira Força de Ataque do segundo time: "))
defesa_time_2 = int(input("De 0 a 30, insira a Consistência de Defesa do segundo time: "))
folego_time_2 = int(input("De 0 a 5, insira o Fôlego do segundo time: "))

sorte_1 = int(input("Digite 1 ou 2 para definir a sorte dos times: "))
sorte_2 = int(input("Digite 1 ou 2 para definir a sorte dos times: "))
sorte_3 = int(input("Digite 1 ou 2 para definir a sorte dos times: "))
sorte_4 = int(input("Digite 1 ou 2 para definir a sorte dos times: "))

# ====================================================================
print("Início de jogo!")

# Primeiro tempo

tempo += 1
print(f"{tempo}° tempo:")
print(f"{nome_time_1} [{gol_1}-{gol_2}] {nome_time_2}")

# ====================================================================
# Priemira Rodada (TIME 1 vai ATACAR)

print(f"O time {nome_time_1} vem pressionando.")

if sorte_1 == 1:
    ataque_time_1 += 2

elif sorte_1 == 2:
    defesa_time_2 += 2

if ataque_time_1 >= defesa_time_2:
    gol_1 += 1
    print(f"GOOOOOOOOOOOOLLLLLL DO TIME {nome_time_1}!!!")
else:
    print(f"O ataque é interrompido! Ótima defesa do time {nome_time_2}")

if sorte_1 == 1:
    ataque_time_1 -= 2

elif sorte_1 == 2:
    defesa_time_2 -= 2

# ====================================================================
# Segunda Rodada (TIME 2 vai ATACAR)

fator_canseira_time_1 = 1 - ( (5 - folego_time_1)/10)
fator_canseira_time_2 = 1 - ( (5 - folego_time_2)/10)


ataque_time_1 *= fator_canseira_time_1
defesa_time_1 *= fator_canseira_time_1

ataque_time_2 *= fator_canseira_time_2
defesa_time_2 *= fator_canseira_time_2

print(f"O time {nome_time_2} vem pressionando.")

if sorte_2 == 1:
    ataque_time_2 += 2

elif sorte_2 == 2:
    defesa_time_1 += 2


if ataque_time_2 >= defesa_time_1:
    gol_2 += 1
    print(f"GOOOOOOOOOOOOLLLLLL DO TIME {nome_time_2}!!!")
else:
    print(f"O ataque é interrompido! Ótima defesa do time {nome_time_1}")

if sorte_2 == 1:
    ataque_time_2 -= 2

elif sorte_2 == 2:
    defesa_time_1 -= 2



# ====================================================================
# Segundo tempo

tempo += 1
print(f"{tempo}° tempo:")
print(f"{nome_time_1} [{gol_1}-{gol_2}] {nome_time_2}")

# Terceira Rodada (TIME 2 vai ATACAR)

ataque_time_1 *= fator_canseira_time_1
defesa_time_1 *= fator_canseira_time_1

ataque_time_2 *= fator_canseira_time_2
defesa_time_2 *= fator_canseira_time_2

print(f"O time {nome_time_2} vem pressionando.")

if sorte_3 == 1:
    ataque_time_2 += 2

elif sorte_3 == 2:
    defesa_time_1 += 2

if ataque_time_2 >= defesa_time_1:
    gol_2 += 1
    print(f"GOOOOOOOOOOOOLLLLLL DO TIME {nome_time_2}!!!")
else:
    print(f"O ataque é interrompido! Ótima defesa do time {nome_time_1}")

if sorte_3 == 1:
    ataque_time_2 -= 2

elif sorte_3 == 2:
    defesa_time_1 -= 2


# ====================================================================
# Quarta Rodada (TIME 1 vai ATACAR)

print(f"O time {nome_time_1} vem pressionando.")

ataque_time_1 *= fator_canseira_time_1
defesa_time_1 *= fator_canseira_time_1

ataque_time_2 *= fator_canseira_time_2
defesa_time_2 *= fator_canseira_time_2

if sorte_4 == 1:
    ataque_time_1 += 2

elif sorte_4 == 2:
    defesa_time_2 += 2

if ataque_time_1 >= defesa_time_2:
    gol_1 += 1
    print(f"GOOOOOOOOOOOOLLLLLL DO TIME {nome_time_1}!!!")
else:
    print(f"O ataque é interrompido! Ótima defesa do time {nome_time_2}")

if sorte_4 == 1:
    ataque_time_1 -= 2

elif sorte_4 == 2:
    defesa_time_2 -= 2

# ====================================================================
# Fim de Jogo

print(f"{nome_time_1} [{gol_1}-{gol_2}] {nome_time_2}")


# ====================================================================
# Jogo Empatado

if gol_1 == gol_2:
    print("Temos um empate! Será decidido em breve nos pênaltis. Fique ligado!")

elif gol_1 > gol_2:
    print(f"ACABOOOOU!! O TIME {nome_time_1} É O CAMPEÃO!!!")

else:
    print(f"Fim de jogo! O time {nome_time_2} é campeão.")