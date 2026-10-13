---
source: "01-evidence/pdf/professional-learning/tensorflow-developer-certificate-candidate-handbook.pdf"
source_sha256: 807e7d104927456c61f2ebc50b680fee185a0c33467fe730935518249d67e0fa
pages: 9
min_text_coverage: 1.0
pages_without_graphics: [7]
converter: "pymupdf4llm 0.0.27 + pymupdf 1.26.5 (por página, respaldo sin gráficos; limpieza v1)"
converted: 2026-10-13
warnings:
  - "páginas con poco texto: [1]"
---
# TensorFlow Developer Certificate

### **Candidate Handbook**

Please review this handbook in its entirety prior to registering and taking the exam.


Last Updated: August 12, 2021

> ⚠️ S01: página 1 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 1 -->

## Contents

### Exam details

Criteria


Skills checklist


Exam environment


Exam time limit


Exam URL

### Candidate identification and authentication Resources allowed during exam Eligibility Registration Fees and payment Taking the exam Results Retaking the exam Length of validity of the certificate Statement of non-discrimination

## Contact


Email: tensorflow-certificate-support@google.com
Web: www.tensorflow.org/certificate


TensorFlow Certificate Candidate Handbook 1

<!-- fin de página 2 -->

## Exam details

### Criteria

The exam tests students in their ability to solve problems by building models using **TensorFlow**

**2.x** .

### Skills checklist


The TensorFlow Developer Certificate exam will test you on this set of skills.


(1) TensorFlow developer skills


You need to demonstrate that you understand how to develop software programs using TensorFlow and
that you can find the information you need to work as an ML practitioner. You need to:


❏ Know how to program in Python, resolve Python issues, and compile and run Python programs

in PyCharm.


❏ Know how to find information about TensorFlow APIs, including how to find guides and API

references on tensorflow.org.


❏ Know how to debug, investigate, and solve error messages from the TensorFlow API.


❏ Know how to search beyond tensorflow.org, as and when necessary, to solve your TensorFlow
questions.


❏ Know how to create ML models using TensorFlow where the model size is reasonable for the
problem being solved.


❏ Know how to save ML models and check the model file size.

❏ Understand the compatibility discrepancies between different versions of TensorFlow.


(2) Building and training neural network models using TensorFlow 2.x


You need to understand the foundational principles of machine learning (ML) and deep learning (DL)
using TensorFlow 2.x. You need to know how to:


❏ Use TensorFlow 2.x.


❏ Build, compile and train machine learning (ML) models using TensorFlow.


❏ Preprocess data to get it ready for use in a model.


❏ Use models to predict results.


❏ Build sequential models with multiple layers.


TensorFlow Certificate Candidate Handbook 2

<!-- fin de página 3 -->

❏ Build and train models for binary classification.


❏ Build and train models for multi-class categorization.


❏ Plot loss and accuracy of a trained model.


❏ Identify strategies to prevent overfitting, including augmentation and dropout.


❏ Use pretrained models (transfer learning).


❏ Extract features from pre-trained models.


❏ Ensure that inputs to a model are in the correct shape.


❏ Ensure that you can match test data to the input shape of a neural network.


❏ Ensure you can match output data of a neural network to specified input shape for test data.


❏ Understand batch loading of data.


❏ Use callbacks to trigger the end of training cycles.


❏ Use datasets from different sources.


❏ Use datasets in different formats, including json and csv.


❏ Use datasets from tf.data.datasets.


(3) Image classification


You need to understand how to build image recognition and object detection models with deep neural
networks and convolutional neural networks using TensorFlow 2.x. You need to know how to:


❏ Define Convolutional neural networks with Conv2D and pooling layers.


❏ Build and train models to process real-world image datasets.


❏ Understand how to use convolutions to improve your neural network.


❏ Use real-world images in different shapes and sizes..


❏ Use image augmentation to prevent overfitting.


❏ Use ImageDataGenerator.


❏ Understand how ImageDataGenerator labels images based on the directory structure.


(4) Natural language processing (NLP)


You need to understand how to use neural networks to solve natural language processing problems
using TensorFlow. You need to know how to:


❏ Build natural language processing systems using TensorFlow.


❏ Prepare text to use in TensorFlow models.


❏ Build models that identify the category of a piece of text using binary categorization


❏ Build models that identify the category of a piece of text using multi-class categorization


TensorFlow Certificate Candidate Handbook 3

<!-- fin de página 4 -->

❏ Use word embeddings in your TensorFlow model.


❏ Use LSTMs in your model to classify text for either binary or multi-class categorization.


❏ Add RNN and GRU layers to your model.


❏ Use RNNS, LSTMs, GRUs and CNNs in models that work with text.


❏ Train LSTMs on existing text to generate text (such as songs and poetry)


(5) Time series, sequences and predictions


You need to understand how to solve time series and forecasting problems in TensorFlow. You need to

know how to:


❏ Train, tune and use time series, sequence and prediction models.


❏ Train models to predict values for both univariate and multivariate time series.


❏ Prepare data for time series learning.


❏ Understand Mean Absolute Error (MAE) and how it can be used to evaluate accuracy of
sequence models.


❏ Use RNNs and CNNs for time series, sequence and forecasting models.


❏ Identify when to use trailing versus centred windows.


❏ Use TensorFlow for forecasting.


❏ Prepare features and labels.


❏ Identify and compensate for sequence bias.


❏ Adjust the learning rate dynamically in time series, sequence and prediction models.

## Note


