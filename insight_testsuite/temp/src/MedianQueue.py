import heapq


class MedianQueue:
    def __init__(self):
        # minHeap default for right
        self.min_right_heap = []
        self.max_left_heap = []
        self.total = 0
        self.count = 0

    def insert(self, num):
        # update count & total
        self.count += 1
        self.total += num

        l_size = len(self.max_left_heap)
        r_size = len(self.min_right_heap)

        # insert into right
        if l_size == 0 and r_size == 0:
            heapq.heappush(self.min_right_heap, num)
            return

        if self.max_left_heap:
            left_val = -self.max_left_heap[0]
        if self.min_right_heap:
            right_val = self.min_right_heap[0]

        # case 1
        if l_size == r_size:
            if num <= left_val:
                heapq.heappush(self.max_left_heap, -num)
            else:
                heapq.heappush(self.min_right_heap, num)

        # left has more element
        elif l_size > r_size:
            # case balance out => add to the right queue
            if num >= left_val:
                heapq.heappush(self.min_right_heap, num)
            else:
                # push to left queue and pop out
                l_head = -heapq.heappop(self.max_left_heap)
                heapq.heappush(self.max_left_heap, -num)
                # add to right queue
                heapq.heappush(self.min_right_heap, l_head)

        # right has more element
        else:
            # case balance out ==> add to the left queue
            if num <= right_val:
                heapq.heappush(self.max_left_heap, -num)
            else:
                # num is greater and should be in right queue
                r_head = heapq.heappop(self.min_right_heap)
                heapq.heappush(self.min_right_heap, num)
                heapq.heappush(self.max_left_heap, -r_head)

    def get_median(self):
        l_size = len(self.max_left_heap)
        r_size = len(self.min_right_heap)
        # equal len
        if l_size == r_size:
            median = self.min_right_heap[0] - self.max_left_heap[0]
            median = round(median/2.0)
            return median
        elif l_size > l_size:
            return -self.max_left_heap[0]
        else:
            return self.min_right_heap[0]

    # return # of elements so far
    def get_queue_len(self):
        return self.count

    # return total value of queue so far
    def get_total(self):
        return self.total
