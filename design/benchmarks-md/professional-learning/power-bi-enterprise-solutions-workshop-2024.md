---
source: "design/benchmarks-pdf/professional-learning/power-bi-enterprise-solutions-workshop-2024.pdf"
source_sha256: 5d936194154a3c8774fd7df35e28c7a427fb9d4348130b86ae9c6ec58946548f
family: professional-learning
pages: 101
min_text_coverage: 0.962
pages_without_graphics: [10, 13, 14, 17, 21, 56, 84, 88, 95, 96, 97]
converter: "pymupdf4llm 0.0.27 + pymupdf 1.26.5 (por página, respaldo sin gráficos; limpieza v1)"
converted: 2026-10-05
warnings:
  - "páginas con poco texto: [1, 2, 3, 6, 7, 8, 24, 26, 28, 29, 37, 38, 44, 49, 57, 58, 66, 69, 78, 79, 80, 84, 85, 86, 87, 88, 95, 98]"
---
# Power BI for Enterprise

**Paul Turley**
**Director, Principal Consultant,**
# Solutions Workshop

**3Cloud Solutions**

**paul@IntelligentBiz.net**
Level: Intermediate


January 25, 2024

> ⚠️ S01: página 1 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 1 -->

## **THANK YOU**



Platinum


Gold


Silver


Bronze

> ⚠️ S01: página 2 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 2 -->

### **Evaluations, evaluations…**

https://evals.datagrillen.com/evals_vienna.aspx

> ⚠️ S01: página 3 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 3 -->

**Paul Turley**


**My Values:**


               **Family**

               **Community, Mentorship**

               **Colleagues, Clients, Career**


**Principal Consultant, Microsoft Data Platform MVP**


**~25 years in IT, data platform, Business Intelligence & data analytics**


TV news

Healthcare software


Helpdesk



**Conferences & Presentations:**

**PASS Summit**

**SQL Saturdays**

**User Groups**

**MBAS, Business Analytics Summit,**

**Live!360**

**SqlServerBi.Blog – ~2 million viewers**



IT Training & Consulting


Data Reporting & BI


2003 2009 2022


14 books



IT Training


BI Analytics



Injury = Desk job


1986 1989

<!-- fin de página 4 -->

SOME BACKGROUND

ABOUT THIS WORKSHOP


This presentation developed as a full-day preconference


Expanded to optional 2-day training


Scaled-down a version to 3-4 hours


Way too many slides! - Not going to present all of them


Not going to complete every exercise


OK to skip ahead and use completed solution files


6

<!-- fin de página 5 -->

Personal BI


Team BI


Enterprise BI


**Power BI Premium**


**Microsoft Fabric**




Futureproof


Scalable


Extensible


Governance


Team Development


Versioning


Deployment Process

> ⚠️ S01: página 6 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 6 -->

The Business Intelligence Process



Plan Get Data Transform Model Calculate Visualize Publish Manage





8

> ⚠️ S01: página 7 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 7 -->

Objectives: Apply enterprise-scale recipes & patterns


9 © 2021, 3Cloud, LLC., All Rights Reserved.

> ⚠️ S01: página 8 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 8 -->

Futureproof Solutions


Extensible Design


11

<!-- fin de página 9 -->

#### _Difficult to_ _see; always_ _in motion,_ _the future_ _is._

