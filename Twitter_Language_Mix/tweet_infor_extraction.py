#Created by Srividhya Chandrasekharan
import matplotlib.pyplot as plt
import langid
import iso639 #Library for working with ISO639-2 language codes.
#Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json


#a big dictionary of languages and their 2 char ISO 639 code
ISO639_2 = {'und':'Undetermined','ab': 'Abkhaz','aa': 'Afar','af': 'Afrikaans','ak': 'Akan','sq': 'Albanian','am': 'Amharic','ar': 'Arabic','an': 'Aragonese','hy': 'Armenian','as': 'Assamese','av': 'Avaric','ae': 'Avestan','ay': 'Aymara','az': 'Azerbaijani','bm': 'Bambara','ba': 'Bashkir','eu': 'Basque','be': 'Belarusian','bn': 'Bengali','bh': 'Bihari','bi': 'Bislama','bs': 'Bosnian','br': 'Breton','bg': 'Bulgarian','my': 'Burmese','ca': 'Catalan; Valencian','ch': 'Chamorro','ce': 'Chechen','ny': 'Chichewa; Chewa; Nyanja','zh': 'Chinese','cv': 'Chuvash','kw': 'Cornish','co': 'Corsican','cr': 'Cree','hr': 'Croatian','cs': 'Czech','da': 'Danish','dv': 'Divehi; Maldivian;','nl': 'Dutch','dz': 'Dzongkha','en': 'English','eo': 'Esperanto','et': 'Estonian','ee': 'Ewe','fo': 'Faroese','fj': 'Fijian','fi': 'Finnish','fr': 'French','ff': 'Fula','gl': 'Galician','ka': 'Georgian','de': 'German','el': 'Greek,rn','gn': 'Guarani','gu': 'Gujarati','ht': 'Haitian','ha': 'Hausa','he': 'Hebrew (modern)','hz': 'Herero','hi': 'Hindi','ho': 'Hiri Motu','hu': 'Hungarian','ia': 'Interlingua','id': 'Indonesian','ie': 'Interlingue','ga': 'Irish','ig': 'Igbo','ik': 'Inupiaq','io': 'Ido','is': 'Icelandic','it': 'Italian','iu': 'Inuktitut','ja': 'Japanese','jv': 'Javanese','kl': 'Kalaallisut','kn': 'Kannada','kr': 'Kanuri','ks': 'Kashmiri','kk': 'Kazakh','km': 'Khmer','ki': 'Kikuyu,yu','rw': 'Kinyarwanda','ky': 'Kirghiz,yz','kv': 'Komi','kg': 'Kongo','ko': 'Korean','ku': 'Kurdish','kj': 'Kwanyama,yama','la': 'Latin','lb': 'Luxembourgish','lg': 'Luganda','li': 'Limburgish','ln': 'Lingala','lo': 'Lao','lt': 'Lithuanian','lu': 'Luba-Katanga','lv': 'Latvian','gv': 'Manx','mk': 'Macedonian','mg': 'Malagasy','ms': 'Malay','ml': 'Malayalam','mt': 'Maltese','mi': 'Maori','mr': 'Marathi (Marathi)','mh': 'Marshallese','mn': 'Mongolian','na': 'Nauru','nv': 'Navajo,ho','nb': 'Norwegian Bokmal','nd': 'North Ndebele','ne': 'Nepali','ng': 'Ndonga','nn': 'Norwegian Nynorsk','no': 'Norwegian','ii': 'Nuosu','nr': 'South Ndebele','oc': 'Occitan','oj': 'Ojibwe,wa','cu': 'Old Church Slavonic','om': 'Oromo','or': 'Oriya','os': 'Ossetian,tic','pa': 'Panjabi,abi','pi': 'Pali','fa': 'Persian','pl': 'Polish','ps': 'Pashto,to','pt': 'Portuguese','qu': 'Quechua','rm': 'Romansh','rn': 'Kirundi','ro': 'Romanian,avan','ru': 'Russian','sa': 'Sanskrit (Samskrta)','sc': 'Sardinian','sd': 'Sindhi','se': 'Northern Sami','sm': 'Samoan','sg': 'Sango','sr': 'Serbian','gd': 'Scottish Gaelic','sn': 'Shona','si': 'Sinhala,alese','sk': 'Slovak','sl': 'Slovene','so': 'Somali','st': 'Southern Sotho','es': 'Spanish; Castilian','su': 'Sundanese','sw': 'Swahili','ss': 'Swati','sv': 'Swedish','ta': 'Tamil','te': 'Telugu','tg': 'Tajik','th': 'Thai','ti': 'Tigrinya','bo': 'Tibetan','tk': 'Turkmen','tl': 'Tagalog','tn': 'Tswana','to': 'Tonga','tr': 'Turkish','ts': 'Tsonga','tt': 'Tatar','tw': 'Twi','ty': 'Tahitian','ug': 'Uighur,ur','uk': 'Ukrainian','ur': 'Urdu','uz': 'Uzbek','ve': 'Venda','vi': 'Vietnamese','vo': 'Volapuk','wa': 'Walloon','cy': 'Welsh','wo': 'Wolof','fy': 'Western Frisian','xh': 'Xhosa','yi': 'Yiddish','yo': 'Yoruba','za': 'Zhuang,ng','zu': 'Zulu'}

