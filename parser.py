import argparse
import random

import pandas as pd

def get_parser():
	parser = argparse.ArgumentParser(usage='[path] [-s] [-i]')
	parser.add_argument('path', help='path of excel')
	parser.add_argument('-s', '--saveas', help='save as(default: exam.xlsx)', default='exam')
	parser.add_argument('-i', '--index', help='start exel pos', type=int)
	return parser

def command_line_runner():
	parser = get_parser()
	args = vars(parser.parse_args())

	if not args['path']:
		print(parser.print_help())
		return
	
	if args['index']:
		_dict = exel2dict(args['path'], args['index'])
	else:
		_dict = exel2dict(args['path'])
	
	q, a = mix_dict(_dict)
	save2exel(q, a, args['saveas'])

def exel2dict(file_name, _range=1):
	xls = pd.ExcelFile(file_name + '.xlsx')
	df = xls.parse(xls.sheet_names[0])

	_dict = {}

	# Todo: pandas indexing to 0, 1
	df[0] = df.pop('Unnamed: 1')
	df[1] = df.pop('Unnamed: 2')

	for i in range(_range, len(df[0])):
		_i = random.choice([0, 1])
		_dict[df[_i][i]] = df[_i ^ 1][i]
	return _dict


def mix_dict(_dict):
	q_rand = random.sample([key for key in _dict.keys()], len(_dict))
	a_rand = [_dict[i] for i in q_rand]
	return q_rand, a_rand

def save2exel(q_rand, a_rand, name):
	writer = pd.ExcelWriter(name + '.xlsx')

	df_q = pd.DataFrame({'질문':q_rand})
	df_a = pd.DataFrame({'정답':a_rand})

	df_q.to_excel(writer, sheet_name='질문')
	df_a.to_excel(writer, sheet_name='정답')

	writer.save()

if __name__ == '__main__':
	command_line_runner()