[Our website, tensorflow.org/certificate recommends](https://tensorflow.org/certificate)

courses for learning the skills that are tested in this

exam. However, the exam does not test the syllabus

of any particular course. The exam may include
questions not specifically addressed in any of the

suggested courses. All knowledge tested in the exam

is adequately covered in the guides and tutorials on
[tensorflow.org.](https://tensorflow.org)


TensorFlow Certificate Candidate Handbook 4

<!-- fin de página 5 -->

### Exam environment

[See "Set up your environment to take the TensorFlow Developer Certifcate Exami](https://www.tensorflow.org/extras/cert/Setting_Up_TF_Developer_Certificate_Exam.pdf) " for more details

on how to make sure your computer is ready to take the exam..


  - You can take the exam from any computer that supports the [PyCharm IDE requirements,](https://www.jetbrains.com/help/pycharm/installation-guide.html)

anywhere there is internet, any time. There is no need to go to a test center.


  - This exam is an online, performance-based test that requires implementing TensorFlow

models using TensorFlow within a PyCharm environment.


  - The exam is expected to take up to 5 hours.


  - In order to take the exam you will install the TensorFlow Exam plugin using the PyCharm

IDE. We recommend you install the PyCharm IDE and become familiar with using it prior

[to taking the exam. Here](https://www.jetbrains.com/help/pycharm/installation-guide.html) are the system requirements for the PyCharm IDE.

### Exam time limit


If you do not press the Submit button before the 5 hours has elapsed, your exam will be auto


submitted. This in itself does not cause you to fail the exam, but you will only be graded for the


questions for which you have already submitted and tested models during the course of taking


the exam.

### Exam URL


[Once you have read this document in its entirety, you can visit the exam URL here.](https://app.trueability.com/google-certificates/tensorflow-developer)

## Candidate identification and authentication


You are required to provide a non-expired Primary ID that contains your photograph, signature and
full name (see acceptable forms of ID in the table below).


If your full name on their Primary ID contains non-latin characters, then you must ALSO provide a

non-expired Secondary ID containing your full name in Latin Characters and signature, OR a

notarized English translation of your Primary ID along with the non-latin character Primary ID.


TensorFlow Certificate Candidate Handbook 5

<!-- fin de página 6 -->

Primary ID (non-expired and including
photograph and signature)


Passport


Government-issued driver’s license/permit
Government-Issued local language ID
(plastic card with photo and signature)


National Identity card


State or province-issued identity card



Secondary ID (non-expired and including
signature with Candidate name in Latin
characters)


Health Insurance Card


U.S. Social Security Card



Exams may be administered to citizens of a sanctioned country listed below PROVIDED the

citizens are tested OUTSIDE the sanctioned country and their exam registration and current ID

show an address OUTSIDE the sanctioned country.


  - Cuba

  - Iran

  - Syria

  - Sudan

  - North Korea

  - Crimea Region of Ukraine

## Resources allowed during exam


You may use whatever learning resources you would normally use during your ML development

work.


TensorFlow Certificate Candidate Handbook 6

<!-- fin de página 7 -->

## Eligibility

You must test as an individual. The certificate is only available for natural persons, not

corporations or other legal entities.

## Registration


You must be registered to be eligible to take the exam. To register for the exam, go [here. To](https://app.trueability.com/google-certificates/tensorflow-developer)

complete the checkout, you will be prompted to enter payment information, and read and accept

the Terms and Conditions for Exam Registration. The exam may be taken at your convenience.

You are not required to take the exam at the time of registration and payment.

## Fees and payment


The exam cost is $100 USD, which includes one exam attempt. You have 6 months from the date
of purchasing the exam to take the exam before your purchase expires. Please note that we are
offering a limited number of stipends to partially cover the cost of taking the TensorFlow
certificate to help ensure this opportunity is accessible for everyone. More details can be found on
[our website.](http://tensorflow.org/certificate)

## Taking the exam


After you download the plugin and sign in, your exam will be provided to you. You will have a
maximum of five hours to complete the exam. If you have not completed the exam after five
hours it will be auto-submitted for you.

## Results


[After you submit your exam, it will be graded and your score will be posted to your Candidate](https://app.trueability.com/user_sessions/new)


[Portal](https://app.trueability.com/user_sessions/new) . If you pass the exam, your name and email will be sent to a third party company who will


TensorFlow Certificate Candidate Handbook 7

<!-- fin de página 8 -->

use your information for the purpose of sending your digital certificate to the email address you

used to purchase the exam.


                        -                         Please contact us at tensorflow certifcatei support@google.com if you passed the exam, but
have not received your digital certificate within ten days or if you would like to opt out of receiving
your certificate.

## Retaking the exam


Please note that you must register and pay for each exam attempt. Our exam retake policy is as


follows:


  If you don't pass on your first attempt, you must wait 14 days before you take the exam

again.


  If you don't pass on your second attempt, you must wait two months before you take the

exam again.


  If after three attempts you still have not passed the exam, you must wait one year before

you take the exam again.

## Length of validity of the certificate


Your certification expires 36 months from the date when you receive your digital badge. To renew

your certification at that time, you need to complete the registration and certificate process again.

## Statement of non-discrimination


TensorFlow endorses the principles of equal opportunity. Eligibility criteria for the TensorFlow
certificate is applied equally to all individuals regardless of age, race, religion, gender, national

origin, veteran status, or disability.


TensorFlow Certificate Candidate Handbook 8

<!-- fin de página 9 -->
