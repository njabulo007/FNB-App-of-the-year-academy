balance = 500

withdrawal = int(input('Enter withdrawal amount: R'))

if withdrawal <= balance:
    balance = balance - withdrawal
    print(f'Withdrawal successful! Remaining balance: R{balance}')
elif withdrawal <= 0:
    print(f'Invalid amount. You must withdraw more than R0.')
else:
    print('Declined. Insufficient funds')