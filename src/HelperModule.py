import heapq

# this class purely processes input line
class InputProcessor:
    def __init__(self):
        self.zip_map = {}
        self.date_map = {}

        # initialize rez for place holder
        self.rez = []
        self.valid = True
        self.valid_zip = True
        self.valid_date = True

        # attribute index
        self.CMTE_ID = 0
        self.TRANSACTION_DT = 13
        self.ZIP_CODE = 10
        self.OTHER_ID = 15
        self.TRANSACTION_AMT = 14


    # process each input line
    def process_input(self, line):
        # reset values for input
        def reset_val():
            self.valid = True
            self.valid_zip = True
            self.valid_date = True

        reset_val()
        self.rez = line.split("|")
        # check other_id attribute: > 0 meaning invalid
        if len(self.rez[self.OTHER_ID]) > 0:
            self.valid = False
            return

        try:
            tran_amt = float(self.rez[self.TRANSACTION_AMT])
        except:
            # return because invalid amt
            return

        # check CMTE_ID or TRANSACTION_AMT is valid
        if len(self.rez[self.CMTE_ID]) == 0 or len(self.rez[self.TRANSACTION_AMT]) == 0\
                or tran_amt <= 0:
            self.valid = False
            return

        # 13: TRANSACTION_DT 0 or mal-formed: invalid less than 8
        # should i check for format?
        if len(self.rez[self.TRANSACTION_DT]) < 8:
            self.valid_date = False
        # 10: ZIP_CODE
        if len(self.rez[self.ZIP_CODE]) < 5:
            self.valid_zip = False

        # automatically add to date queue in this case
        # because we will not output results until we've done processing all data
        self.add_to_date_queue()

    # return desired output or null
    def get_zip_result(self):
        if not self.valid or not self.valid_zip:
            return None
        # convert to float
        try:
            amt = float(self.rez[self.TRANSACTION_AMT])
        except:
            return None

        # get attribute value
        cmte_id = self.rez[self.CMTE_ID]
        zip_code = self.rez[self.ZIP_CODE][0:5]
        cmte_zip_id = cmte_id + zip_code

        # add to zip_r
        zip_r = [cmte_id, zip_code]
        # hash zip_id
        median_queue = self.zip_map.get(cmte_zip_id)
        if median_queue is None:
            median_queue = MedianQueue()
            median_queue.insert(amt)
            # insert to zip_map
            self.zip_map[cmte_zip_id] = median_queue

            # first entry
            zip_r.append(str(round(amt)))
            zip_r.append("1")
            zip_r.append(str(round(amt)))
        else:
            # insert
            median_queue.insert(amt)
            # get median, count, total
            zip_r.append(median_queue.get_median())
            zip_r.append(median_queue.get_queue_len())
            zip_r.append(median_queue.get_total())

        # return result joint by |
        return "|".join(zip_r)

    # add to date query
    def add_to_date_queue(self):
        if not self.valid or not self.valid_date:
            return None

        # convert to float
        try:
            amt = float(self.rez[self.TRANSACTION_AMT])
        except:
            return None

        # get attribute values
        cmte_id = self.rez[self.CMTE_ID]
        date = self.rez[self.TRANSACTION_DT]
        cmte_date_id = cmte_id + date

        median_queue = self.date_map.get(cmte_date_id)
        if median_queue is None:
            median_queue = MedianQueue()
            median_queue.insert(amt)
            # insert to date
            self.date_map[cmte_date_id] = median_queue

        else:
            median_queue.insert(amt)

    # call this at the very end only once
    def get_date_result(self):
        # return self.date_map record to be processed for writing
        return self.date_map


class MedianQueue:
    def __init__(self):
        # minHeap default for right
        self.min_right_heap = []
        self.max_left_heap = []
        self.total = 0.0
        self.count = 0.0

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
            return str(median)
        elif l_size > l_size:
            return str(round(-self.max_left_heap[0]))
        else:
            return str(round(self.min_right_heap[0]))

    # return # of elements so far
    def get_queue_len(self):
        return str(round(self.count))

    # return total value of queue so far
    def get_total(self):
        return str(round(self.total))
