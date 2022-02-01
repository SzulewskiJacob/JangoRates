"""
Definition of views.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
from seaborn import regression
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from forex_python.converter import CurrencyRates

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    c = CurrencyRates()
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'Euro':"{:.4f}".format(c.get_rate('USD','EUR')),
            'Pound':"{:.4f}".format(c.get_rate('USD','GBP')),
            'Ruble':"{:.4f}".format(c.get_rate('USD','RUB'))
        }
    )

def return_graph(data, name):
    plt.title(name)
    plt.xlabel("Date")
    plt.ylabel("Close")
    fig = plt.figure()
    plt.plot(data["Close"])
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data

def pound(request):
    assert isinstance(request, HttpRequest)
    data = pd.read_csv("djangoratesip.azurewebsites.net/PoundHistorical.csv")
    x = data[["Open", "High", "Low"]]
    y = data["Close"]
    x = x.to_numpy()
    y = y.to_numpy()
    y = y.reshape(-1, 1)
    from sklearn.model_selection import train_test_split
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
    from sklearn.tree import DecisionTreeRegressor
    model = DecisionTreeRegressor()
    model.fit(xtrain, ytrain)
    ypred = model.predict(xtest)
    data = pd.DataFrame(data={"Predicted Rate": ypred.flatten()})
    one = data.values.item(1)
    two = data.values.item(2)
    three = data.values.item(3)
    four = data.values.item(4)
    five = data.values.item(5)
    return render(

        request,
        'app/pound.html',
        {
            'title':'Pound',
            'one':one,
            'two':two,
            'three':three,
            'four':four,
            'five':five
        }
    )

def ruble(request):
    assert isinstance(request, HttpRequest)
    data = pd.read_csv("djangoratesip.azurewebsites.net/RubleHistorical.csv")
    x = data[["Open", "High", "Low"]]
    y = data["Close"]
    x = x.to_numpy()
    y = y.to_numpy()
    y = y.reshape(-1, 1)
    from sklearn.model_selection import train_test_split
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
    from sklearn.tree import DecisionTreeRegressor
    model = DecisionTreeRegressor()
    model.fit(xtrain, ytrain)
    ypred = model.predict(xtest)
    data = pd.DataFrame(data={"Predicted Rate": ypred.flatten()})
    one = data.values.item(1)
    two = data.values.item(2)
    three = data.values.item(3)
    four = data.values.item(4)
    five = data.values.item(5)
    return render(

        request,
        'app/ruble.html',
        {
            'title':'Ruble',
            'one':one,
            'two':two,
            'three':three,
            'four':four,
            'five':five
        }
    )

def euro(request):
    assert isinstance(request, HttpRequest)
    data = pd.read_csv("djangoratesip.azurewebsites.net/EuroHistorical.csv")
    graph = return_graph(data, 'EUR - USD Exchange Rate')
    x = data[["Open", "High", "Low"]]
    y = data["Close"]
    x = x.to_numpy()
    y = y.to_numpy()
    y = y.reshape(-1, 1)
    from sklearn.model_selection import train_test_split
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
    from sklearn.tree import DecisionTreeRegressor
    model = DecisionTreeRegressor()
    model.fit(xtrain, ytrain)
    ypred = model.predict(xtest)
    data = pd.DataFrame(data={"Predicted Rate": ypred.flatten()})
    one = data.values.item(1)
    two = data.values.item(2)
    three = data.values.item(3)
    four = data.values.item(4)
    five = data.values.item(5)
    return render(

        request,
        'app/euro.html',
        {
            'title':'Euro',
            'one':one,
            'two':two,
            'three':three,
            'four':four,
            'five':five,
            'graph':graph
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
