# Introduction

Inspired from the [Mckinsey Report of the Penetration of AI in Banks](https://www.mckinsey.com/~/media/mckinsey/industries/financial%20services/our%20insights/building%20the%20ai%20bank%20of%20the%20future/building-the-ai-bank-of-the-future.pdf), It is now becoming a common use-case where Banks can leverage smart data from IOT devices such as Smart watches to price insurance products accordingly based on the activity level of the person.

This is my attempt at a sample implementation of the same.
NOTE : Only the code is available on github, not the data since the data is over 500MB

# Methodology

The code is written in python, it uses numpy for mathematical manipulations whereas data is fed into pandas into DataFrames.
The data is procured from Kaggle.

There is custom rule created which assess the fitness score.
```
fitness_score = 0.5 * heart_data + 0.3 * step_counts + 0.2 * sleep_duration + np.random.normal(0, 5, num_samples)
fitness_level = ["low" if score < 100 else "moderate" if score < 200 else "high" for score in fitness_score]
```

Based on this, we can classify if a person is fit or not.
This information can then drive underwriting stakeholders within insurance groups to price the insurance appropriately.

The model used is Linear regression from Scikit-learn and Random Forest classifier for classifiying if a person is healthy or not.


# Results

On assessing the fitness score and running it through a regression, We are able to successfully classify a person's data across 20 days, classifying him as healthy or unhealthy.

![My Image](https://github.com/peachypeachyy/portfolio-contents/blob/main/insurance_discount/supporting_assets/insurance_discount_op.png)

If required, these data points can be exposed via API for underwriting teams to arrive at decisions.

NOTE : This is a sample implementation and not a real life solution