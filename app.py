import json
import numpy as np
import pandas as pd

def fibonacci(n):
    a=0
    b=1
    c=0
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    return c

@app.route('/fibonacci',methods=['GET','POST'])
def collectData():
    n=int(request.args.get('n'))
    
    result=fibonacci(n)
    return(json.dumps(result))

if(__name__=="__main__"):
    app.run()
