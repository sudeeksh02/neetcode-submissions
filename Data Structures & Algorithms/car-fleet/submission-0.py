class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[0]
        fleet=len(position)
        store={}
        n=len(position)
        for i in range(n):
            store[position[i]]=(target-position[i])/speed[i]
        s_store=dict(sorted(store.items(),reverse=True))

        for car in s_store:
            if s_store[car] > stack[-1]:
                stack.append(s_store[car])
            else:
                fleet-=1
        return fleet