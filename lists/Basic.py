
Day 2 Python Core Engineering Assessment
kpensalenaondongu8@gmail.com Switch account
 
Question 2 Find the missing passes
Easy to moderate  |  9 minutes  |  15 marks
Return every score greater than or equal to 50, in the original order. Inputs are lists of integers from 0 to 100. An empty list must return an empty list.
def passing_scores(scores):
    passed = []
    for index in range(len(scores) - 1):
        if scores[index] > 50:
            passed.append(scores[index])
    return passed
print(passing_scores([49, 50, 80, 65]))
Q2 Part B
Correct the function without changing the input list. [6 marks]
def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return passed
print(passing_scores([49, 50, 80, 65]))
Q2 Part A
Predict the current printed output. Identify both independent defects and explain which result each defect loses. [5 marks]
it will print 80
it losed 50 65
it losed 50 because the conditional statement says if the scores is > 50 not >= 50 so 50 is = 50 not greater.
it losed 65  thou 65 is > 50 but the loop stopped at the second to the last number in the list and 65 is the last number. 
Q2 Part C
Write three executable assertions: one for the pass boundary 50, one for a single passing score, and one for an empty list. [4 marks]
assert = if score == 0:
        return "score cant be empty"

assert = if score >= 50:
       return "pass boundary"
assert = if score < 50:
       return "single passing score

Page 3 of 6
Never submit passwords through Google Forms.
This content is neither created nor endorsed by Google. - Contact form owner - Terms of Service - Privacy Policy
Does this form look suspicious? Report

Google Forms