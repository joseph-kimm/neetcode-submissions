class Twitter:

    def __init__(self):

        self.time = 0
        self.followMap = dict()
        self.tweet = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.tweet.keys():
            self.tweet[userId] = []

        self.tweet[userId].append((self.time, tweetId))
        self.time += 1

        return

    def getNewsFeed(self, userId: int) -> List[int]:

        heap = []

        if userId in self.tweet.keys():

            pos = len(self.tweet[userId]) - 1
            time, tweet = self.tweet[userId][pos]
            
            heapq.heappush(heap, (-time, tweet, userId, pos - 1))

        if userId in self.followMap.keys():
            for followee in self.followMap[userId]:

                if followee in self.tweet.keys():

                    pos = len(self.tweet[followee]) - 1
                    time, tweet = self.tweet[followee][pos]

                    heapq.heappush(heap, (-time, tweet, followee, pos -1))

        res = []

        while heap and len(res) < 10:

            time, tweet, followee, pos = heapq.heappop(heap)
            res.append(tweet)

            if pos >= 0:
                time, tweet = self.tweet[followee][pos]
                heapq.heappush(heap, (-time, tweet, followee, pos - 1))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId == followeeId:
            return 

        if followerId not in self.followMap.keys():
            self.followMap[followerId] = set()

        self.followMap[followerId].add(followeeId)

        return
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.followMap.keys() and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        return
        
