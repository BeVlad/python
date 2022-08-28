from time import sleep


class TrafficLight:
    try:
        i_rate = int(input("Input the number of traffic light cycles (Attention! The number of cycles cannot be "
                           "more than 10). Total time of one cycle ~ 12 sec: "))
        if i_rate > 10:
            raise BaseException
    except BaseException:
        print("Error. Please, input the digit.")
        exit(0)

    __color = ('red', 'yellow', 'green')

    def running(self) -> object:
        i_cycle = 0

        while i_cycle < self.i_rate:
            i_cycle += 1
            i_text = "The traffic light is now on:"

            for i_color in TrafficLight.__color:
                if i_color == 'red':
                    print(i_text, i_color)
                    sleep(5)
                elif i_color == 'yellow':
                    print(i_text, i_color)
                    sleep(2)
                elif i_color == 'green':
                    print(i_text, i_color)
                    sleep(5)
                else:
                    print("Error. Please restart program.")
                    exit(0)


TrafficLight().running()
