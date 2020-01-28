Word Slicer
==========

Cut your unspaced (or 'too spaced') long texts.



Usage
-----
```python
import wordslicer

model = wordslicer.train('train_file')
text = open('input_file', 'r').read()
text = wordslicer.separate(model, text) # or wordslicer.join(model, text)
save('output_file', text)
```

Performance
-----------

For an input of:
* 161029 words to train
* 1000 lines to separate

The results:
* Text with 36889 words
* Time: real    0m1,368s


Example:
```
>>> wordslicer.separate(model, "Boromirhesitatedforasecond.'Yes,andno,'heansweredslowly.'Yes:Ifoundhimsomewayupthehill,andIspoketohim.IurgedhimtocometoMinasTirithandnottogoeast.Igrewangryandheleftme.Hevanished.Ihaveneverseensuchathinghappenbefore.thoughIhaveheardofitintales.HemusthaveputtheRingon.Icouldnotfindhimagain.Ithoughthewouldreturntoyou.'")

Boromir hesitated for a second. 'Yes, and no,' he answered slowly. 'Yes: I found him some way up the hill, and I spoke to him. I urged him to come to Minas Tirith and not to go east. I grew angry and he left me. He vanished. I have never seen such a thing happen before. though I have heard of it in tales. He must have put the Ring on. I could not find him again. I though the would return to you.'
```


How to Install
--------------

```
pip3 install wordslicer
```

Features
----------------------

* Train your model: with the training ability, this package works with every language.

* Evaluate your model: check if your training text is good enough for your input text:

![image](https://i.imgur.com/bnEqlEP.png)


Credits
----------------------
This project was inspired by Generic Human on http://stackoverflow.com/a/11642687/2449774 . 
Thank you!