#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
world=Flask(__name__)
@world.route('/')
def function():
    return render_template('deployment.html') 
@world.route('/deployment',methods=['POST'])
def xyz():
    if(request.method=='POST'):
        num1=request.form['num1']
        num2=request.form['num2']
        total=int(num1)+int(num2)
        product=int(num1)*int(num2)
        return render_template('deployment.html',sum2=total,multiply=product)
if (__name__)=='__main__':
    world.run()

