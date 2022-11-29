wake_up = int(input('Wake up hour: '))
hour_without_dream = 0
call_summ = 0

for i in range(wake_up, 23):
    print('Now is', i, 'hour')
    call = int(input('How many callories: '))
    call_summ += call
    if call_summ >= 2000:
        print('Enough')
        break
    hour_without_dream += 1

print('Callories: ', call_summ)
print('Hour without dream: ', hour_without_dream)

