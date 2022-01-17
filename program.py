import functools
import os.path
import time
class Program:
    def __init__(self,file_name):
        self.data = 0
        self.timer = 0
        tic = time.perf_counter()
        
        with open(file_name,'r') as f:
            self.data = f.read().split()
            toc = time.perf_counter()
            self.timer = toc - tic
            self.data = list(map(int, self.data))
    def time_check(self):
        return self.timer < 100
    def find_min(self):
        return min(self.data)
    
    def find_max(self):
        return max(self.data)
    
    def add(self):
        return sum(self.data)
    
    def multiply(self):
        try:
            return functools.reduce(lambda a, b : a * b, self.data)
        except OverflowError as error:
            print(error)
        
    def file_exists(self, file_path):
        return os.path.exists(file_path)