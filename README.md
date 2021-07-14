# The never-ending threat in Amazon rainforest

Brief analysis of Amazon Fires reported from 1998 to 2017.

The data is a compilation of datasets from official government reports and posted on Kaggle by Luís Gustavo Modelli.

More info here : [Kaggle Dataset](https://www.kaggle.com/gustavomodelli/forest-fires-in-brazil)

Official source : [Brazil Gov Website](http://dados.gov.br/dataset/sistema-nacional-de-informacoes-florestais-snif)

![amazonfires](img/amazonfires.jpg)

## Introduction

Well, this is not a topic that I'm glad to work with but it is one that **WE** must talk about. I know it is not a funny joke but Fires spreading in Amazon is a "hot" topic every single year and governments from the biggest economies in the world discuss (somehow) methods to deal with it. Brazil authorities have been constantly showing that they can't handle this properly and data presents us with some evidence. I hope that more and more works like this one that consistently show the devastation of Amazon rainforest calls for more public attention, nature will not prevail as long as we just wait for someone (or something...) do what must be done.

Let's dive into it. Thanks for being here.

## Assumptions

We have a dataset that contains the **number of fires reported in Brazil**.Including information by each State, year and month.
While I was looking the data I felt the need to exclude the first two years of measurement because those numbers were relatively too low compared with other years, which suggest the process of collecting the data was not that robust at the time. **So I filtered my dataset to get data from year 2000 or after that**.

## Tools

Language:   Python, always Python.

IDE:        VS Code

## Tables

In every analysis we use techniques and programming to create well-suited tables to help us understand our data quickly. That's the point right now.

I'm gonna show what tables / dataframes I made and the `code` right next to it to help you do the same if necessary.

The whole point is to present some condensed information to shed some light about the data and what are the next steps we should take.


