<h2>Small project.</h2><br>
Main.py is the speech-to-text where text is stored in op.txt.
Apply.ipynb is from where the image is displayed by taking it from the images folder according to the last sentence from op.txt file.<be><hr>
Run main.py then go to apply.ipynb,<br>
make sure that you change the directory to yours before running.<br>
In the images folder, every image name needs to be changed to some adjective+keyword name.
<hr>
<br><h4>Dependencies required</h4>
  
```
pip install -r requirements.txt
```
<hr><br>
<b>Explaination for the Apply.ipynb</b><br>

In this code, we first define the list of keywords to extract. We then download the NLTK tagger if necessary 
and tokenize the sentence into words and tags using the pos_tag function.<br>

Next, we initialize empty lists for adjectives and keywords. 
We then loop through each word and tag, and check if the word is a keyword. 
If the word is a keyword, we check if there is an adjective before this keyword. 
If there is, we add the adjective and keyword to their respective lists.<br>

After that, we combine the adjectives and keywords into phrases which is a list. We then filter the phrases list into 2 more list which are latest_phrases_list and rejected_phrases_list<br>
latest_phrases_list is a unique list for all the final keyword occurence in phrases list and rejected_phrases_list is the difference of phrases list and latest_phrases_list.<br>

Finally, we define the path to the image folder and loop through each phrase from both list. 
For each phrase, we get the keyword from the phrase and define the path to the subfolder. 
We then search for the image file in the subfolder using the <b>os.listdir<b> function.<br>
If the image file is found (for latest_phrases_list), we combine the subfolder path and the image file name and display the image using the PIL library.<br> 
If the image file is found (for rejected_phrases_list), we print a message saying "Image present for the phrase'..'".
<br>If no image is found (for both list), the phrase is appended to a feedback file along with a timestamp and a message indicating that the image was not found.<br>
