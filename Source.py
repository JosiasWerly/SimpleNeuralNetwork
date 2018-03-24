#       
# **jWly 2018**
# References    
#   misc
#       http://www.falstad.com/mathphysics.html
#       https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1        
#   numpy
#       https://www.datacamp.com/community/tutorials/python-numpy-tutorial?utm_source=adwords_ppc&utm_campaignid=1001535064&utm_adgroupid=48949243189&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t1&utm_creative=236326164852&utm_targetid=aud-299261629574:dsa-379899700955&utm_loc_interest_ms=&utm_loc_physical_ms=1001686&gclid=CjwKCAjw4sLVBRAlEiwASblR-ztV5_DNEmEUli50S-k930m86iy-E75-FncZlWIiTu844hJ_xO5bQBoCHw0QAvD_BwE






#python3.3
import numpy as np #you need to download np
from numpy import exp, array, random, dot



debug=False
def nonlin(x, base=1, deriv=False):
	if deriv==True:
	    return x*(base-x)
	return base/(base+np.exp(-x))
if __name__ == "__main__":
    print("starting")
    inputSet=array([
        [0, 0, 1],
        [0, 1, 1],
        [1, 0, 1],
        [0, 1, 0],
        [0, 0, 0],
        ])
    outputSet=array([
            [-1],
            [-1],
            [-1],
            [0],
            [0]])
    print(inputSet, "\n")
    print(outputSet, "\n")
    syn0=2*np.random.random((3,4)) - 1
    syn1=2*np.random.random((4,1)) - 1  
    
    print("training")
    for q in range(0, 80000):
        l0=inputSet
        l1=nonlin(np.dot(l0, syn0))
        l2=nonlin(np.dot(l1, syn1))

        l2_error=outputSet-l2
        if(q%10000)==0:
            if debug:
                print ("Error:" + str(np.mean(np.abs(l2_error))))        
                print(syn0, "\n")
                print(syn1, "\n")
            else:
                print(float(q/80000), "%")
        
        l2_delta = l2_error*nonlin(l2,deriv=True)
        l1_error = l2_delta.dot(syn1.T)
        l1_delta = l1_error*nonlin(l1,deriv=True)

        syn1 += l1.T.dot(l2_delta)
        syn0 += l0.T.dot(l1_delta)

    print("trained")
    while True:
        arr = [int(i) for i in input().split()]
        l0=arr
        l1=nonlin(np.dot(l0, syn0))
        l2=nonlin(np.dot(l1, syn1))
        print(l2)