import os
from datetime import datetime

from tpsread import TPS
import pandas as pd

data = []

if __name__ == '__main__':
    print(datetime.now())
    for topdir, dirs, files in sorted(os.walk('./')):
        for filename in files:
            if filename.lower().endswith('.tps'):
                print(os.path.join(topdir, filename))
                # try:
                tps = TPS(os.path.join(topdir, filename), encoding='cp1251', cached=True, check=True, current_tablename='UNNAMED')
                
                # tps.set_current_table('UNNAMED')
                for record in tps:
                    print(record)
                    data.append(record)
                    pass
                
    df = pd.DataFrame(data)
    
    # df.to_csv('test.csv')

    # print(datetime.now())

                    #unittest
                    #pep8
                    #Docs (+comment)
                    #readme
                    #pydoc
                    #Profiler

                    #metadata field
                    #load in memory