class Sol:
    def word_pattern(self,pattern,str):
        list=[]
        list_str=str.split()
        for i,char in enumerate(pattern):
            if char not in list :
                if list_str[i] in list:
                    return False
                list=list+[char,list_str[i]]
            elif char in list and list[list.index(char)+1]!=list_str[i]:
                return False
            elif list_str[i] in list and pattern[i]!=list[list.index(char)]:
                return False

        return True
if __name__ == '__main__':
    p1=Sol()
    print(p1.word_pattern("baaa","cat dog dog dog"))
