This project attempts to quantify change in the “diversity of ideas” in large historical corpus over the past century. It uses machine learning libraries like 
TextBlob and NLTK's VADER to classify sentences or clauses as opinionated ones. For every decade, the program then calculates the total number of opinionated sentences/clauses 
(from the 1900s-2000s) and takes the ratio of that against the total number of sentences or clauses, respectively (if the total number of 
opinionated sentences/clauses were to be counted and a graph were to be constructed on that, it would not be accurate as naturally less texts and therefore less 
opinionated sentences/clauses are available the further back you go in time.) The program then constructs a graph that displays the ratio of opinionated 
sentences/clauses to total sentences/clauses for each decade of the 20th century, allowing one to track the change in the amount of opinions over the 20th century. 
This change in opinions was tracked in three categories - newspaper, fiction, and magazine articles - through the century. 

There are primarily two ways in which the change in opinions can be tracked over the past century. The first is by looking at the number of opinionated 
clauses versus the total number of clauses in a decade. The second way is by looking at the number of of opinionated sentences versus the total number of sentences 
in a decade. The algorithm to split sentences into clauses is not 100% accurate, and neither is TextBlob and NLTK's VADER's classifying sentences/clauses as 
opinionated ones. The three are however, fairly accurate, and can give one a rough idea of how the diversity of ideas changed over the 20th century. 

The dataset used in this project is included in the project's files. It was downloaded as sample data from COHA (https://www.corpusdata.org/formats.asp). 
The data was downloaded as "Linear Text" for "COHA."

To run the project, change the value of the corpus_root string in "def sentiment_analyze (category):". "C:\Users\user\PycharmProjects\" will have to be changed 
according to where the project is stored. The rest of corpus_root does not have to be changed as the dataset is included in the project files.

According to the results, the “diversity of ideas” in the areas of fiction, magazine, and newspaper decreased overall over the span of the 20th century. See the images in the Textblob folder in src for more detailed graphs. 

Credit: 
The algorithm used for splitting sentences into clauses was adapted from original code posted to 
Stack Overflow: https://stackoverflow.com/questions/65227103/clause-extraction-long-sentence-segmentation-in-python by user 
polm23 (https://stackoverflow.com/users/355715/polm23). 
