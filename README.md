# nauka-angielskiego

Spec:
- Python 3.10

Basic Concept:
- imports 3000 most common English words from [3000-English-words list]
- gives the user 10 words one by one and places it in his [hand]
- the user [interacts] with those words [by translating] each of them (first eng->pol then pol-eng)
- the user needs to get [6 stars] (or points) for each word (you get 3 from eng->pol translation and 3 from pol-eng translation)
- you [get 1 star] when you successfully translate the word
- [first 3] times you translate from English to Polish, [later 3] from Polish to English
- whenever you make a [mistake], [1 star is taken away] from you
- if you [master the word] (6 stars) the word [disappears from your hand] and is [replaced by a new word] from the 
  [Words-to-Master list], which consists of words from [3000-English-words list] minus [hand] and [Mastered-Words list] 
- mastered words are placed in the [Mastered-Words list]

Implementation:
- for multilingual version use APIs for translation 
- if it's only eng-pol version a manual creation of [translated words list] is much simpler 
- when first starting the app, give the user 10 random words with their translations
- any other app usage is testing the user by asking for translations
- the user has access to his [hand] from the menu, he can check both eng and pol translations
- he can also access the [Mastered-Words list]
- user gets [tested] max [once per day]


- possible options for later:
- test the user occasionally (every week/ random) by giving him a list of 10 words from those he already learned 
  (mastered words list)- if he fails the test for any particular word - that word is placed in a separate list, which
  takes priority as a source for new words
- The Final test (7th star): ask the user to create a sentence with the word and send it to chat GPT to check it
- multilingual version
- use a dictionary API to give definitions and all kinds of information about the word (accessible from the menu)
- additional information like: how many mistakes per each word, which word was moved back from mastered, 
  how many times tested, how many times user completed the test flawlessly etc.




APIs:
https://console.cloud.google.com/freetrial/signup/tos?facet_utm_source=01&facet_utm_campaign=01&facet_utm_medium=01&facet_url=https:%2F%2Fcloud.google.com%2Ftranslate%2Fdocs%2Freference%2Frest&facet_id_list=%5B39300012,%2039300021,%2039300118,%2039300196,%2039300251,%2039300318,%2039300320,%2039300325,%2039300346,%2039300354,%2039300363,%2039300373,%2039300409,%2039300422,%2039300434,%2039300471,%2039300488,%2039300496,%2039300497%5D
to get word translations to various languages