# We use the file saved from last step as example
tweets_filename = 'twitter_stream_10k_tweets.txt'
tweets_file = open(tweets_filename, "r")

#Creating dictionary to hold language ID and count of occurence

language_dict = {"und": "Undeterminded", "en": "English(default) ",  "ar": "Arabic", "bn":"Bengali" , "cs":"Czech" ,"da":"Danish" , "de":"German" ,  "el":"Greek" , "es":"Spanish" , "fa":"Persian" , "fi":"Finnish" ,  "fil":"Filipino" , "fr":"French" ,  "he":"Hebrew" , "hi":"Hindi" ,  "hu":"Hungarian" , "id":"Indonesian" , "it":"Italian" , "ja":"Japanese" , "ko":"Korean" ,  "msa":"Malay" , "nl":"Dutch" , "no":"Norwegian" ,"pl":"Polish" , "pt":"Portuguese" , "ro":"Romanian" ,  "ru":"Russian" ,  "sv":"Swedish" ,  "th":"Thai" ,  "tr":"Turkish" ,  "uk":"Ukrainian" ,  "ur":"Urdu" ,  "vi":"Vietnamese","zh":"Chinese" }
dict = {} 
num_lang = "" #number of languages found in the tweets extracted from Twitter
und_lang = 0 #number of "und" found in the tweets with text
tweets_count = 100000.0 #number of tweets extracted
num_lang_supported_by_twitter = 34
num_tweet_texts = 0 #the number of tweets with textual content

#using langid
lang_dict={} #contains languages identified and the number of tweets that are written in that language
tweets_file = open(tweets_filename, "r")
num_lang_ided = 0
lang_ided = ""

#count to see how similar langid and twitter's machine lang detection works:-
agree=0
disagree=0
disagreed_langs=""

#location stats
count_geo_tagged_tweets = 0
count_tweets_from_US = 0
count_geotagged_tweets_from_US = 0
US_dict={}

#plotting purposes
country_dict={}
count_countries = 0
plt_lang_dict={}

for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet:
            num_tweet_texts+=1;
            language = tweet['lang'].encode("ascii") #using JSON's lang attribute
            lang_detected = langid.classify(tweet['text'])[0] #using python library langid
            #print language, lang_detected
            if language == lang_detected:
                agree+=1
            else:
                disagree+=1
                disagreed_langs+=language+" and "+lang_detected+" ; "

            #creating/updating dictionary based on JSON's lang attribute
            if language=='und' or language not in ISO639_2:
                und_lang+=1
            #else:
            if language in dict:
                dict[language]=dict[language]+1
            else:
                dict[language]=1
                if language in ISO639_2:
                    num_lang+=language+" : "+ISO639_2[language]+", "
                else:
                    num_lang+=language+" : "+ISO639_2['und']+", "
                #num_lang+=language_dict[language]
                #num_lang+=iso639.to_name(language)+", "

            #creating/updating another dictionary based on langid's results
            if lang_detected in lang_dict:
                lang_dict[lang_detected]=lang_dict[lang_detected]+1
            else:
                lang_dict[lang_detected]=1
                num_lang_ided +=lang_dict[lang_detected]
                #lang_ided+=iso639.to_name(lang_detected)+", "
                lang_ided+=ISO639_2[lang_detected]+", "


            #location stats finding
            #filter tweets from USA
            #print tweet['place'] #gives location from which tweet originated
            #print tweet['user']['location'] #user picked location

            if 'place' in tweet and tweet['place'] != None:
                #print tweet['place']
                country = tweet['place']['country'].encode("ascii")
                country_code = tweet['place']['country_code']

                #updating the dictionary
                if country in country_dict:
                    country_dict[country]+=1
                else:
                    country_dict[country]=1

                if country_code=="US" or country=="United States":
                    #creating a dictionary with languages and their counts...
                    if language in US_dict:
                        US_dict[language]=US_dict[language]+1
                    else:
                        US_dict[language]=1

                    num_lang+=language_dict[language]
                    #num_lang+=iso639.to_name(language)+", "
                    #print "found a tweet from USA"
                    count_tweets_from_US += 1
                    if user_info['geo_enabled']==True:
                        count_geotagged_tweets_from_US += 1

            if 'geo_enabled' in tweet['user']:
                user_info = tweet['user']
                if user_info['geo_enabled']==True:
                    count_geo_tagged_tweets+=1
                    #print "Found a geotagged tweet bruh!!"
        
    except:
        # read in a line is not in JSON format (sometimes error occured)
        #print "error"
        continue