[Doing Power BI the Right Way: 1. Futureproofing Power BI solutions | Paul Turley's SQL Server BI Blog](https://sqlserverbi.blog/2020/07/29/doing-power-bi-the-right-way-1-futureproofing-power-bi-solutions/)
https://sqlserverbi.blog/2020/07/29/doing-power-bi-the-right-way-1-futureproofing-power-bi-solutions/

<!-- fin de página 10 -->

Extensible Design

GOING TO EXTREMES AND FINDING BALANCE


One model per Report One model with all the

answers



Flexibility


Redundancy & inconsistency



Central Control


Complexity & inflexibility



13

<!-- fin de página 11 -->

Scalability


14



More Data


More Users


Workload


Ease of Design

<!-- fin de página 12 -->

Self-Service BI Mindset


We Have Some Data We Need a Report



What color

should it be?



How to navigate

between pages



This data looks


OK. Let’s

import it.



What visuals


should be


used?



How can users

export the
report data?



Can we design
the report to look

like the old one?



16

<!-- fin de página 13 -->

Enterprise BI Mindset


Data Sources Data Shaping & Storage Report Design



How are records

identified & how are


tables related?


How should data

be shaped &

modeled for

reporting?



What business

questions are

being
answered?


Visualization


choices


Standard report
branding, theme

colors & layout



Are calculations

accurate & used

correctly?


Report page

navigation



Who owns &
manages this

source data?


Which of the

three sources


for a table is


correct?



How/who decides

how data should be


accessed &


secured?



How should

data quality

issues be

resolved?



How often should

records be loaded


& refreshed?


Do we need to
track changes &

history?



Are there standard


definitions for

calculations across

the organization?



17

<!-- fin de página 14 -->

How Much Data?

CAN WE MANAGE WITH POWER BI…


Data models typically require a fraction of the source data storage size
(due to column selection & compression)

Import models run in-memory & are typically very fast.

DirectQuery enables access to large tables with a performance cost, OK with little grouping and
when only light calculations are needed.

Advanced features enable optimizations over DirectQuery, like aggregations & composite
models.



Thousands/

Millions of rows


10x Millions of rows


Billions of rows





~250 MB


1 GB



Ideal working set for desktop development


File size upload limit / Pro license dataset limit



400 GB



DirectQuery (no limit)


Direct Lake (even better - maybe)

<!-- fin de página 15 -->

Team Development
Versioning & File Management


19

<!-- fin de página 16 -->

###### Manage Power BI Desktop Files




**Store files in a centrally managed network-**
**assessable folder**

The storage folder should support
automatic backup and recovery in the case
of storage loss.

**Report and dataset developers must open files**
**from the Windows file system**
Files must either reside in or be

synchronized with the Windows file

system.

Files containing imported data typically

range in size from 100 to 600 MB. Any
shared folder synchronization or disaster
recovery system should be designed to
effectively handle multiple files.



**Options:**

OneDrive For Business (shared by team,

with folder synchronization).

SharePoint or SharePoint Online (with

folder synchronization).

GitHub and/or VSTS with local repository

& folder synchronization. If used, Git must
be configured for large file storage (LFS) if
PBIX files are to be stored in the

repository.

NEW – Power BI Project with Git

integration.

Reduce file size to under 100

MB. We’ll talk about this a bit

later.

<!-- fin de página 17 -->

Clearing DevOps, Versioning & Team Development Blockers


 - Power BI file size


Keep PBIX files under 100 MB, as a guideline


 - Separate data model PBIX from Report PBIX when:


   Project has matured


   Parallel data model & report development is feasible


  - Treat PBIX file as a binary file


   Don’t compare, split or merge with app dev schema compare tools


   More DevOps & object-level integration is coming. Be patient


   Option: manage data model as .BIM (but realize the trade-offs).


  - Store BI project files in simple code repository


   OneDrive for Business


   Git / Azure DevOps


22

<!-- fin de página 18 -->

Data Governance


how it relates to Power BI solutions


23

<!-- fin de página 19 -->

Dataset, Model and App Deployment & Delivery Cycle
REPORT DELIVERY EN MASS


Certified Reports on Certified Datasets


Datasets

|Col1|Prod|Col3|
|---|---|---|
|Test|||
|Test|||



Dev workspaces Deployment pipelines



Reports



|Col1|Prod|Col3|
|---|---|---|
|Test|||
|Test|||


Workspaces are promoted

through Deployment Pipelines

after test acceptance



Developers deploy datasets

and reports to workspaces


26



Workspace App Business Users


Report workspace delivered as an App

<!-- fin de página 20 -->

Certified & Self-Service Decision Tree

REPORTING & ANALYTICS PATHS


Reports & Datasets


View report in

workspace or

App

Y



Is there


an

existing
Report?


N



Y


Is there


an

Existing

Dataset?


N



Create new

“self-service”


model &


report


Request IT

add or extend


dataset



Certified


report
/dataset


Certified


dataset


Semi
trusted

dataset



Create report

connected to


certified


dataset


Y


Need to

import new

“self

service”


data?


N



Semi
trusted


report


Semi
trusted


report


Certified


dataset



“I need to


analyze
some data”



iterate into

certified

dataset



27

<!-- fin de página 21 -->

Power BI Adoption


Power BI adoption should blend with the
organizational data governance strategy

Data culture

Sponsorship

Content ownership (Data Stewardship)

Content delivery (Certification, self-service)

Community of Practice / training & knowledge
sharing

Security & system oversight


[https://docs.microsoft.com/en-us/power-bi/guidance/powerbi-adoption-roadmap-overview](https://docs.microsoft.com/en-us/power-bi/guidance/powerbi-adoption-roadmap-overview)


28

<!-- fin de página 22 -->

Hands On Exercises


Part 1 Part 2 Part 3 Part 4


Lab Exercise Solution Files:




Create advanced measures

Visualize

Deploy to cloud service

Deliver to user audience




Prepare source data

Connect to data sources

- Create parameters

Filter records




Transform data

Import tables

Create data model

Create base measures

<!-- fin de página 23 -->

Setup


30

> ⚠️ S01: página 24 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 24 -->

Lab Project Files & Folders


Using Windows File Explorer, copy the folder **Power BI Enterprise Solutions Workshop** from the

USB drive to the C: drive on your computer.


Follow instructions to:


 Work in the
**Working Project Files** folder


 Copy solution files from the
**Solution Project Files** folder


You will create this file


31

<!-- fin de página 25 -->

Power BI Desktop Options


32

> ⚠️ S01: página 26 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 26 -->

Hands On Exercise
Part 1:
Connect & Transform Data


Part 1 Part 2 Part 3 Part 4




Create advanced measures

Visualize

Deploy to cloud service

Deliver to user audience




Prepare source data

Connect to data sources

- Create parameters

Filter records




Transform data

Import tables

Create data model

Create base measures

<!-- fin de página 27 -->

Iteration 1


Fact tables &

related dimensions:


Online Sales


Store Sales


35 © 2021, 3Cloud, LLC., All Rights Reserved.

> ⚠️ S01: página 28 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 28 -->

Iteration 1 Requirements
FUNCTIONAL REQUIREMENTS


The Sales organization needs…

Online Sales Qty

Online Sales Amt

Store Sales Qty

Store Sales Amt

Executive Leadership needs…


36

> ⚠️ S01: página 29 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 29 -->

Iteration 1 Requirements
REPORT CAPABILITIES & WIREFRAME


Functional Report Requirements


“Back of the napkin report design”


Business questions:


What is the Sales Amount grouped by Year or Month
or Day, for a specific period of time.

- Trend chart should allow a user to select a time series

metric (like Month Over Month, Month Over Month %
Change, Month To Date, Prior Month, Year To Date) &
then show them along the axis of Years, Months or

Days.

All of the data on the report can be filtered by store
regions, such as State, City or an individual Store.


37

<!-- fin de página 30 -->

Iteration 1 Requirements
DIMENSIONAL MATRIX

|Col1|Date|Account|Customer|Product|Store|
|---|---|---|---|---|---|
|**Online Sales**|X||X|X||
|Online Sales Qty||||||
|Online Sales Amt||||||
|**Store Sales**|X|||X|X|
|Store Sales Qty||||||
|Store Sales Amt||||||



38

<!-- fin de página 31 -->

Data Modeling Essentials & Best Practices in Power BI


Flat Model
Master/Detail Dimensional


[Doing Power BI the Right Way: 5. Data Modeling Essentials & Best Practices (1 of 2) | Paul Turley's SQL Server BI Blog](https://sqlserverbi.blog/2020/12/25/doing-power-bi-the-right-way-6-data-modeling-essentials-best-practices-1-of-2/)
https://sqlserverbi.blog/2020/12/25/doing-power-bi-the-right-way-6-data-modeling-essentials-best-practices-1-of-2/

<!-- fin de página 32 -->

Transformation Options
TO PREPARE & SHAPE DATA FOR MODELING



**Power Query**

Design in Desktop


Execute in service

Small-moderate data volume


Self-service data mashup



**Dataflows**

Design in browser

Execute in service

In-place of data warehouse



In-place of data warehouse **ETL/ELT & Views**

Reusable queries



Execute in database



Integrated in data

warehouse

Enterprise-scale

<!-- fin de página 33 -->

Preparing, shaping & transforming source data
using Power Query



Consolidate &

optimize steps



Create

parameters



Set date range

filter on fact


tables



Rename

columns



Apply
transformations





Rename &


annotate


steps



Use objects that


support query

folding



Remove all


unneeded


columns



Change all
column data


types



[Doing Power BI the Right Way: 2. Preparing, shaping & transforming source data | Paul Turley's SQL Server BI Blog](https://sqlserverbi.blog/2020/08/16/doing-power-bi-the-right-way-2-preparing-source-data/)
https://sqlserverbi.blog/2020/08/16/doing-power-bi-the-right-way-2-preparing-source-data/

<!-- fin de página 34 -->

Object Naming Conventions






|Database Developer<br>•<br>Table, field/column names<br>Bal<br>•<br>Measure names<br>•<br>All objects expose<br>•<br>Code-friendly names<br>friendly names<br>•<br>Cryptic object names:<br>•<br>Hide key columns<br>Pascal case, Camel case, Hungarian<br>•<br>Hide numeric colu<br>notation,<br>named measures|Col2|Col3|BI Solution Designer<br>•<br>Descriptive names<br>nce<br>•<br>Sentence case<br>to users should have<br>•<br>Non-standardized<br>utility objects<br>ns & create friendly|Col5|
|---|---|---|---|---|
|**Database Developer**<br>•<br>Table, field/column names<br>•<br>Measure names<br>•<br>Code-friendly names<br>•<br>Cryptic object names:<br>Pascal case, Camel case, Hungarian<br>notation,<br>**Bal**<br>•<br>All objects expose<br>friendly names<br>•<br>Hide key columns<br>•<br>Hide numeric colu<br>named measures|n names<br>mes<br>mes:<br>el case, Hungarian<br>**Bal**<br>•<br>All objects expose<br>friendly names<br>•<br>Hide key columns<br>•<br>Hide numeric colu<br>named measures|n names<br>mes<br>mes:<br>el case, Hungarian<br>**Bal**<br>•<br>All objects expose<br>friendly names<br>•<br>Hide key columns<br>•<br>Hide numeric colu<br>named measures|•<br>Descriptive names<br>•<br>Sentence case<br>•<br>Non-standardized<br>**nce**<br>to users should have<br> utility objects<br>ns & create friendly|•<br>Descriptive names<br>•<br>Sentence case<br>•<br>Non-standardized<br>**nce**<br>to users should have<br> utility objects<br>ns & create friendly|
||||||

<!-- fin de página 35 -->

Optimize Power Query


   Test transformations with


large data volumes

   Pivot, unpivot & Transpose

actions are costly & may not
work effectively with large
data volume

   Complex and “creative”

transformations might work in
Desktop or with small data
volumes but not in production

   Web service API calls & nested


M functions may not work in
the service.


43



This query, with redundant,
dependent steps; takes three
times longer to load records

<!-- fin de página 36 -->

Using Parameters
Importing Dimensions
Importing Facts


44 © 2021, 3Cloud, LLC., All Rights Reserved.

> ⚠️ S01: página 37 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 37 -->

Add Query Parameters


45

> ⚠️ S01: página 38 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 38 -->

Importing Dimension Data


- Dim Customer

- Dim Product

- Dim Store

- Dim Date


- Parameterize connection information


Import from tables or views, not using in-line SQL statements


- Remove unneeded columns


Rename columns to apply friendly names


46

<!-- fin de página 39 -->

Power Query Optimization


Power Query steps generate M code


Formatted code can be easier to
read and debug


Generate steps to establish code
pattern & then enhance code


Code comments create tooltips in the
designer


47

<!-- fin de página 40 -->

Importing Fact Tables


Tables contain tens of millions of rows


Use date range parameters to reduce local working
set and keep PBIX file small.


PartitionDateTime:


  Row count reduction


  Incremental Refresh


UpdateDate:


  Detect changes


No need to rename fact table columns


48

<!-- fin de página 41 -->

Where to Perform Calculations


**Store Sales Amt**


**If calculated at the row-level** :


1. Perform calculation in the upstream ETL
process & store value


2. Calculate at the source, in a view


3. Custom field in Power Query


4. Calculated column in DAX


**Store Sales Amt = SalesQuantity * UnitPrice**
(on a single row)


49



**If calculated outside of a single row context,**
**or if the calculation on a single row is**

:
**affected by filter context**


Perform calculation in DAX as a measure

<!-- fin de página 42 -->

Date Dimension


Generating a Date dimension table

options:

ETL pipeline

SQL script in the source database

Power Query/M

Calculated table using DAX


50



Convert date values to numbers

```
 // Convert dates to numbers

StartNum  =  Number.From( DimDateStart ),

EndNum   =  Number.From( DimDateEnd )

```

Create a range of numbers using the variable values

```
 // Generate number range

 NumRange  =  { StartNum..EndNum }

```

<!-- fin de página 43 -->

Adding Date Part Columns to the Dim Date Table


51




Quarter > Quarter of Year

- Month > Month

- Month > Name of Month

- Week > Week of Year

- Week > Week of Month

Day > Day

Day > Name of Day

> ⚠️ S01: página 44 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 44 -->

Fact Table Transformations

GENERAL GUIDANCE


- Remove all unnecessary columns

- Ideally only contains keys and

numeric measure base columns

- Utility columns for partitioning &

change tracking

- Table will be hidden in the data


model

- No need to rename columns with

friendly names


52




**Fact Online Sales**

**Fact Store Sales**

<!-- fin de página 45 -->

Fact Table Transformations

MANAGING DATA VOLUME


Add Partition key date/time type
column

Set date range filter to use
**RangeStart** & **RangeEnd**
parameters


53



The FactOnlineSales table contains about 21

million rows.


Load only data needed for development into
the local copy of the model.

<!-- fin de página 46 -->

You Gotta Know When to Fold ‘Em

UNDERSTANDING QUERY FOLDING


Query folding produces a query, in the native
language of the data source.


Many query steps can be folded


Some steps cannot


Perform the most critical steps first:


  Filtering


  Grouping


  Remove columns


  Change data type


1. Try to get entire query to fold


2. Perform less impactful steps later, if folding is broken


54

<!-- fin de página 47 -->

Create a Measure Container Table

A PLACE TO PUT MY MEASURES


Create a single measure
group/container table for all

measures


Fact tables in the data model will

be hidden


Some measures are based on
values from multiple fact tables


55

<!-- fin de página 48 -->

Iteration 2


Introduce new fact tables

& related dimensions:


- Scenario Plan


- Exchange Rate


56

> ⚠️ S01: página 49 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 49 -->

Iteration 2 Requirements
CHANGE REQUEST


Our business stakeholder has requested that an addition be made to the current project due to business conditions
that have changed since the beginning of the project. Our **Project Manager** has met with the **CFO** and the **CIO**,
suggesting that the current work be completed and delivered before making additions. However, the additional
request is deemed to be a critical need, and the business have asked that the project scope be expanded to include
these additional tables and report functionality. **A change request has been written and approved** to include these
new requirements and the **project budget and schedule have been adjusted** to reflect this new request.


Financial Planners need:

Sales Quota table with Actual Sales & Budget

Sales Organization needs:

Exchange Rates

Currency Rates change during the day and reports with currency converted measures
must include **real-time** updates as the source data changes


57

<!-- fin de página 50 -->

Iteration 2 Requirements
REPORT CAPABILITIES & WIREFRAME


 - The bottom visual should be

enhanced to include **Actual**

**Sales Amount** and **Budget Sales**

**Amount** from the Sales Quota

system


 - Calculated difference between

Actual Sales and Budget


58

<!-- fin de página 51 -->

Iteration 2 Requirements
REPORT CAPABILITIES & WIREFRAME


 A second report page will show

**Combined Sales Amount** values in

US dollars alongside the sales value
converted to any selected foreign

currency.


 Currency conversion is based on the
**most current** exchange rate, using

real-time source data.


59

<!-- fin de página 52 -->

Iteration 2 Requirements

|Customer<br>Product<br>Store<br>Date<br>Online Sales X X X<br>Online Sales Amt<br>Online Sales Qty<br>Store Sales X X X<br>Store Sales Qty<br>Store Sales Amt|Col2|Col3|Col4|Col5|Col6|Scenario Currency|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Date**<br>**Customer**<br>**Product**<br>**Store**<br>**Online Sales**<br>X<br>X<br>X<br>Online Sales Amt<br>Online Sales Qty<br>**Store Sales**<br>X<br>X<br>X<br>Store Sales Qty<br>Store Sales Amt||**Date**|**Customer**|**Product**|**Store**||**Scenario**|**Currency**|
|**Date**<br>**Customer**<br>**Product**<br>**Store**<br>**Online Sales**<br>X<br>X<br>X<br>Online Sales Amt<br>Online Sales Qty<br>**Store Sales**<br>X<br>X<br>X<br>Store Sales Qty<br>Store Sales Amt|**Online Sales**|X|X|X|||||
|**Date**<br>**Customer**<br>**Product**<br>**Store**<br>**Online Sales**<br>X<br>X<br>X<br>Online Sales Amt<br>Online Sales Qty<br>**Store Sales**<br>X<br>X<br>X<br>Store Sales Qty<br>Store Sales Amt|Online Sales Amt||||||||
|**Date**<br>**Customer**<br>**Product**<br>**Store**<br>**Online Sales**<br>X<br>X<br>X<br>Online Sales Amt<br>Online Sales Qty<br>**Store Sales**<br>X<br>X<br>X<br>Store Sales Qty<br>Store Sales Amt|Online Sales Qty||||||||
|**Date**<br>**Customer**<br>**Product**<br>**Store**<br>**Online Sales**<br>X<br>X<br>X<br>Online Sales Amt<br>Online Sales Qty<br>**Store Sales**<br>X<br>X<br>X<br>Store Sales Qty<br>Store Sales Amt|**Store Sales**|X||X|X||||
|**Date**<br>**Customer**<br>**Product**<br>**Store**<br>**Online Sales**<br>X<br>X<br>X<br>Online Sales Amt<br>Online Sales Qty<br>**Store Sales**<br>X<br>X<br>X<br>Store Sales Qty<br>Store Sales Amt|Store Sales Qty||||||||
|**Date**<br>**Customer**<br>**Product**<br>**Store**<br>**Online Sales**<br>X<br>X<br>X<br>Online Sales Amt<br>Online Sales Qty<br>**Store Sales**<br>X<br>X<br>X<br>Store Sales Qty<br>Store Sales Amt|Store Sales Amt||||||||
|**Sales Quota**<br>X<br>X<br>Quota Qty<br>Quota Amt<br>**Exchange Rate**<br>X<br>End of Day Rate|||||||||
|**Sales Quota**<br>X<br>X<br>Quota Qty<br>Quota Amt<br>**Exchange Rate**<br>X<br>End of Day Rate|**Sales Quota**|X||X|||X||
|**Sales Quota**<br>X<br>X<br>Quota Qty<br>Quota Amt<br>**Exchange Rate**<br>X<br>End of Day Rate|Quota Qty||||||||
|**Sales Quota**<br>X<br>X<br>Quota Qty<br>Quota Amt<br>**Exchange Rate**<br>X<br>End of Day Rate|Quota Amt||||||||
|**Sales Quota**<br>X<br>X<br>Quota Qty<br>Quota Amt<br>**Exchange Rate**<br>X<br>End of Day Rate|**Exchange Rate**|X|||||||
|**Sales Quota**<br>X<br>X<br>Quota Qty<br>Quota Amt<br>**Exchange Rate**<br>X<br>End of Day Rate|End of Day Rate|||||||X|



60 © 2021, 3Cloud, LLC., All Rights Reserved.

<!-- fin de página 53 -->

New Fact Table Queries


Fact Sales Quota


  Simple query, import from **vwFactSalesQuota**


  Apply the same pattern as previous fact table queries except no
UpdateDate column


Fact Exchange Rate


  Based on **vwFactExchangeRate** view


  Connect using **DirectQuery**


61

<!-- fin de página 54 -->

Hands On Exercise
Part 2:
Data Modeling for Scale


Part 1 Part 2 Part 3 Part 4




Create advanced measures

Visualize

Deploy to cloud service

Deliver to user audience




Prepare source data

Connect to data sources

- Create parameters

Filter records




Transform data

Import tables

Create data model

Create base measures

<!-- fin de página 55 -->

Model Design


**Database Developer**



**BI Solution Designer**




- Flattened results Import details

**Balance**


- Transform in SQL or ETL tool Transform in Power Query

            Build dimensional star schema

Wide tables


            Avoid wide tables

Pre-aggregated results

            Remove long text fields

Import summary data

            Remove unused fields

            Tall tables are OK if they are optimized
for storage & analytics

<!-- fin de página 56 -->

Model Design


64

> ⚠️ S01: página 57 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 57 -->

Date Dimension


Mark table as Date table, select Date type key
column


Create date part hierarchies to support report
drill-down navigation


65

> ⚠️ S01: página 58 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 58 -->

Build the Data Model


Create relationships


Arrange tables


Create multiple layouts for large models


Proper query and transformation design
simplifies data model design


Adding DirectQuery tables to an import
model creates a “composite model”


DirectQuery tables are displayed with
different colored headings


A composite model contains “soft”
relationships


66

<!-- fin de página 59 -->

Build the Data Model


True dimensional design makes relationship mapping simple


Avoid bi-directional relationships, but use them when necessary
(typically for many-to-many)


Manage user expectations with dimension>dimension cross
filtering


High cardinality dimensions affect performance at scale


Consistent key naming simplifies model and helps avoid
mistakes


Some exceptions are OK
(for example: DateKey > Date)


Be careful with relationship Autodetect
(which is on by default)


Relationship MUST be on the same data type. watch for:


  - Date <> DateTime


  - WholeNumber <> Decimal


67

<!-- fin de página 60 -->

Quick… Hide the Facts

HIDE ALL FACT TABLES


Implicit & Explicit Measures


  Ideally, expose only measures and hide all summable numeric columns


  Some client tools don’t support implicit measures (like Excel)


  Explicit measures, although a little more work, provide more control and flexibility

Hide key & utility fields

Hiding a table effectively hides the individual columns


68

<!-- fin de página 61 -->

Hierarchies

SUPPORT DRILL-DOWN NAVIGATION


Product hierarchy

Date hierarchies

Create multiple hierarchies for
different reporting needs

Parent-child hierarchies
(chart of accounts or employee
org chart) are more complicated.


69

<!-- fin de página 62 -->

Table Partitioning & Incremental Refresh


70

<!-- fin de página 63 -->

Date Range Filtering & Incremental Refresh
SOLVES MULTIPLE PROBLEMS


In a data model without Incremental Refresh, data volume can
be managed in the service using RangeStart & RangeEnd
parameters

In a data model with Incremental Refresh, date range
partitioning is automatically managed in the service & the
parameters are removed from view

Using the RangeStart & RangeEnd parameter filtering approach
provide a consistent best practice design pattern


71

<!-- fin de página 64 -->

Configure Incremental Refresh
FOR EACH FACT TABLE


Archive periods:
Generates one static partition per specified period

Incremental refresh periods:
Generates one partition per specified period

Detect data changes:
Reprocesses any partition with a date newer than
the last refresh date.

Get the latest data in real time with DirectQuery:
Create a hybrid model with a DirectQuery partition
newly inserted records


72

<!-- fin de página 65 -->

Incremental Refresh & Partition
Demonstration


FOR EACH FACT TABLE


First data refresh process takes time to
create all partitions


73

> ⚠️ S01: página 66 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 66 -->

Hands On Exercise
Part 3:
Measure Development in the Enterprise


Part 1 Part 2 Part 3 Part 4




Create advanced measures

Visualize

Deploy to cloud service

Deliver to user audience




Prepare source data

Connect to data sources

- Create parameters

Filter records




Transform data

Import tables

Create data model

Create base measures

<!-- fin de página 67 -->

Row Count & Validation Measures


Table row counts are a convenient initial data

validation test


Ensures data is loaded as expected


Use Tabular Editor to duplicate existing
measures & add to display folders

```
 Row Count Fact Online Sales =

 COUNTROWS( 'Fact Online Sales' )

```

75



Tabular Editor:

<!-- fin de página 68 -->

Enhancing the Model
with Measures


76

> ⚠️ S01: página 69 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 69 -->

Base Measures


Replace “implicit measures” / numeric fact
table columns


Basis for additional measures


77




|Measure Name|Expression|
|---|---|
|**Online Sales Amt**|= SUM( 'Fact Online Sales'[SalesAmount] )|
|**Online Sales Qty**|= SUM( 'Fact Online Sales'[SalesQuantity] )|
|**Store Sales Amt**|= SUM( 'Fact Store Sales'[SalesAmount] )|
|**Store Sales Qty**|= SUM( 'Fact Store Sales'[SalesQuantity] )|
|**Combined Sales Amt**|= [Online Sales Qty] + [Store Sales Qty]|
|**Quota Sales Amt**|= SUM( 'Fact Sales Quota'[TotalSalesAmountQuota] )|
|**Quota Sales Qty**|= SUM( 'Fact Sales Quota'[TotalSalesQuantityQuota] )|

<!-- fin de página 70 -->

Display Folders
TO ORGANIZE MEASURES


Display folder is a measure property
(rather than an actual “folder”)

Set Display Folder property for a measure to
“create” a folder

Use Tabular Editor to drag measures into
existing folders


Tabular Editor:


78



Power BI Desktop – Model view:

<!-- fin de página 71 -->

Calculation Groups



Reduce measure count & development effort


Implement time intelligence


Layer complex calculation logic over any
selected measure



79

<!-- fin de página 72 -->

Creating multiple measures: There has got to be a better way!
USING TABULAR EDITOR TO CREATE A CALCULATION GROUP


Enables variation logic to be added to
a selected measure


Can be used to implement calculation
enhancements like time intelligence


Many advanced & creative
possibilities




Specialized DAX functions are used to
pass the selected measure into a
calculation group expression


80




|DAX Function|Purpose|
|---|---|
|**SELECTEDMEASURE()**|Passes the currently selected measure into a<br>calculation group expression.|
|**SELECTEDMEASUREFORMATSTRING()**|Returns the format string property of the selected<br>measure.|
|**SELECTEDMEASURENAME()**|Returns the name of the selected measure.|

<!-- fin de página 73 -->

Calculation Group to Implement Time Intelligence
USE TABULAR EDITOR TO CREATE A CALCULATION GROUP


Time Intelligence calculation items:

  - Current

  - MoM

  - MoM %

  - MTD

  - PM

  - PY

  QTD

  - YoY

  - YoY %

  - YTD


Completed expressions for all items are in: **Time Intelligence Calculation Group Items.txt**


81

<!-- fin de página 74 -->

Hands On Exercise
Part 4:
Visualize & Analyze


            Prepare source data

            Connect to data sources

          - Create parameters

            Filter records



Part 1 Part 2 Part 3 Part 4




Transform data

Import tables

Create data model

Create base measures




Create advanced measures

Visualize

Deploy to cloud service

Deliver to user audience

<!-- fin de página 75 -->

Report Requirements Review
REPORT CAPABILITIES & WIREFRAME


Business questions:


- What is the **Sales Amount** grouped by **Year** or **Month** or

**Day**, for a specific period of time.

- Trend chart should allow a user to select a **time series**

**metric** (like Month Over Month, Month Over Month %
Change, Month To Date, Prior Month, Year To Date) &
then show them along the axis of Years, Months or Days.

All of the data on the report can be filtered by store
regions, such as **State**, **City** or an individual **Store** .


- The bottom visual should be enhanced to include **Actual**

**Sales Amount** and **Budget Sales Amount** from the Sales

Quota system


- C alculated difference between **Actual Sales** and **Budget**


83

<!-- fin de página 76 -->

Report Requirements Review
ITERATION 2 REPORT CAPABILITIES & WIREFRAME


 A second report page will show

**Combined Sales Amount** values in

US dollars alongside the sales value
converted to any selected foreign

currency.


 Currency conversion is based on the
**most current** exchange rate, using

real-time source data.


84

<!-- fin de página 77 -->

Visual Report Design


85

> ⚠️ S01: página 78 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 78 -->

Functional Design to Physical Design


86

> ⚠️ S01: página 79 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 79 -->

Functional Design to Physical Design
ITERATION 2 REQUIREMENTS


This page is provided in the Part 5 solution


87

> ⚠️ S01: página 80 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 80 -->

Hands On Exercise
Part 5:
Deploy, Test & Deliver


Part 1 Part 2 Part 3 Part 4




Create advanced measures

Visualize

Deploy to cloud service

Deliver to user audience




Prepare source data

Connect to data sources

- Create parameters

Filter records




Transform data

Import tables

Create data model

Create base measures

<!-- fin de página 81 -->

Managed Deployment & Delivery


89

<!-- fin de página 82 -->

Continuous Integration & Continuous Delivery (CI/CD)
for Power BI



A quickly-evolving discipline:

Manual techniques

Report & dataset separation

Deployment pipeline

Decompose PBIX file objects
with Tabular Editor

Next-generation:

Desktop capability

Azure DevOps integration


90



DEV TEST PROD

<!-- fin de página 83 -->

Using a Deployment Pipeline to Manage Deployment Stages



Deploy here


Promote to Test


Promote to Release &
Convert workspace to App



Deployment
pipeline contains 3

workspaces:
DEV, TEST & Prod



91

> ⚠️ S01: página 84 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 84 -->

Using a Deployment Pipeline to Manage Deployment Stages


DEV TEST PROD


92

> ⚠️ S01: página 85 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 85 -->

Dataset Settings
APPLIES TO DEPLOYED DATASET


93

> ⚠️ S01: página 86 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 86 -->

Deployment Rules
APPLIES TO EACH VERSION OF A DATASET IN THE WORKSPACE


94

> ⚠️ S01: página 87 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 87 -->

Pipeline Comparison
COMPARES VERSIONS OF EACH OBJECT IN PIPELINE


DEV & TEST versions

are the same


95



TEST & PROD versions are

Different PROD is older.

> ⚠️ S01: página 88 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 88 -->

Automate Deployment Pipelines Using APIs and Azure DevOps


REST methods enable automation with:


Azure DevOps actions


PowerShell


Custom code of choice






|Assign Workspace|Get Pipeline Operation|Selective Deploy|
|---|---|---|
|**Create Pipeline**|**Get Pipeline Operations**|**Unassign Workspace**|
|**Delete Pipeline**|**Get Pipelines**|**Update Pipeline**|
|**Delete Pipeline User**|**Get Pipeline Stage**<br>**Artifacts**|**Update Pipeline User**|
|**Deploy All**|**Get Pipeline Stages**||
|**Get Pipeline**|**Get Pipeline Users**||



96

<!-- fin de página 89 -->

Certified & Governed Data Models


97

<!-- fin de página 90 -->

Endorsing Certified Datasets & Reports


Part of the organization’s
governance & adoption plan


Governance policy sets
criteria for validation &

endorsement


Data steward owns source

data & validates dataset

trustworthiness


98

<!-- fin de página 91 -->

Separating Data Models & Reports


99

<!-- fin de página 92 -->

Planning for Separation – data
models & reports


The Thick and Thin
of Reports
Separate reports and data models can be:

  Versioned

  Deployed & managed separately

  Central “Certified” dataset

  Use Live Connect when
creating new reports


[Doing Power BI the Right Way: 7.](https://sqlserverbi.blog/2020/11/17/doing-power-bi-the-right-way-8-planning-for-separation-data-models-reports/)
[Planning for separation – data models and reports | Paul Turley's SQL Server BI Blog](https://sqlserverbi.blog/2020/11/17/doing-power-bi-the-right-way-8-planning-for-separation-data-models-reports/)


[5 Tips for Separating Power BI Datasets and Reports — Coates Data Strategies](https://www.coatesdatastrategies.com/blog/5-tips-for-separating-power-bi-datasets-and-reports)

<!-- fin de página 93 -->

Separating an Existing Model & Report
SPLIT PBIX FILE EXTERNAL TOOL


Split PBIX & Hot Swap Connections
developed by Steve Campbell

Installs with Business Ops – free tools
from PowerBI.tips

Removes data model & connection from
new report file

Reconnect report to published dataset


101

<!-- fin de página 94 -->

Analyzing & Tuning Data Models
CONNECTING TO LOCAL AND REMOTE DATA MODELS


Tools


Localhost

connection


XMLA
endpoint


102



Desktop data model


Published dataset

> ⚠️ S01: página 95 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 95 -->

… [Using Performance Analyzer]


103


```
// DAX Query

DEFINE

VAR __DS0FilterTable =
TREATAS({"Refrigerators"}, 'Dim Product'[Subcategory Name])

VAR __DS0Core =
SUMMARIZECOLUMNS(
ROLLUPADDISSUBTOTAL('Dim Customer'[Company Name],
"IsGrandTotalRowTotal"),
__DS0FilterTable,
"Online_Sales_Performance_Summary", '_Measures'[Online Sales
Performance Summary],
"v_Online_Sales_Performance_Summary_FormatString",
IGNORE('_Measures'[_Online Sales Performance Summary FormatString])
)

VAR __DS0PrimaryShowAll =
ADDMISSINGITEMS(
'Dim Customer'[Company Name],
__DS0Core,
ROLLUPISSUBTOTAL('Dim Customer'[Company Name],
[IsGrandTotalRowTotal]),
__DS0FilterTable
)

VAR __DS0PrimaryWindowed =
TOPN(502, __DS0PrimaryShowAll, [IsGrandTotalRowTotal], 0, 'Dim
Customer'[Company Name], 1)

EVALUATE

__DS0PrimaryWindowed

ORDER BY

[IsGrandTotalRowTotal] DESC, 'Dim Customer'[Company Name]

```

<!-- fin de página 96 -->

Performing Analysis with DAX Studio
CLEAR CACHE, QUERY PLAN & SERVER TIMINGS

```
   // DAX Query

   DEFINE

   VAR __DS0FilterTable =
   TREATAS({"Refrigerators"}, 'Dim Product'[Subcategory Name])

   VAR __DS0Core =
   SUMMARIZECOLUMNS(
   ROLLUPADDISSUBTOTAL('Dim Customer'[Company Name],
   "IsGrandTotalRowTotal"),
   __DS0FilterTable,
   "Online_Sales_Performance_Summary", '_Measures'[Online
   Sales Performance Summary],
   "v_Online_Sales_Performance_Summary_FormatString",
   IGNORE('_Measures'[_Online Sales Performance Summary
   FormatString])
   )

   VAR __DS0PrimaryShowAll =
   ADDMISSINGITEMS(
   'Dim Customer'[Company Name],
   __DS0Core,
   ROLLUPISSUBTOTAL('Dim Customer'[Company Name],
   [IsGrandTotalRowTotal]),
   __DS0FilterTable
   )

   VAR __DS0PrimaryWindowed =
   TOPN(502, __DS0PrimaryShowAll, [IsGrandTotalRowTotal], 0,
   'Dim Customer'[Company Name], 1)

   EVALUATE

   __DS0PrimaryWindowed

   ORDER BY

   [IsGrandTotalRowTotal] DESC, 'Dim Customer'[Company Name]

```

104

<!-- fin de página 97 -->

### **Evaluations, evaluations…**

https://evals.datagrillen.com/evals_vienna.aspx

> ⚠️ S01: página 98 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 98 -->

Resources

<!-- fin de página 99 -->

#### **Model Design Guidelines**


  - Dimensional design concepts haven’t changed in 20 years & are as true as ever


  - Dimensional modeling “rules” should be followed but can be relaxed for Power BI in certain

cases, such as:


—
Leaving some dimensional attributes in fact tables


—
Use natural keys rather than generating surrogate keys


  - The art of dimensional modeling ranges from simple to complex. Start with the basics.


  - Flattened “spreadsheet” models are OK for small, informal projects but have significant

limitations


  - As models grow in size & complexity, data quality challenges will surface that can be solved

by implementing proper governance controls


[The Kimball Method: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques)

[Lawrence Corr, Model Storming Agile method: https://modelstorming.com/hierarchy-map](https://modelstorming.com/hierarchy-map)

<!-- fin de página 100 -->

Enterprise Scale Options


In many ways, Power BI has now surpassed the capabilities of SQL Server
Analysis Services. Microsoft are investing in the enterprise capabilities of the
Power BI platform by enhancing Power BI Premium Capacity, adding Paginated
Report and features to support massive scale specialized use cases. Consider
the present and planned capabilities of the Power BI platform; before, choosing
another data modeling tool such as SSAS.


**Resources:**


[https://sqlserverbi.blog/2018/07/27/power-bi-for-grownups](https://sqlserverbi.blog/2018/07/27/power-bi-for-grownups)


[https://sqlserverbi.blog/2018/12/13/data-model-options-for-power-bi-solutions](https://sqlserverbi.blog/2018/12/13/data-model-options-for-power-bi-solutions)

<!-- fin de página 101 -->
