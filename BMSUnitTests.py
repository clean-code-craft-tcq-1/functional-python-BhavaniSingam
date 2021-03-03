if __name__ == '__main__':
            assert(isBatteryOk(25, 70, 0.7) == True)
            assert(isBatteryOk(45, 80, 0.8) == True)
            assert(isBatteryOk(50 , 90, 0.9) == False)
            assert(isBatteryOk(25 , 15, 0.9) == False)
            assert(isBatteryOk(25 , 65, 0.9) == False)
            assert(isBatteryOk(15, 85, 0.7) == False)