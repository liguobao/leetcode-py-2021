class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def word_contians(word1, word2):
            m, n = len(word1), len(word2)
            w1_array = list(word1)
            w2_array = list(word2)
            if m+1 != n:
                return False
            # 取前后字符串的差集
            un_array = []
            for x in w2_array:
                if x not in w1_array:
                    un_array.append(x)
            if len(un_array) >0:
                one_c = un_array[0]
            else:
                one_c = max(set(w2_array), key=w2_array.count)
            for i in range(m+1):
                w_array = w1_array.copy()
                w_array.insert(i, one_c)
                if "".join(w_array) == word2:
                    return True         
            return False

        words.sort(key=lambda x: len(x))
        words_count = len(words)
        dp = [1] * words_count
        result = 0
        for i in range(words_count):
            for j in range(i):
                # 判断前一个字符和当前字符是否符合包含关系
                # 前一个字符串添加任意字符，可以变成后一个字符串
                if word_contians(word1=words[j], word2=words[i]):
                    dp[i] = max(dp[i], dp[j]+1)
            result = max(result, dp[i])
        return result


# words = ["a", "b", "ba", "bca", "bda", "bdca"]
# result = Solution().longestStrChain(words)
# print(f"words:{words},result:{result}")


# words = ["heond","wmbhhot","afdzknhh","mdsimgpqewdwoo","wmbhthviot","slepzhpi","pkvhvwdcqsrbt","glkdcip","vnkwnwznjiiebjst","pkvhwdcqsrbt","sdveezfru","krxbxoxhgupawp","hfuoymvwzerk","nqqzqmjbxjg","huomvzrk","zsmqpwc","oiugsmf","oiugsmfrw","vllpohgnj","afgpocwiptcken","zricanuvv","wqdctrivii","nqqjbxjg","beeedij","hyqamuuqbtpayl","zricavjnuvv","afdznkjnthh","joniyugswsmfreww","rxxoxhgpwp","wsijcjazz","vlvlpibohglnj","beei","wtccvloxactpi","wvngcdrmkpm","jatspqmvczxbezt","slepzhpiat","beeedivjh","oniugsmfrew","yaub","hon","hvizwkbeoc","zricavjnuyvv","slepzhpia","wmbhthvot","slxegpzhpiaetd","nswoj","pkwdcqsrbt","ztgocsvgild","swoj","zrmicavjnuymvv","thnufatvyuzsy","slxegpzhpihauetd","hyqaubtpal","krxbxoxhgpwp","slxegpzhpiatd","dh","yqaubt","vlvlpiibonfhglnj","bbeeedivjh","zspwc","wmbhhvot","nqqozvqmjbxjg","jatspqmvczxbz","ztgcsvgl","qtsloluy","ztcsvgl","mdbzvfpceaaebk","aspmvcxbz","t","oiugsmfr","msimgpqedwoo","bpbga","eqtslsoluby","og","n","homvzrk","rwrlqltzsinaxt","dzh","nswojj","yqaub","oigsmf","zpsmqpwc","ogf","kwdcqsrbt","phzboklxxikhwy","bbeeedievdjh","vlvlpibonfhglnj","wbhho","wsijpmchjnazz","hojm","ttpmv","wsijchjazz","riuddyqramdwo","wcloxacp","vllpognj","zpwc","vngcdrmkp","swj","kwcrb","slxegpzhpiauetd","hvizwhkbehoc","krxbxoxhgupwp","aspmcbz","wvungcdrmckpm","jaspqmvczxbz","jatspqmvczxbez","kbexhubrl","heonydea","vlvlpibohgnj","wccloxacp","hfuoymvwzrk","vlvlpbohgnj","lepzpi","mdsximgpqewdwoo","tp","clgqzo","sveezfru","sdvejoezfru","ttp","hyqtamuuqbtpayl","s","hozrk","nqqyozvqmjbxjg","hyqaubtpl","dzhh","hyqaubtp","hho","ttpm","dbzvfpceaaebk","zrmicavjnuyvv","jatspqmvczxbezvt","nnvswojj","ztgcsvgil","beeedijh","wmbhthfviot","ehojm","beeedi","eqtsloluy","vlpgnj","svgl","homzrk","mdbzvflpceaaebk","wccloxacpi","slepzpi","heoojnmydea","ho","nqzqmjbxjg","cgqzo","nqzqjbxjg","oniugssmfrew","wrsiyqzrswvudn","wrsiyzrswvudn","bbeeeedievdjh","e","heoojnydea","zricnuvv","sdvejwoezfru","vngcdrmkpm","aspmvcbz","csvgl","hyqaubt","krxbxoxhgupawwbp","wvungcdrmkpm","dbzvfceaebk","slxegpzhpiat","khyqtamuuqbtpayl","msimgpqewdwoo","zpsmqpawc","pehojm","heon","vnkwnwzjiebjst","wtccvloxaectpi","cb","nqqzvqmjbxjg","glhub","bbseeeedievxdjhc","vlvlpibofhglnj","bbeeeedievxdjh","sw","ezi","joniyugssmfreww","hfuomvwzrk","wbhhot","vlgnj","eriuddyqramduwo","wvqdzctrivikki","bei","jaspmvczxbz","kwcrbt","whho","eqtslsoluy","vllpbohgnj","bpbaga","heondea","hfuoyamvwzerk","slxepzhpiat","joniugssmfrew","glkcip","aspmb","r","wmbhthfvviot","xhnvizwhkbehoc","kwcsrbt","afdznhh","o","zricajnuvv","pkhwdcqsrbt","dbzvfpceaebk","zetgocsvgild","be","aspmbz","yab","fdznhh","oiugsmfrew","svg","hvizwhkbeoc","hoj","joniyugssmfrew","nqzqyozfvqmjbxjg","afdzknthh","heoojnymyodea","sdvejwoezfrju","pkvhvwdcqksrbt","vnkwnwznjiebjst","epzpi","fdzhh","afgpoclwiptcken","ezpi","zcsvgl","nvswojj","hfuomvzrk","ogsmf","wsijpchjazz","kwcqsrbt","wvqdctriviki","bbeeeedievxdjhc","heonda","zsmpwc","beedi","ogmf","ho","heoojnymydea","wtccvloxacpi","jaspmvcxbz","vnkwnwziebjst","wsijcjaz","hyqamubtpayl","nqzqyozvqmjbxjg","hyqamuubtpayl","afdzkjnthh","xhnvizwqhkbehoc","sveezfu","c","ry","wtccloxacpi","krxxoxhgpwp","sdvejezfru","wqdctriviki","on","tmtpmv","peheojm","bbeeedievjh","krxbxoxhgupawbp","riuddyqramduwo","ztgocsvgil","vlpognj","wvqdzctriviki","mimgpqedwoo","wsijpmchjazz","hnvizwhkbehoc","heoonydea","hyqamubtpal","tsloluy","uzrmricavjnuymvv","zrmricavjnuymvv"]
words = ["a","aa","aab","aabb","bbaac"]
result = Solution().longestStrChain(words)
print(f"words:{words},result:{result}")
