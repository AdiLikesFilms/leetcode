class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        places = len(flowerbed)
        index_i = places - 1 
        totalplants = 0

        for i in range(places):

            if flowerbed[i] == 0:
                print("Check 1: It is a zero")

                if i == 0:
                    print('Left side is empty check right side then')

                    nextpos = i + 1

                    if nextpos >= places or flowerbed[nextpos] == 0:
                        print('It can be planted here')

                        flowerbed[i] = 1
                        totalplants = totalplants + 1

                elif i == index_i:
                    print('last part just check left side')

                    leftpos_e = i - 1 

                    if flowerbed[leftpos_e] == 0:
                        print("can be planted at this")

                        flowerbed[i] = 1
                        totalplants = totalplants + 1

                else:
                    leftpos = i - 1 

                    if flowerbed[leftpos] == 0:
                        print("left side is 0")

                        rightpos = i + 1 

                        if flowerbed[rightpos] == 0:
                            print("right side also 0 it can be planted here")

                            flowerbed[i] = 1
                            totalplants = totalplants + 1

        if totalplants >= n:
            return True
        else:
            return False