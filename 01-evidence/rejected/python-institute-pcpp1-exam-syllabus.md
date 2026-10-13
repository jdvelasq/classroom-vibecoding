---
source: "01-evidence/rejected/python-institute-pcpp1-exam-syllabus.pdf"
source_sha256: 4acafd64c19406395a9140e0b5193ec17f2173709c6df5cf226dc252d10af8ba
pages: 8
min_text_coverage: 1.0
pages_without_graphics: [4, 5, 7, 8]
converter: "pymupdf4llm 0.0.27 + pymupdf 1.26.5 (por página, respaldo sin gráficos; limpieza v1)"
converted: 2026-10-13
---
# **PCPP1™ – Certified Professional in** **Python Programming 1** **(Exam PCPP-32-10x) – EXAM** **SYLLABUS**

## PCPP-32-101 Exam

### Status: Live & Active

**The exam consists of five sections:**


**Section 1 → 15 items** Max Raw Score: 42 (35%)


**Section 2 → 7 items** Max Raw Score: 14 (12%)


**Section 3 → 8 items** Max Raw Score: 24 (20%)


**Section 4 → 8 items** Max Raw Score: 22 (18%)


**Section 5 → 7 items** Max Raw Score: 18 (15%)


Last updated: March 11, 2022


Aligned with Exam PCPP-32-101




|1|Col2|
|---|---|
|||

<!-- fin de página 1 -->

### Section 1: Advanced Object-Oriented Programming (35%)

Objectives covered by the block (15 exam items)


**PCPP-32-101 1.1 – Understand and explain the basic terms and**
**programming concepts used in the OOP paradigm**


  essential terminology: class, instance, object, attribute, method, type,
instance and class variables, superclasses and subclasses

  - reflexion: _isinstance()_, _issubclass()_

  - the ___init__()_ method

  creating classes, methods, and class and instance variables; calling
methods; accessing class and instance variables


**PCPP-32-101 1.2 – Perform Python core syntax operations**


  Python core syntax expressions – magic methods: comparison
methods (e.g. ___eq__(self, other)_ ), numeric methods
(e.g. ___abs__(self)_ ), type conversion methods (e.g. ___init__(self)_ ), object
intro- and retrospection (e.g. ___str__(self)_, ___instancecheck__(self,_
_object)_ ), object attribute access (e.g. ___getattr__(self, attribute)_ ),
accessing containers (e.g. ___getitem__(self, key)_ )

  operating with special methods

  extending class implementations to support additional core syntax
operations


**PCPP-32-101 1.3 Understand and use the concepts of inheritance,**
**polymorphism, and composition**


  - class hierarchies

  single vs. multiple inheritance

  Method Resolution Order (MRO)

  duck typing

  inheritance vs. composition

  modelling real-life problems using the "is a" and "has a" relations


**PCPP-32-101 1.4 Understand the concept of extended function**
**argument syntax and demonstrate proficiency in using decorators**


  - special identifiers: _*args_, _**kwargs_

  forwarding arguments to other functions

  function parameter handling

  - closures

  - function and class decorators

  decorating functions with classes




|2|Col2|
|---|---|
|||

<!-- fin de página 2 -->

  creating decorators and operating with them: implementing
decorator patterns, decorator arguments, wrappers

  decorator stacking

  syntactic sugar

  - special methods: ___call___, ___init___


**PCPP-32-101 1.5 Design, build, and use Python static and class methods**


  implementing class and static methods

  - class vs. static methods

  - the _cls_ parameter

  - the _@classmethod_ and _@staticmethod_ decorators

  class methods: accessing and modifying the state/methods of a class,
creating objects


**PCPP-32-101 1.6 Understand and use Python abstract classes and**
**methods**


  abstract classes and abstract methods: defining, creating, and
implementing abstract classes and abstract methods

  overriding abstract methods

  implementing a multiple inheritance from abstract classes

  delivering multiple child classes


