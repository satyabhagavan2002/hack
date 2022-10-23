class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        tcount = Counter(target)
        def getScore(s):
            temp = dict(tcount)
            sdict = defaultdict(int)
            res = 0
            for c in s:
                if c in temp and temp[c] > 0:
                    temp[c] -= 1
                    res += 1
                    sdict[c] += 1
            return (res, sdict)
        stickers = [getScore(s) for s in stickers]
        stickers.sort(key = lambda x: x[0], reverse = True)
        stickers = [x[1] for x in stickers if x[0] > 0]
        opt = [stickers[0]]
        for i in range(1, len(stickers)):
            if opt[-1].keys() == stickers[i].keys() :
                continue
            opt.append(stickers[i])
        stickers = opt[:]
            
        seen = set()
        q = deque([target])
        step = 0
        while q:
            n = len(q)
            step += 1
            for i in range(n):
                cur = q.popleft()
                if cur in seen:
                    continue
                seen.add(cur)
                for stick in stickers:
                    if cur[0] not in stick:
                        continue
                    new = str(cur)
                    for s in stick:
                        new = new.replace(s,'', stick[s])
                    if new == "":
                        return step
                    if new not in seen:
                        q.append(new)
        return -1
