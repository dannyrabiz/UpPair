# UpPair
Easy to use  python tool to visualize intersection between paired groups. 

## Setup and Installation 
UpPair will be available on [pypi](https://pypi.org/) soon to be installed via `pip`

`pip install UpPair`

Alternatively, if you prefer anaconda 

`conda install UpPair`

## Introduction
Where [UpSet plots](https://ieeexplore.ieee.org/document/6876017/) were created to solve the problem of the over complicated Venn Diagram with multiple sets overlapping, UpPair is designed to solve the issue of sequential paired Venn Diagrams. 
![](https://github.com/dannyrabiz/UpPair/blob/main/Images/Sequential_Venn.png)

On its own a Venn diagram is satisfactory in displaying data; however, if the diagrams are related to one another and one wanted to compare them as to visualize a comparison between the groupings, they are essentially unhelpful both for visualizing absolute numbers and relative overlap ratios. UpPair plots allow you maintain all the data demonstrated in a Venn, while allowing you to orient each pairing in a way that compairing between them is simple and intuitive. The best part is that with our tool, you can create these plots with only 1 line of code and with straightforward easy to use cusomtizations.


### Example 1: Basic Plot 
- Visualize the overlap of replicate samples from the same patient sequenced separaltey
![](https://github.com/dannyrabiz/UpPair/blob/main/Images/Example1.png)

### Example 2: 
- Comparing methodologies on same sample
![](https://github.com/dannyrabiz/UpPair/blob/main/Images/Example2.png)

### Example 3: Two features stacked
![](https://github.com/dannyrabiz/UpPair/blob/main/Images/Example3.png)

### Example 4: Grouping of 3 samples. 
- Figure shows intersection of somatic mutation identified in various biopsies in the same individual
![](https://github.com/dannyrabiz/UpPair/blob/main/Images/Example4.png)

### Example 5:  
- Figure shows comparison of two methods (CTC and cfDNA) to detect somatic mutations compared with biopsy. Both methods are compared only with against biopsy (treated as gold-standard) and sensitivity and specifity is displayed. Results are compared across multiple cancer types to determine if a given method would perform better in a certain cancer type. 
![](https://github.com/dannyrabiz/UpPair/blob/main/Images/Example5.png)

### Example 6:
- Figure shows results from a single patient over the course of a few years. It displays the consistency between somatic mutations dected from cfDNA and CTC collections. It also shows their relationship with two biomarkers over the course of various treatments. 
![](https://github.com/dannyrabiz/UpPair/blob/main/Images/Example6_new.png)