**PCPP-32-101 1.7 Understand and use the concept of attribute**
**encapsulation**


  definition, meaning, usage

  - operating with the _getter_, _setter_, and _deleter_ methods


**PCPP-32-101 1.8 Understand and apply the concept of subclassing built-**
**in classes**


  inheriting properties from built-in classes

  using the concept of subclassing the built-ins to extend class
features and modify class methods and attributes


**PCPP-32-101 1.9 Demonstrate proficiency in the advanced techniques**
**for creating and serving exceptions**


  exceptions as objects, named attributes of exception objects, basic
terms and concepts

  - chained exceptions, the ___context___ and ___cause___ attributes,
implicitly and explicitly chained exceptions

  - analyzing exception traceback objects, the ___traceback___ attribute

  operating with different kinds of exceptions




|3|Col2|
|---|---|
|||

<!-- fin de página 3 -->

**PCPP-32-101 1.10 Demonstrate proficiency in**
**performing** _**shallow**_ **and** _**deep**_ **copy operations**


  - _shallow_ and _deep_ copies of objects

  object: label vs. identity vs. value

  - the _id()_ function and the _is_ operand

  - operating with the _copy()_ and _deepcopy()_ methods


**PCPP-32-101 1.11 Understand and perform (de)serialization of Python**
**objects**


  object persistence, serialization and deserialization: meaning,

purpose, usage

  serializing objects as a single byte stream: the _pickle_ module, pickling
various data types

  - the _dumps()_ and _loads_ functions

  serializing objects by implementing a serialization dictionary:
the _shelve_ module, file modes, creating chelve objects


**PCPP-32-101 1.12 Understand and explain the concept of**
**metaprogramming**


  metaclasses: meaning, purpose, usage

  - the _type_ metaclass and the _type()_ function

  - special attributes: ___name___, ___class___, ___bases___, ___dict___

  operating with metaclasses, class variables, and class methods

### Section 2: Coding Conventions, Best Practices, and Standarization (12%)


Objectives covered by the block (7 exam items)


**PCPP-32-101 2.1 – Understand and explain the concept of Python**
**Enhancement Proposals and Python philosophy**


  the PEP concept and selected PEPs: PEP 1, PEP 8, PEP 20, PEP 257

  PEP 1: different types of PEPs, formats, purpose, guidelines

  PEP 20: Python philosophy, its guiding principles, and design;
the _import this_ instruction and PEP 20 aphorisms


**PCPP-32-101 2.2 – Employ the PEP 8 guidelines, coding conventions, and**
**best practices**


  PEP 8 compliant checkers

  recommendations for code layout: indentation, continuation lines,
maximum line length, line breaks, blank lines (vertical whitespaces)

  default encodings



**4**

<!-- fin de página 4 -->

  module imports

  recommendations for string quotes, whitespace, and trailing
commas: single-quoted vs. double-quoted strings, whitespace in
expressions and statements, whitespace and trailing commas

  recommendations for using comments: block comments, inline

comments

  documentation strings

  naming conventions: naming styles, recommendations

  programming recommendations


**PCPP-32-101 2.3 – Employ the PEP 257 guidelines, conventions, and best**
**practices**


  docstrings: rationale, usage

  comments vs. docstrings

  PEP 484 and type hints

  creating, using, and accessing docstrings

  one-line vs. multi-line docstrings

  - documentation standards, linters, fixers

### Section 3: GUI Programming (20%)


Objectives covered by the block (8 exam items)


**PCPP-32-101 3.1 – Understand and explain the basic concepts and**
**terminology related to GUI programming**


  GUI: meaning, rationale, basic terms and definitions

  visual programming: examples, basic features

  widgets/controls – basic terms: windows, title and title bars, buttons,
icons, labels, etc.

  classical vs. event-driven programming

  - events – basic terms

  widget toolkits/GUI toolkits


**PCPP-32-101 3.2 – Use GUI toolkits, basic blocks, and conventions to**
**design and build simple GUI applications**


  - importing _tkinter_ components

  - creating an application's main window: the _Tk()_, _mainloop()_,
