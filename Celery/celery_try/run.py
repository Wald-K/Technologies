from tasks import long_task


if __name__ == '__main__':

    x = long_task.delay(5)

    print('end of main script')

    z = x.get()

    print(z)




