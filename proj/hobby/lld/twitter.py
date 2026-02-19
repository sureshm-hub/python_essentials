# https://leetcode.com/problems/design-twitter
import heapq
from collections import defaultdict
from typing import List

#  * Space: O(N+M)
#  * Time: O(FlogF) per getNewsFeed call
#  *       O(1) - postTweet/follow/unfollow
class Twitter:

    def __init__(self):
        # userId -> list of [orderId, tweetId]
        self.userFeed = defaultdict(list)
        # follower -> set of followees
        self.followers = defaultdict(set)
        # global counter to preserve tweet order
        self.orderId = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.orderId += 1
        self.userFeed[userId].append([self.orderId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        feedSize = 10
        newsFeed: List[int] = []

        # Get followees and include self
        followees = set(self.followers.get(userId, set()))
        followees.add(userId)

        # Python has min-heap, so we push negative orderId to simulate max-heap
        recents = []
        # initialize heap with latest tweet of each followee
        for uid in followees:
            feed = self.userFeed.get(uid, [])
            if feed:
                last = len(feed) - 1
                order_id, tweet_id = feed[last]
                # (-order_id, tweet_id, uid, index_in_feed)
                heapq.heappush(recents, (-order_id, tweet_id, uid, last))

        # k-way merge over per-user sorted feeds
        while recents and len(newsFeed) < feedSize:
            neg_order, tweet_id, uid, idx = heapq.heappop(recents)
            newsFeed.append(tweet_id)

            next_idx = idx - 1
            feed = self.userFeed.get(uid, [])
            if next_idx >= 0 and next_idx < len(feed):
                order_id, next_tweet_id = feed[next_idx]
                heapq.heappush(recents, (-order_id, next_tweet_id, uid, next_idx))

        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)