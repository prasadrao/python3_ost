import datetime
import time
import random

class Q(object):

    def __init__(self,a=None,b=None):
        if not a and not b:
            self.a = random.randrange(1,10)
            self.b = random.randrange(1,10)
        else:
            self.a = a
            self.b = b
        self.answer = self.a + self.b

    def get_answer(self):
        self.start = time.time()
        self.ans = input("What is the sum of {0} and {1} ?\n".format(self.a,self.b))
        self.end = time.time()

    def confirm(self):
        return int(self.ans) == self.answer

    def time_taken(self):
        return datetime.timedelta(seconds=(self.end - self.start)).seconds

if __name__ == '__main__':
    count = 0
    out = []
    tot_time = 0
    while count < 5:
        ques = Q()
        ques.get_answer()
        print(ques.confirm())
        if ques.confirm():
            print("{} is correct answer!".format(ques.ans))
            out.append((count+1, ques.time_taken(), "right"))
        else:
            print("{} is wrong answer!".format(ques.ans))
            out.append((count+1, ques.time_taken(), "wrong"))
        count += 1
    for i in out:
        print("Question #{0} took about {1} seconds to complete and was {2}".format(i[0],i[1],i[2]))
        tot_time += i[1]
    print("You took {} seconds to finish the quiz.".format(tot_time))
    print("Your average time was {} seconds per question.".format(tot_time/5))
