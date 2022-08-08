class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        run_task_stask = []
        for log in logs:
            idx, action_type, timestamp = log.split(":")
            idx = int(idx)
            timestamp = int(timestamp)
            if action_type =="start":
                # 队列里面有数据，前面有运行的程序
                # 这个时候需要把这个程序终止掉，同时计算它已经运行时间的时间
                if run_task_stask:
                    # 前一个任务
                    task_info = run_task_stask[-1]
                    task_id = task_info[0]
                    task_timestamp = task_info[1]
                    # 前一个任务的时间 = 当前 - 任务存储的时间
                    ans[task_id] = ans[task_id] + (timestamp - task_timestamp)
                    # 更新这个任务的最后运行时间
                    task_info[1] = timestamp
                # 把正在运行的程序压到栈里面
                run_task_stask.append([idx,timestamp])
            else:
                # 当前日志说明程序结束了，直接从栈里面拿程序的开始时间
                last_task_info = run_task_stask.pop()
                task_id = last_task_info[0]
                task_timestamp = last_task_info[1]
                # 结束时间 - 最后运行时间 + 1
                ans[task_id] = ans[task_id] + (timestamp - task_timestamp) + 1
                # 如果栈没有空，更新运行时间 
                if run_task_stask:
                    run_task_stask[-1][1] = timestamp +1
        return ans


n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
result = Solution().exclusiveTime(n, logs)
print(result)
