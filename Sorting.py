class sorting:
    def Bubble_Sort(self,arr):
        print(f"Initial Array={arr}\n")

        for i in range(len(arr)-1):
            print(f'\tIteration-{i+1}')
            for j in range(0,len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                print(f'pass-{j+1}--->{arr}')
            print(f'End=={arr}',end='\n\n')

        print(f"\nFinal Array={arr}\n")


    def Insertion_Sort(self,arr):
        print(f"Intitial Array={arr}\n")

        for i in range(1,len(arr)):
            print(f"\tIteration-{i}")
            key = arr[i]
            j = i-1
            while j>-1 and arr[j]>key :
                arr[j+1]=arr[j]
                j-=1
                print(f"Move--{arr}")
            arr[j+1]=key
            print(f"End = {arr}",end="\n\n")

        print(f"\nFinal Array={arr}\n")


    def Selection_Sort(self,arr):
        print(f"Initial Array={arr}\n")

        for i in range(len(arr)-1):
            print(f"\tIteration-{i+1}")
            ind = i
            for j in range(i+1,len(arr)):
                           if arr[ind]>arr[j]:
                               ind=j
            arr[i],arr[ind]=arr[ind],arr[i]
            print(f"End = {arr}")
        print(f"\nFinal Array={arr}\n")


    def Merge_Sort(self,arr):
        print(f"Intial Array={arr}\n")

        def divide(ar,s,e):
            if s==e:return
            mid = s + (e-s)//2
            print(f"First Part-{ar[s:mid+1]} Second Part-{ar[mid+1:e+1]}")
            divide(ar,s,mid)
            divide(ar,mid+1,e)
            merge(ar,s,mid,e)
            print(f"Merged -{ar[s:e+1]}",end="\n\n")

        def merge(ar,s,mid,e):
            tem = [0]*(e-s+1)
            i,j,k = s,mid+1,0
            while i<=mid and j<=e :
                if ar[i]<ar[j] :
                    tem[k]=ar[i]
                    i+=1
                else :
                    tem[k]=ar[j]
                    j+=1
                k+=1
            while i<=mid :
                tem[k]=ar[i]
                k+=1
                i+=1
            while j<=e:
                tem[k]=ar[j]
                k+=1
                j+=1
            
            k=0
            while s<=e :
                ar[s]=tem[k]
                s,k=s+1,k+1

        divide(arr,0,len(arr)-1)
        print(f"\nFinal Array={arr}\n")

    def Quick_Sort(self,arr) :
        print(f"Initial Array={arr}\n")

        def partition(arr,s,e):
            if s>=e :return 
            p=pivot_first_ele(arr,s,e)
            print(f'intermidiate--> {arr[s:p]} - {arr[p]} -{arr[p+1:e+1]}')
            partition(arr,s,p-1)
            partition(arr,p+1,e)
        def pivot_last_ele(ar,s,e):
            pi = ar[e]
            i = s-1
            for j in range(s,e):
                if ar[j]<=pi :
                    i+=1
                    ar[j],ar[i]=ar[i],ar[j]
            ar[i+1],ar[e]=ar[e],ar[i+1]
            return i+1
        def pivot_first_ele(ar,s,e):
            pi = ar[s]
            i = e+1
            for j in range(e,s,-1):
                if pi<ar[j] :
                    i-=1
                    ar[j],ar[i]=ar[i],ar[j]
            ar[i-1],ar[s]=ar[s],ar[i-1]
            return i-1
        
        partition(arr,0,len(arr)-1)
        print(f"\nFinal Array={arr}\n")

    def Counting_Sort(self,arr):
        print(f"Initial Array={arr}\n")
        min_ele,max_ele = min(arr),max(arr)
        count = [0]*(max_ele-min_ele+1)
        for ele in arr:
            count[ele-min_ele]+=1
 
        for i in range(1,len(count)):
            count[i]+=count[i-1]

        ans = [0]*len(arr)

        for ele in arr:
            ans[count[ele-min_ele]-1]=ele
            count[ele-min_ele]-=1

        print(f"Final Array={ans}\n")


k = sorting()
l = list(map(int,input().split()))
k.Counting_Sort(list(l))
k.Insertion_Sort(list(l))
k.Merge_Sort(list(l))
k.Quick_Sort(list(l))
k.Bubble_Sort(list(l))
k.Selection_Sort(list(l))

