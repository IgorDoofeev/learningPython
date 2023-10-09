def recursive(value):
    print(value)
    if value < 4: # Усовие остановки
        recursive(value+1)
    print(value)


recursive(1)