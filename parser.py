import pandas as pd
import random


def make(filename):
	xls = pd.ExcelFile(filename + '.xlsx', on_demand = True)
	df = xls.parse(xls.sheet_names[0])

	df[0] = df.pop('Unnamed: 1')
	df[1] = df.pop('Unnamed: 2')

	questions = []
	answers = []

	for i in range(len(df[0])):
		_i = random.choice([0, 1])
		questions.append(df[_i][i])
		answers.append(df[_i ^ 1][i])

	return answers[1:], questions[1:]

def save2exel(answers, questions):
	write = pd.ExcelWriter('test.xlsx')

	df_q = pd.DataFrame({'질문':questions})
	df_a = pd.DataFrame({'정답':answers})

	df_q.to_excel(write, sheet_name='questions')
	df_a.to_excel(write, sheet_name='answers')

	write.save()

if __name__ == '__main__':
	questions, answers = make('wordlist')
	save2exel(questions, answers)
