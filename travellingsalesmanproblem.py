import numpy as np
import operator
import time

s_time=time.time()
arr=np.array([[np.inf,7,6,8,4],
              [7,np.inf,8,5,6],
              [6,8,np.inf,9,7],
              [8,5,9,np.inf,8],
              [4,6,7,8,np.inf]])
m_arr=arr

h_dic={0:'a', 1:'b', 2:'c', 3:'d', 4:'e'}
v_dic={0:'a', 1:'b', 2:'c', 3:'d', 4:'e'}
path=[]


def penalty(p_arr):
    d={}
    ind=np.where(p_arr==0)
    for i,j in zip(ind[0],ind[1]):
        d[i,j]= np.partition(p_arr[i],len(p_arr[i])-2)[1] + np.partition(p_arr[:,j],len(p_arr[:,j])-2)[1]

    #print(max(d.items(), key=operator.itemgetter(1))[0])
    return max(d,key=d.get)
    

def red_arr(T_arr,ind):
    T_arr=np.delete(T_arr,ind[0],0)
    T_arr=np.delete(T_arr,ind[1],1)
    return T_arr
    

def check_for_zero(m_arr):
    k=0
    for i in m_arr:
        if (np.all(i)):
            mini=i.min()
            m_arr[k]=[x-mini for x in i]
            k+=1
            continue
        k+=1
    return m_arr


def chng_dic(ind):
    global h_dic,v_dic

    h_key,h_val= zip(*h_dic.items())
    h_val=list(h_val)
    h_key=list(h_key)
    h_val.remove(h_dic[ind[0]])
    h_dic=dict(zip(h_key,h_val))
        
    v_key,v_val= zip(*v_dic.items())
    v_val=list(v_val)
    v_key=list(v_key)
    v_val.remove(v_dic[ind[1]])
    v_dic=dict(zip(v_key,v_val))
    


while True:
    f_r_check=check_for_zero(m_arr)
    f_c_check=check_for_zero(f_r_check.T)
    T_arr=f_c_check.T

    ind=penalty(f_c_check.T)
    path.append((h_dic[ind[0]],v_dic[ind[1]]))
    
    if (h_dic[ind[0]] in v_dic.values()) and (v_dic[ind[1]] in h_dic.values()):
        f_c_check.T[ind[1],ind[0]]=np.inf

    reduce_arr=red_arr(T_arr,ind)
    m_arr=reduce_arr

    chng_dic(ind)
    if len(v_dic)==1 and len(h_dic)==1:
        path.append((h_dic[0],v_dic[0]))
        break

x=''    
print(path)
path_dict=dict(path)
i=0
keey=input('where to start')
x+=keey
while i<4:
    for key,val in path_dict.items():
        if keey==key:
            x+=val
            keey=val
            i+=1
            break
print(x)

e_time=time.time()
print(e_time-s_time)