print "\n\n*******************Q2*************"
print "\n",tweets_count,"tweets were extracted from Twitter using the Twitter Streaming API"
print "\n","Out of",tweets_count,"tweets extracted, the No. of tweets with text are: ",num_tweet_texts
print "\n","Out of",tweets_count,"tweets extracted, non-textual updates are: ",(tweets_count-num_tweet_texts)
print "\n",count_geo_tagged_tweets," tweets were geolocation tagged"
print "\n","Tweets from",len(country_dict)," countries were analyzed!"
print "\n","Dictionary that shows the distribution of tweets from different countries = ",country_dict


#printing some stats bruh!
set_of_lang_captured =  set(dict.keys())
languages_in_tweets = len(set_of_lang_captured)


percent_identified = 100.0*(1.0*(num_tweet_texts-und_lang)/num_tweet_texts)
print "\n","Twitter's ability to detect language from tweets' texts for tweets with text is : ",percent_identified,"%"
print "\n","No. of languages found in the extracted tweets/status update are",languages_in_tweets

print "\n","Dictionary of the languages(ISO639 code, count of occurence) detected by Twitter: ",dict

#fraction_unsupported = 100

print"_______________PERCENT DISTRIBUTION OF LANG______________________________________"
for l in dict.keys():
    fraction = 100.0 * (1.0*dict[l]/num_tweet_texts)
    #fraction_unsupported-=fraction
    #print iso639.to_name(l),":",fraction,"%"
    if l in ISO639_2:
        print ISO639_2[l],":",fraction,"%"
    else:
        print ISO639_2['und'],":",fraction,"%"


print "\n\n****************Q3***************************"
print "\n","No. of languages found in the extracted tweets/status update are",num_lang_ided 
print "\nThey are",lang_ided

print "\n","Twitter's machine language detection and Python's langid agreed ",agree," time(s) and disagreed",disagree," time(s)"
#print disagreed_langs
print "\n","Twitter's machine detection gives out 'und'(short for Undetermined) for the attribute 'lang' for languages not supported by Twitter. LangID being pretrained with 97 languages is able to correctly detect languages (however remote they are). Thus, there arises some conflict in the language detected by Twitter and langid sometimes."

#print "Undetermined Languages : ",fraction_unsupported,"%"
print"\n","Dictionary got by doing language analysis on tweets using langid : ",lang_dict


print"\n************************************Q4*******************"

print "\nDictionary to show distribution of languages in the USA = ",US_dict
print"\n _______________PERCENT DISTRIBUTION OF LANG(USA)______________________________________"
for l in US_dict.keys():
    fraction = 100.0 * (1.0*US_dict[l]/count_tweets_from_US)
    #fraction_unsupported-=fraction
    #print iso639.to_name(l),":",fraction,"%"
    if l in ISO639_2:
        print ISO639_2[l],":",fraction,"%"
    else:
        print ISO639_2['und'],":",fraction,"%"

print "\n","Out of ",count_tweets_from_US," tweets from USA, ",count_geotagged_tweets_from_US," were geotagged."

print "*********************************************************"
tweets_file.close()


'''
plt_lang_dict=lang_dict

for key in plt_lang_dict.keys():
    plt_lang_dict[ISO639_2[key]] = plt_lang_dict.pop(key)

print plt_lang_dict
'''