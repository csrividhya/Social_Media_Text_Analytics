#Created by Srividhya Chandrasekharan
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt
import math


country = {'Canada': 4, 'Brazil': 2, 'Australia': 2, 'Brasil': 19, 'South Africa': 2, 'Nepal': 1, 'Venezuela': 2, 'Uruguay': 2, 'India': 3, 'Costa Rica': 2, 'United States': 65, 'Malaysia': 5, 'Norge': 1, 'Germany': 1, 'Colombia': 2, 'Martinique': 1, 'Republic of Korea': 1, 'Argentina': 5, 'Republic of the Philippines': 3, 'Ecuador': 1}
from operator import itemgetter
s = sorted(country.items(), key=itemgetter(1),reverse=True)
print s


num_tweets=[]
countryID=[]

countryID=[i[0] for i in s]
num_tweets=[int(i[1]) for i in s]

#plot as bar graph Teams by num_tweets
xlocations = np.array(range(len(s)))+0.5
plt.xticks(xlocations+0.50, countryID)
plt.xticks(rotation=-45)
start=int(min(num_tweets))
end=int(max(num_tweets))
plt.ylim(start-5,end)
plt.yticks(np.arange(0,end+10,5.0))
plt.ylabel('num_tweets') 
plt.title("Countries by number of textual tweets got on Tue Sep 05 02:37:02 +0000 2017")
plt.bar(xlocations,num_tweets,color=['crimson']) #'crimson'
plt.show()


#*************************
#plotting languages vs count of tweets in them

lang = {'Estonian': 16, 'Hebrew (modern)': 34, 'Bulgarian': 2, 'French': 85, 'Bengali': 6, 'Pashto,to': 3, 'Tamil': 11, 'Haitian': 4, 'Oriya': 1, 'Nepali': 7, 'Finnish': 30, 'Albanian': 8, 'Tagalog': 37, 'Serbian': 1, 'Malayalam': 3, 'Aragonese': 25, 'Spanish; Castilian': 820, 'Walloon': 5, 'Catalan; Valencian': 14, 'Galician': 36, 'Czech': 17, 'Slovak': 5, 'Urdu': 36, 'Polish': 35, 'Occitan': 7, 'Xhosa': 4, 'Swedish': 12, 'Norwegian Bokmal': 1, 'Uighur,ur': 3, 'Kirghiz,yz': 1, 'Azerbaijani': 20, 'Faroese': 2, 'Kannada': 2, 'Amharic': 28, 'Indonesian': 106, 'Marathi (Marathi)': 11, 'Zulu': 5, 'Macedonian': 1, 'Georgian': 12, 'Norwegian': 6, 'Thai': 262, 'Afrikaans': 6, 'Slovene': 18, 'Basque': 11, 'Japanese': 1780, 'Croatian': 7, 'Chinese': 172, 'Arabic': 497, 'Breton': 12, 'Swahili': 25, 'Icelandic': 3, 'Latvian': 5, 'Turkish': 68, 'Italian': 80, 'English': 3004, 'Hindi': 53, 'Korean': 443, 'Malagasy': 4, 'Khmer': 18, 'Hungarian': 14, 'Bosnian': 5, 'Lithuanian': 22, 'Malay': 37, 'Luxembourgish': 7, 'Russian': 38, 'Kazakh': 1, 'Irish': 6, 'Armenian': 4, 'Sinhala,alese': 11, 'Norwegian Nynorsk': 2, 'Javanese': 14, 'Greek,rn': 12, 'German': 89, 'Persian': 28, 'Mongolian': 3, 'Vietnamese': 10, 'Kinyarwanda': 21, 'Dutch': 40, 'Northern Sami': 3, 'Lao': 1, 'Welsh': 4, 'Maltese': 25, 'Assamese': 2, 'Kurdish': 2, 'Romanian,avan': 20, 'Danish': 29, 'Quechua': 10, 'Latin': 61, 'Esperanto': 19, 'Portuguese': 413, 'Ukrainian': 1, 'Panjabi,abi': 1}
from operator import itemgetter
l = sorted(lang.items(), key=itemgetter(1),reverse=True)


l=l[:10]
print l
num_tweets=[]
langID=[]

langID=[i[0] for i in l]
num_tweets=[int(i[1]) for i in l]
print langID

#plot as bar graph Teams by num_tweets
xlocations = np.array(range(len(l)))+0.5
plt.xticks(xlocations+0.50, langID)
plt.xticks(rotation=-45)
start=int(min(num_tweets))
print start
end=int(max(num_tweets))
print end
plt.ylim(start-5,end)
plt.yticks(np.arange(50,end+100,100.0))
plt.ylabel('num_tweets') 
plt.title("Languages by number of textual tweets got on Tue Sep 05 02:37:02 +0000 2017")
plt.bar(xlocations,num_tweets,color=['chartreuse']) #'crimson'
plt.show()