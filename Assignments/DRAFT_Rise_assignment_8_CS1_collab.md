## Anyone, anywhere, anybody: computing Austen’s differences
### CS21-ENGL35 Fall 2017 collaborative assignment

DRAFT

## Intro

In ENGL035: The Rise of the Novel we have been studying the history of the novel. We’re interested in the history of the novel for many reasons. For a long time, people have written and read novels for entertainment and for instruction; to learn about people unlike themselves, and to see representations of people like themselves circulate in print; to learn about the world, and to learn new ways of thinking and feeling. In this class, we have been especially interested in how the novel developed both as a reflection of social and psychological life and a model for it. That is, the novel was a form that reflected what it was like to think, feel, and live as an everyday and historically unremarkable person, but it was also a form that opened up new possibilities for how a reader might think, feel, and live as an everyday person. The novel helped you learn how you might fall in love, grow up, be (or become, or refuse to become) a woman (or a man), grow old, or mourn the loss of a child. Perhaps most importantly, the novel could help you understand (or believe) that you are (or are potentially) a valuable and interesting person even in the face of overwhelming evidence that you are actually a very ordinary and very replaceable person.

When we read novels for the purpose of discussing them in a classroom, we read them in part as we read when we read for pleasure - from cover to cover, following the plot, identifying (or not) with characters, enjoying the scenery. But we also read them more discontinuously and intensively - skipping around to search for evidence of a claim, dwelling for twenty minutes on a single word (as on that memorable October 25, 2017, when we spent that amount of time discussing the final word of Evelina, which is “Evelina”). This kind of reading takes a long time, novels themselves are long (sometimes VERY long), and the semester and our attention spans are short. Therefore in this class we have only been able to read (give or take) ten novels published over the span of 242 years (1719-1961). During this timespan, hundreds of thousands of novels were published, so we need to be selective.

How do we choose? We choose novels for a syllabus like ours - in which we can only read ten novels - not because they are "average" nor because they are wholly "exceptional," but because they are "exemplary." The are in some (controversial) sense the "best," yes, but they are the best "of their kind." They must somehow represent larger groups of novels (so that we can learn something about "the novel" in the class, not just something about ten random novels), and yet they must also be compelling and important in their own right. We implicitly claim, therefore, that each novel on our syllabus is  representative but also distinctive. Jane Austen's novels, for example, are regularly framed in this way. Though it is clear how they draw on existing conventions, we also imagine them as significantly different from the novels that came before them, and as exerting a strong influence on the novels that came after them. For critic Ian Watt, for example, Austen is innovative in the way she joins different forms of realism that were previously separate, allowing one novel to be both psychologically realist and yet also true to external life. For critics like D.A. Miller and Frances Ferguson, Austen's narrative style (her impersonal narrator and use of free indirect discourse) is both new and trendsetting.  (Interestingly, as we've discussed in class, this razor's-edge logic of the exemplary canon is also a logic the novel itself must negotiate: it must represent characters who are unusual enough to be interesting and yet average enough to pass as everyday people, who in the words of Catherine Gallagher.)

## Comparison: How?

*This assignment will ask: how specifically are Austen's novels (which she wrote and published between approximately 1790 and 1818) different from those of her contemporaries? How different are they from the other eighteenth-century and early-nineteenth-century novels we might read in a class like this one?*

