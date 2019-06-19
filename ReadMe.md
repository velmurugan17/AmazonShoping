# AmazonShopping automation

This project automates some of basic functionalities of amazon web store

# Setup and Installation

## Chrome driver setup

> This suit is configured to run in chromedriver.Check your current chrome browser version and download related driver https://chromedriver.storage.googleapis.com/index.html.Update config file with downloaded chromedriver path.


```json
"driver":{
    "chrome":"local_path_to_driver"
  }
```

## Python version
> supports python 2.x and 3.x.However current suit is tested with 2.7.13

## Environment setup
1. Create virtual envrionment `virtualenv <environment_name>`

2. Activate virtual environment
    * ubuntu/linux distribution : `source <environment_name>/bin/activate`
    * Windows                   : `<environment_name>\Scripts\activate`
3. Install dependant packages.[use pip3 for py3 environment]
    * `pip install pytest`
    * `pip install selenium`

## config file update
```
Update username,email,password and chromedriver path in config file
```

## Test Execution
```
cd <path_to_repo>/AmazonShoping
pytest --junit-xml=testResult.xml

```

## Security Warning

amazon may requests security verification during first time login.Login once and complete email verification before starting the test incase if any login error is seen during test suit running


## Automated Testcases

| Testcase ID | Testcase |
| ----------- | -------- |
| TC01 | Launch store |
| TC02 | Verify login |
| TC03 | Verify search is working |
| TC04 | Add product to cart |
| TC05 | Add 10 product to cart |
| TC06 | Remove product from cart |
| TC07 | Clear cart |
| TC08 | Get current logged in user |
| TC09 | Get all major categories |
| TC10 | Get all sub categories |
