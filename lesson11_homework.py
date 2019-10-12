
class Question:  #text
    def __init__(self, text):
        self.text = text
        self.answers = []

    def answer(self, text):
        self.answers.append(text)

    def generate_stats(self): #-> dict:
        return {name: self.answers.count(name) for name in self.answers}
    # returns dictionary with answers statistics ('yes': 2, 'no': 3, 'BMW': 3


class ChoicesQuestion(Question):
    def __init__(self, text, choices):
        super().__init__(text)
        self.choices = choices

    def answer(self, text):
        if text in self.choices:
            self.answers.append(text)

class MultipleQuestion(Question):
    def __init__(self, text, choices, **count):
        super().__init__(text)
        self.choices = choices
        self.count = count

    def answer(self, text):
        if len(text) <= self.count.get('max_choices'):
            self.answers.append(text)


class CheckboxQuestion(Question):

    def answer(self, text):
        if text.lower() in ('yes', 'no'):
            self.answers.append(text)


cq = CheckboxQuestion('Do you agree that BMW is the fastest car - yes or no:')
cq.answer('Yes')
cq.answer('No')
cq.answer('do not know')
cq.answer("Yes")
print(cq.answers)


cbq = ChoicesQuestion('What is the fastest car?', ['BMW', 'Opel', 'Tesla'])
cbq.answer('Tesla')
cbq.answer('Audi')
cbq.answer('Opel')
print(cbq.answers)


mq = MultipleQuestion('What are the fastest cars out out of these?',
                      ['BMW', 'Opel', 'Tesla'], max_choices=2)



mq.answer(['BMW', 'Opel'])
mq.answer(['Tesla', 'BMW'])
print(mq.answers)
print(cq.generate_stats())


