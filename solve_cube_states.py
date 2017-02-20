import subprocess
import json
import threading
import re
import math

# This scramble takes a few seconds to solve. Use for testing.
# RB BU DL LF BD RF RU LU DR UF LB DF RBU DFL LUB BRD DLB UFR FDR ULF

# This scramble takes almost exactly 3 minutes to solve. Use for testing.
# BL RB LD FU FL RF BD DF UR RD UL UB BUR FRU FLD RFD ULF BRD DLB UBL

regex = ur"(\b[FBRLUD]['2 ]? )+"

class SolutionThread(threading.Thread):
    def __init__(self, name='Thread', start=0, num=2):
        threading.Thread.__init__(self)
        self.states = cube_states[start:start+num]
        self.start_idx = start
        self.num = num
        self.counter = 0
        self.name = name

    def run(self):
        #print self.name + ': ' + str(self.states)
        cube_queries = '\n'.join(self.states) + '\n'
        p = subprocess.Popen(['./optiqtm'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out = p.communicate(input=cube_queries.encode('utf-8'))[0]
        self.parse_out(out)

    def parse_out(self, output):
        threadLock.acquire(1)
        with open('output/optiqtm_response_2_1000.txt', 'a') as f:
            f.write(output)
            f.write('\n\n\n')
        threadLock.release()
        for s in output.split('\n'):
            matches = re.search(regex, s)
            if matches:
                if self.counter >= len(self.states):
                    print "index error"
                else:
                    current_scramble = self.states[self.counter]
                    scrambles[current_scramble]['solution'] = matches.group()
                    self.counter += 1
                    threadLock.acquire(1)
                    with open('output/solutions_2_1000.csv', 'a') as f:
                        f.write(current_scramble + ',' + matches.group())
                        f.write('\n')
                    threadLock.release()


threadLock = threading.Lock()
threads = []
scrambles = {}

with open('output/scrambles.json', 'r') as f:
    scrambles = json.load(f)

cube_states = scrambles.keys()

num_threads = 5.
start = 0
for i in range(int(num_threads)):
    states_each = int(math.ceil(len(cube_states)/num_threads))
    t = SolutionThread('Thread ' + str(start), start, states_each)
    start += states_each
    t.start()
    threads.append(t)

# Wait for all threads to complete
for t in threads:
    t.join()

with open('output/solutions_2_1000.json', 'w') as f:
    json.dump(scrambles, f)

print "Exiting Main Thread"
