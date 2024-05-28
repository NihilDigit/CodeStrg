def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def play_momo(n):
    if n == 0:
        print('shamiko wins!')
    else:
        play_shamiko(n-1)

def play_shamiko(n):
    if n == 0:
        print('momo wins!')
    elif is_even(n):
        play_momo(n-2)
    else:
        play_momo(n-1)

play_momo(1)