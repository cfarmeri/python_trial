import csv
import pandas as pd

names = ['bin',
		 'swScore',
		 'milliDiv',
		 'milliDel',
		 'milliIns',
		 'genoName',
		 'genoStart',
		 'genoEnd',
		 'genoLeft',
		 'strand',
		 'repName',
		 'repClass',
		 'repFamily',
		 'repStart',
		 'repEnd',
		 'repLeft',
		 'id']

type(names)
assert type(names) == list

df = pd.read_csv("./tmp.txt", sep='\t', names=names)
type(df)
assert isinstance(df, pd.DataFrame)
assert isinstance(df['genoName'], pd.Series)


name_se = pd.Series(df['repFamily'] + ':::' + df['repClass'] + ':::' + df['repName'], name='rmaskName')
assert isinstance(name_se, pd.Series)

bed_df = pd.concat([df['genoName'],
					df['genoStart'],
					df['genoEnd'],
					name_se,
					df['swScore'],
					df['strand']],
				   join='outer',
				   axis=1,
				   )
bed_df.head()






























