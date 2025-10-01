class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles >= numExchange:
            drink = numBottles // numExchange
            res += drink
            numBottles = drink + (numBottles % numExchange)
        return res