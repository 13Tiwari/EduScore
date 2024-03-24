# EduScore

## Inspiration

We have a desire to help college students take control of their economic situations. This is especially important right now, when job prospects, especially in tech, are not as rosy as they were in the past years. We see this app having the potential to really help students be fiscally responsible and lead them to make smart financial decisions going forward so that they can really succeed.

## What it does

We trained a proprietary machine learning model that accurately predicts your credit score. It then provides information on how you can improve your credit score. It does this without risking your social security number or giving your data to third parties. It also does not affect your credit limit at all.

## How we built it

We found a high-quality data set of labeled credit score data. We then pre-processed the data and trained the model using Scikit-Learn's implementation of the support vector machine algorithm. We also performed hyper-parameter tuning and dropped insignificant features. We exported this model and uploaded it to our backend webserver, hosted on PythonAnywhere. This backend webserver has an API that responds to a form on the user-facing website.

## Challenges we ran into

We faced significant challenges putting our model onto a deployable web server. It was easy to have the model run on a local Flask environment, but finding one that would work for free on the public internet was difficult. We spent time debugging different file formats to store the model and dealt with CORB/CORS security issues. We fixed these by adjusting our HTTP headers.

## Accomplishments that we're proud of

We're proud of the product we produced and the technologies we were able to learn about and implement! Our credit score website could be of meaningful use to anyone trying to navigate the credit system, and we're delighted with our team's collaboration.

## What we learned

We learned about Flask, HTTP headers, frontend and backend development, and troubleshooting.

## What's next for EduScore

We hope to add features that analyze more aspects of credit score to provide an even better model. Our aim is also to refine the website to support higher service loads, ensuring more students and individuals have proper access.

## Built With

- CSS
- Flask
- GitHub
- GoDaddy
- Google
- HTML
- JavaScript
- Kaggle
- LinkedIn
- Porkbun
- PropelAuth
- Python
- Scikit-Learn
- WordPress

## Try it out

[auth.eduscore.courses](auth.eduscore.courses)
