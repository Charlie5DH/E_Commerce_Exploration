# E_Commerce_Exploration
Data exploration of E-Commerce in Brazil using Public Dataset by Olist, available at [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce)

The dataset has information of <strong>100k orders from 2016 to 2018</strong> made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: 

- Order status
- Price
- Payment
- Freight Performance to customer location 
- Product attributes 
- Reviews written by customers
- Geolocation dataset that relates Brazilian zip codes to lat/lng coordinates

This is real commercial data, it has been anonymized, and references to the companies and partners in the review text have been replaced with the names of Game of Thrones great houses. 

## Context

Olist connects small businesses from all over Brazil to channels without hassle and with a single contract. Those merchants are able to sell their products through the Olist Store and ship them directly to the customers using Olist logistics partners. See more on our website: [www.olist.com](https://www.olist.com/)

After a customer purchases the product from Olist Store a seller gets notified to fulfill that order. Once the customer receives the product, or the estimated delivery date is due, the customer gets a satisfaction survey by email where he can give a note for the purchase experience and write down some comments.

1. An order might have multiple items.
2. Each item might be fulfilled by a distinct seller.
3. All text identifying stores and partners where replaced by the names of Game of Thrones great houses.

## Data Schema

![](D:\Repositories\E_Commerce_Exploration\image\Data_Schema.png)



## Requirements

- matplotlib
- Python3
- numpy
- Pandas

## Set up the Python environment

Run `conda env create` to create an environment called `E_Commerce`, as defined in `environment.yml`. This environment will provide us with the right Python version as well as the CUDA and CUDNN libraries. (`conda env create -f environment.yml`). We will install Python libraries using `pip-sync`:

Or you can run

```
conda env create --prefix ./env --file environment.yml
```

To create the environment as sub-directory

So, after running `conda env create`, activate the new environment and install the requirements:

```sh
conda activate E_Commerce
pip install -r requirements.txt
```

or, if you use a local environment

```
conda activate ./env
pip install -r requirements.txt
```

If you add, remove, or need to update versions of some requirements, edit the `.in` files, then run

```
pip-compile requirements.in && pip-compile requirements-dev.in
```

## References

- https://www.kaggle.com/olistbr/brazilian-ecommerce