and _title_ methods

  adding widgets to the window: buttons, labels, frames,
the _place()_ method, widget constructors, location, screen
coordinates, size, etc.

  launching the event controller: event handlers, defining and using
callbacks, the _destroy()_ method, dialog boxes

  shaping the main window and interacting with the user



**5**

<!-- fin de página 5 -->

  checking the validity of user input and handling errors

  - working with _Canvas_ and its methods

  - using the _Entry_, _Radiobutton_, and _Button_ widgets

  - managing widgets with the _grid_ and _place_ managers

  - binding events using the _bind()_ method


**PCPP-32-101 3.3 – Demonstrate proficiency in using widgets and**
**handling events**


  settling widgets in the window's interior, geometry managers

  coloring widgets, color modes: RGB, HEX

  event handling: writing event handlers and assigning them to
widgets

  event-driven programming: implementing interfaces using events
and callbacks

  widget properties and methods

  variables: observable variables and adding observers to variables

  using selected clickable and non-clickable widgets

  identifying and servicing GUI events

### Section 4: Network Programming (18%)


Objectives covered by the block (8 exam items)


**PCPP-32-101 4.1 – Understand and explain the basic concepts of**
**network programming**


  - REST

  - network sockets

  Domains, addresses, ports, protocols, and services

  - Network communication: connection-oriented vs. connectionless

communication, clients and servers


**PCPP-32-101 4.2 – Demonstrate proficiency in working with sockets in**
**Python**


  - the _socket_ module: importing and creating sockets

  connecting sockets to HTTP servers, closing connections with servers

  - sending requests to servers, the _send()_ method

  - receiving responses from servers, the _recv()_ method

  exception handling mechanisms and exception types


**PCPP-32-101 4.3 – Employ data transfer mechanisms for network**
**communication**




|6|Col2|
|---|---|
|||

<!-- fin de página 6 -->

  JSON: syntax, structure, data types (numbers, strings, Boolean
values, _null_ ), compound data (arrays and objects), sample JSON
documents and their anatomies

  - the _json_ module: serialization and deserialization, serializing Python
data/deserializing JSON (the _dumps()_ and _loads_ methods), serializng
and deserializing Python objects

  XML: syntax, structure, sample xml documents and their anatomies,
DTD, XML as a tree

  processing xml files


**PCPP-32-101 4.4 – Design, develop, and improve a simple REST client**


  - the _request_ module

  designing, building, and using testing environments

  - HTTP methods: _GET_, _POST_, _PUT_, _DELETE_

  - CRUD

  adding and updating data

  fetching and removing data from servers

  analyzing the server's response

  response status codes

### Section 5: File Processing and Communicating with a Program’s Environment (15%)


Objectives covered by the block (7 exam items)


**PCPP-32-101 5.1 – Demonstrate proficiency in database programming in**
**Python**


  - the _sqlite_ module

  creating and closing database connection using
the _connect_ and _close_ methods

  creating tables

  inserting, reading, updating, and deleting data

  - transaction demarcation

  - cursor methods: _execute_, _executemany_, _fetchone_, _fetchall_

  - creating basic SQL statements ( _SELECT_, _INSERT_
_INTO_, _UPDATE_, _DELETE_, etc.)


**PCPP-32-101 5.2 – Demonstrate proficiency in processing different file**
**formats in Python**


  parsing XML documents

  searching data in XML documents using
the _find_ and _findall_ methods

  - building XML documents using the _Element_ class and
the _SubElement_ function



**7**

<!-- fin de página 7 -->

reading and writing CSV data using functions and
classes: _reader_, _writer_, _DictReader_, _DictWriter_

logging events in applications

working with different levels of logging

using _LogRecord_ attributes to create log formats

creating custom handlers and formatters

parsing and creating configuration files using
the _ConfigParser_ object

- interpolating values in _.ini_ files



**8**

<!-- fin de página 8 -->
