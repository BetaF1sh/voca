import pandas as pd
import random


def make(filename):
	xls = pd.ExcelFile(filename + '.xlsx', on_demand = True)
	df = xls.parse(xls.sheet_names[0])

	df[0] = df.pop('Unnamed: 1')
	df[1] = df.pop('Unnamed: 2')

	del df[0][0], df[1][0]

	_dict = {}

	for i in range(1, len(df[0]) + 1):
		_i = random.choice([0, 1])
		_dict[df[_i][i]] = df[_i ^ 1][i]
	return _dict


def rand_dict(_dict):
	q_rand = random.sample([key for key in _dict.keys()], len(_dict))
	a_rand = [_dict[i] for i in q_rand]
	return q_rand, a_rand

def save2exel(_dict):
	writer = pd.ExcelWriter('test.xlsx')
	
	q_rand, a_rand = rand_dict(_dict)

	df_q = pd.DataFrame({'질문':q_rand})
	df_a = pd.DataFrame({'정답':a_rand})

	df_q.to_excel(writer, sheet_name='questions')
	df_a.to_excel(writer, sheet_name='answers')

	writer.save()

if __name__ == '__main__':
	save2exel(make('wordlist'))