There are a few ways we might go about answering this question. When we read *Evelina*,  we tried to get a sense of a wider ecosystem of fiction in which Burney’s novel appeared by browsing through the titles of novel in bibliographies and skimming some digital facsimiles of fictions in the ECCO database in exercise 5[ADD LINK], and by manipulating catalog metadata created by librarians in exercise 6. In those exercises, we looked at a bit of information about smaller groups of novels - eyeballing 80 or 90 titles to learn what we can. (In the decade that saw the publication of The Life and Strange Surprising Adventures of Robinson Crusoe, for example, how many other novels were published that named themselves “Life” or “Adventures”? How many novels published between 1776 and 1779 had (like the 1778 *Evelina*) a woman's first name as a title?

But is this handful of novels we are reading really representative of the much larger number of novels we are not reading? We need a way of responding to this question. One thing we can do is trust that the individual novels we are reading are to a certain degree representative of much larger groups of novels. (Often, these are novels that people have continued to read since their first publication, so we know at least that many generations of readers have found them compelling.) But if we could dispense with actually reading every novel, and instead construct a description or representation of each novel or or a group of novels that would let us compare them more easily, we might be able to answer some of our questions about how the novels we are actually reading compare to the novels we don't have time to read. One method for doing this is by good old-fashioned skimming of a reduced amount of information about a larger number of novels. When we read Evelina,  we tried to get a sense of a wider ecosystem of fiction in which Burney’s novel appeared by browsing through the titles of novel in bibliographies and skimming some digital facsimiles of fictions in the ECCO database in exercise 5, and by manipulating catalog metadata created by librarians in exercise 6. In these cases, we are looking at a bit of information about a score or a handful of novels - eyeballing titles to learn about what publishers and authors thought readers would be interested in, for example. (In the decade that saw the publication of The Life and Strange Surprising Adventures of Robinson Crusoe, for example, how many other novels were published that named themselves “Life” or “Adventures”?)

What if we want to be able to compare larger groups of novels, more than we can easily eyeball? And what if we want to compare the contents of these novels, rather than their titles or publication information? To do this, we can try computational modeling. In this assignment, we will identify a feature that can be easily extracted from each text or group of texts, and then decide how we might go about representing this in a way that lets us easily compare texts to one another. Clearly, the kinds of features or textual characteristics we can extract (or generate) from texts will severely limit the kinds of questions we can ask. (On the other hand, the very act of having to isolate a machine-identifiable characteristic or group of characteristics in a big group of novels may very well help us think entirely differently about texts and textuality.)

It is important to understand that when we create any computational model of a text or group of texts – whether the fairly simple one in this assignment or much more sophisticated models - we are deliberately choosing the create a VERY reductive description or representation of each text so that we can easily manipulate and compare the representations of a larger number of novels. What we are NOT doing is pretending that this feature in any way stands in for a human reading of the text, or offers any kind of full representation of the text. Rather, are using feature extraction to look closely at and compare one very specific aspect of the text, an aspect that we cannot easily see when we read. Another way to think about what we are doing is not “reduction” of each text to a given feature or set of features, but “transformation” – the creation of a new text that tell us something ABOUT the original texts from which we began. [Cite Ramsay.] (You may notice, by the way, that this tension between imagining a representation as a reduction as opposed to imagining a representation as a transformation is also a current running through some of the literary-critical treatments of novelistic realism we have been examining.)

### More Distinctive Words

How will we make this comparison? In this particular assignment, we are going to compare different texts and collections of texts in order to find out what their most distinctive words are. These distinctive words will - for the purposes of this assignment - act as a very reductive description of the texts they are drawn from. Because this is such a reductive model of a text, we won’t be able to answer most questions a literary critic would have about single text she was studying. However, reducing the scope of our evidence in this way WILL allow us to answer a few questions about a much larger group of texts.

In this exercise, we will be able to compare a novel we have read - Jane Austen's Northanger Abbey (1790/1818) - with a series of other text corpora - the complete works of the uncanonical (and, for the time, old-fashioned) novelists Mary Brunton, with the generation-earlier corpus of Frances Burney, and with Austen's own complete works. We will then move on to compare both Northanger Abbey and Austen’s complete works with two larger collections of novels: a corpus that has been selected to represent "canonical" novels and one that has been selected to represent “the archive”  - to see what we can learn about how the novels we read in The Rise of the Novel compare with the many other novels we aren't reading.

Comparing a text with a corpus, or a corpus with a corpus, is tricky. We could simply calculate raw frequencies: how many times does the word “anyone” appear in Jane Austen’s novels, and how many times in Mary Brunton’s? But of course we have six Austen novels and only two Brunton novels, so this will be unfair. To even things out, we should divide the count of every word by the total number of words in the corpus. Then, at least, we can compare to similar numbers.

Let's take an example. What proportion of Austen’s corpus is made up of the word “everything,” and what proportion of Brunton’s is made up of the word “everything”? It turns out that 'everything' occurs just 2 times out of a total of 340,411 words in Brunton, and 310 out of 752,331 words in Austen.

Even eyeballing this probably tells us that "everything" is much more prevalent in Austen than in Brunton, but let's figure out what precise proportion of "everything" is each author's collected works by dividing the number of occurrances of "everything" by the total number of words in the author's collected works. So for the word 'everything' in Brunton, dividing 2 by 340,411 (and then multiplying by 100 to make percentages) gives us "everything" as ~ 0.00005% of all words, whereas for "everything" in Austen, dividing 310 by 752,331 and then multiplying by 100 will give us "everything" as ~ 0.04% of all words.

The ratio (310/752331) / (2/340411) = 0.00041205267	/ 0.00000587525 = 70.1 which tells us that ‘everything’ is about 70 times more likely to appear in Austen than in Brunton. If we calculate this ratio for every word in both documents, we can  find the set of words for each text or group of texts that are, in a sense, the most important words in that text - if we can judge importance by relative frequency of use.

This is the measure we are using in this exercise. However, there are some limits to what it can tell us, and a number of other methods for comparing texts and corpora exist. (For example, see )
In the "Further Reading" and "Extra Credit" sections you will find ideas and examples of how some people have gone about accounting for these shortcomings. The bottom line, however, is that we may be able to build a better way of determining which words to use as a representation or stand-in for our texts, but they will always remain a very specific and partial representation. This is a *good* thing.


### Corpus: to what can we compare Austen?

Comparing Austen's novels and compete works to "everything else" sounds great in theory; how will it work in practice? First, we need to determine what groups of novels we might want to compare to Austen's; then we need to figure out if they exist in "clean," machine-readable text form. (As we learned in Assignment 4, even if we have a digital facsimile of a novel, using OCR on it won't necessarily give us a good-enough machine-readable text.)

For this assignment, we will use the texts and corpora described below.

All of these corpora are composed of text that were transcribed by a person or people, so they are very accurate. Almost all computational text analysis work requires that we pre-process or "clean" existing machine-readable texts before we can use them. In this case, we have removed metadata and other ancillary text that we don't want to see in our results. The SINGERMENDENHALL corpus is different because it was created via OCR of scanned novels; we then processed the resulting (very messy) text by removing "non-words" (any words that appear < 200 times in the Google ngram corpus) and uppercase words. The programs we use will also include functions that remove or ignore some words; our program, for example, ignores words that appear < 5 times in both texts or corpora that we are comparing.

#### AUSTEN
Our Jane Austen corpus contains the texts of Emma, Lady Susan, Mansfield Park, Northanger Abbey, Persuasion, Pride and Prejudice, and Sense and Sensibility.

#### BRUNTON
Our Maria Brunton corpus contains the novels Discipline and Self-Control.

#### BURNEY
Our Burney corpus contains Cecelia, Evelina, and The Wanderer. [Note: add Camilla]

#### CANON
The “canon” collection contains 44 works of eighteenth- and early-nineteenth-century fiction that are taught frequently in university-level classes on the novel and fiction; we drew them from a survey of 40 recent syllabi for eighteenth-century and history of the novel classs. They are Pamela (1740), Tristram Shandy (1749), Evelina (1778), Robinson Crusoe (1719), Tom Jones (1749), Joseph Andrews (1742), Oroonoko, or The Royal Slave (1688), Moll Flanders (1722), Northanger Abbey (1817), Shamela (1741), Clarissa (1748), The Castle of Otranto (1764), Emma (1815), Roxana (1724), The Female Quixote (1752), The Monk (1796), Fantomina: or, Love in a Maze (1724), The Man of Feeling (1771), A Sicilian Romance (1790), A Sentimental Journey (1768), Humphry Clinker (1771), Gulliver’s Travels (1726), Candide (1759), Castle Rackrent (1800), Mansfield Park (1814), The Fair Jilt (1688), Pilgrim's Progress (1678), The Mysteries of Udolpho (1794), Pride and Prejudice (1813), Les Liaisons Dangereuses (1782), The Princesse de Clèves (1678), Sense and Sensibility (1811), A Simple Story (1791), The Romance of the Forest (1791), Anti-Pamela (1741), Don Quixote (1615), Jane Eyre (1847), The History of Pompey the Little (1750), Belinda (1801), Roderick Random (1748), The History of Rasselas (1759), The Italian (1797), Waverley (1814). (Love in Excess (1719) is on this list but not included because of the lack of a readily available machine-readable text.) They come primarily from the Project Gutenberg archive.

#### Archive
We have two corpora that stand in for the “archive” or - to use the words of Margaret Cohen - “the great unread” (“Narratology in the Archive of Literature,” 61) - all of those books that were published and (possibly) read at one time but which have not been read much since. Our first “archive” corpus is CHAWTON,  a collection of 75 novels drawn from the Chawton House Library’s Novels Online project, which contains little-known novels written (primarily) by women and published during the eighteenth and early nineteenth centuries.

A alternate model for “archive” is SINGERMENDENHALL. This corpus contains seventy-five rare works of eighteenth-century fiction drawn from the Singer-Mendenhall collection at the University of Pennsylvania. The SINGERMENDENHALL corpus is different because it was created via OCR of scanned novels; we then processed the resulting (very messy) text by removing "non-words" (any words that appear < 200 times in the Google ngram corpus) and uppercase words.

Are either of these corpora a perfect representation of the "real" archive of late-eighteenth and early-nineteenth-century fiction? Nope! But there's really no perfect representation, and there is a lot we can learn from this one.

### How to run the CS21 "more distinctive words" program [fill this in]

We will walk through the program in class so that you have a basic idea of how it implements the “most distinctive word” calculation. [Rich, can you add a brief explanation or  narrative version of the pseudocode?]

We will be running this program - written in the programming language Python - from the command line via your Terminal (on Mac) or PowerShell (on PC). The command line is simply a different tool for viewing and interacting with the files and programs on your computer. You have already completed a tutorial teaching you the basics of how to navigate your file structure and run programs from the command line.

1. Download the folder containing the corpora and program into your own computer. Save it somewhere that makes sense to you.

2. Open your Terminal or PowerShell and change directory (cd) into the "bin" folder within the assignment folder.

3. To run the program, enter the command:

> python3 sample.py

And follow the assignment's prompts to compare two texts or corpora.

You will see a few outputs. First, there will be a list of most frequent words in each corpus with a number alongside telling you how many times that word occurs. These can be potentially interesting, but will not be our primary focus. Next comes the two list of "most distinctive" word in each corpus; each word is accompanied by a number that tells you how many times the word word appears in Corpus A than in Corpus B.

You will then also be able to select any word from that list and ask the program to display all instances of it in the context of the surrounding words from the text, which will give you a sense of the word's uses. (This is called Keyword in Context, or KWiC.)

### Questions and Interpretation

1. Once you have the program running, try these comparisons first: The AUSTEN corpus to BRUNTON, CHAWTON, and CANON corpora.

You will see at least one fairly striking result in this comparison.


2. Next, map out come comparisons - between Austen's novels and other groups of novels, and between individual Austen novels and other individual novels - that you would like to make in order to answer some of the questions below.




Note: We cannot answer the question of whether Austen is different from her contemporaries, because we have built difference into our output: our friends in CS21 have constructed a program that will find difference no matter what. But given difference, we can use the lists o

So what “more distinctive” metrics *can’t* do is prove that Austen is generally divergent or distinctive from her contemporaries

### Write

After




### Extra credit for non-CS people

Open the script in Atom or a similar code-editing tool and modify the script to do one of the following:

Display 20 words instead of 10 and re-run the script.

The number of words that must appear in both corpora for the word to appear at all in the results output is currently 5; set that number to a different number and re-run the script.

### Extra credit for anyone

In his book Nabokov’s Favorite Word is Mauve, data journalist Ben Blatt notes that Jane Austen’s “use of words like "very" is off the charts,” and gives an example:

[add image]

Based on only what you see here, what is potentially wrong with Blatt’s example? Might what is wrong with this example be a symptom of what else might go wrong with the computational text analysis of literature when a literary critic is not involved?

### Extra credit for anyone

Here are two studies that use “most distinctive” words
The first, “   “ by Matt Jockers and     ,  parses a corpus of about 3,000 nineteenth-century novels into pronoun-verb pairs. Using pronoun gender as the variable, Jockers and X try to discover whether there are patterns to the relation between pronoun gender and verb. Another study, inspired by

For this extra credit assignment you have two options. The first is briefer and more purely critical

The second ask you to turn to

-add a “reinterpret” assignment for https://juliasilge.com/blog/gender-pronouns/ - need to think about narrated vs reported speech, FID, non-FID, and first person (ie, Jane Eyre). Think about how KWiC might help check some of this. Think about what other data you might want to better get at this question about gender. Think about the role of gender in text analysis. Read also the Jockers-


Citations and related work

Eric Simpson, Jane Austen and contemporary prose style
https://pagesandlights.wordpress.com/2013/01/23/jane-austen-and-contemporary-prose-style/

Eric Simpson, More on Jane Austen and stylistic signatures
https://pagesandlights.wordpress.com/2013/01/25/more-on-jane-austen-and-stylistic-signatures/

Ted Underwood, Identifying diction that characterizes an author or genre: why Dunning’s may not be the best method.
https://tedunderwood.com/2011/11/09/identifying-the-terms-that-characterize-an-author-or-genre-why-dunnings-may-not-be-the-best-method/

Ben Schmidt,

See also:
http://sappingattention.blogspot.com/2011/11/compare-and-contrast.html
http://sappingattention.blogspot.com/2011/10/dunning-statistics-on-authors.html

Stephen Ramsay

Austen

Sarah Allison

Richard

Other thanks from Twittr


APPENDIX 3: programming tasks at the core of CS21 assignment

For the texts and groups of texts like those listed below, students will extract and write to a file:

1. Lists of "most common" words in the given texts and corpora

2. Lists of "most standout” words in given pairs of texts and corpora

Note: "More standout" or “more distinctive” words are created by taking a count of how often each word in two compared texts (or groups of texts) occurred relative to the number of words in each text. (For example, for the word 'everything' in  novels by Jane Austen vs. novels by Mary Brunton, 'everything' occurred 2 out of 394,890 times in Brunton but 281 out of 881,546 in Austen. The ratio (2/394890) / (281/881546) was bigger than any other ratio for any word that occurs in Austen and Brunton.)

3. Keyword in Context (kwic) lists for selected interesting "more likely" words
