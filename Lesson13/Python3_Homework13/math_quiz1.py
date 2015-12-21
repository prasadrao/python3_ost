from datetime import datetime
import random
def math_quiz():
    a = random.randrange(1,10)
    b = random.randrange(1,10)
    start_time = datetime.now()
    ans = input("What is the sum of {0} and {1} ?\n".format(a,b))
    if int(ans) == a + b:
        print("{0} is right answer!".format(ans))
        return (datetime.now() - start_time).seconds, True
        #res[count+1] = [(datetime.now() - start_time).seconds, "right"]
    else:
        print("{0} is Wrong answer!".format(ans))
        #res[count+1] = [(datetime.now() - start_time).seconds, "wrong"]
        return (datetime.now() - start_time).seconds, False

if __name__ == '__main__':
    count = 0
    out = []
    tot_time = 0
    while count < 5:
        out.append(math_quiz())
        count += 1
    for i in out:
        print("Question #{0} took about {1} seconds and answer was {2}".format(out.index(i)+1,i[0],i[1]))
        tot_time += i[0]
    print("You took {} seconds to finish the quiz.".format(tot_time))
    print("Your average time was {} seconds per question.".format(tot_time/5))
