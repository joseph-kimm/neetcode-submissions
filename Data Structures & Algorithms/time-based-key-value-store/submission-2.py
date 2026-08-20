class TimeMap:

    def __init__(self):

        self.values = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.values.keys():
            self.values[key] = []

        self.values[key].append((timestamp, value))
        return
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.values.keys():
            return ""

        answers = self.values[key]

        if timestamp > answers[-1][0]:
            return answers[-1][1]

        l = 0
        r = len(answers) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if answers[m][0] == timestamp:
                return answers[m][1]
            
            elif answers[m][0] < timestamp:
                l = m + 1
            
            else:
                r = m - 1
            
        if answers[m][0] < timestamp:
            return answers[m][1]
        
        elif m > 0:
            return answers[m-1][1]
        
        else:
            return ""

            


        
